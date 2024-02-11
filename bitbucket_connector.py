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

  def get_repositories(self, query):
    params = {
        "q": f"slug~\"{query}\" OR name~\"{query}\"",
        "fields": "values.slug,values.links.html.href,next,page,size",
    }
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{self.username}:{self.password}".encode()).decode(),
    }

    response = requests.get(f"https://api.bitbucket.org/2.0/repositories/{self.workspace}", params=params, headers=headers)
    response_payload = response.json()
    response.raise_for_status()
    return [BitbucketRepository(repo.get("slug"), repo.get("links").get("html").get("href")) for repo in response_payload.get("values", [])]
