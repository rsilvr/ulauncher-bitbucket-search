import requests
import base64

class BitbucketRepository:

  def __init__(self, name, url):
    self.name = name
    self.url = url

class BitbucketConnector:

  def __init__(self, workspace, username, password):
    self.workspace = workspace
    self.username = username
    self.password = password
    self.headers = {
        "Authorization": "Basic " + base64.b64encode(f"{self.username}:{self.password}".encode()).decode(),
    }

  def handle_query(self, url, params, limit, results = None):
    results = results or []
    response = requests.get(url, params=params, headers=self.headers)
    response_payload = response.json()
    response.raise_for_status()
    new_items_to_append = limit - len(results)
    results.extend(response_payload.get("values", [])[:new_items_to_append])
    if len(results) < limit and response_payload.get("next"):
        page = response_payload.get("page") + 1
        params["page"] = page
        return self.handle_query(url, params, limit, results)
    return results

  def get_repositories(self, query, limit):
    params = {
        "q": f"slug~\"{query}\" OR name~\"{query}\"",
        "fields": "values.slug,values.links.html.href,next,page",
        "sort": "-updated_on"
    }
    repositories = self.handle_query(f"https://api.bitbucket.org/2.0/repositories/{self.workspace}", params, limit)
    return [BitbucketRepository(repo.get("slug"), repo.get("links").get("html").get("href")) for repo in repositories]
