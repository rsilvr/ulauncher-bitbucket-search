from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.event import ItemEnterEvent, KeywordQueryEvent
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from bitbucket_connector import BitbucketConnector

BITBUCKET_ICON = "images/bitbucket.png"
CODE_ICON = "images/code.svg"
PIPELINES_ICON = "images/pipelines.svg"
PULL_REQUEST_ICON = "images/pull-request.svg"
SETTINGS_ICON = "images/settings.svg"
ERROR_ICON = "images/error.svg"

class BitbucketSearch(Extension):
    def __init__(self):
        super(BitbucketSearch, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener()) 


class KeywordQueryEventListener(EventListener):

    def assemble_missing_preference_message(self, preference):
        return RenderResultListAction([
            ExtensionResultItem(
                icon=BITBUCKET_ICON,
                name="Missing Bitbucket preference",
                description=f"Please set your Bitbucket {preference} in the extension preferences",
                on_enter=DoNothingAction()
            )
        ])

    def on_event(self, event, extension):

        items = []

        workspace = extension.preferences.get('workspace', None)
        username = extension.preferences.get('username', None)
        password = extension.preferences.get('password', None)

        if not workspace:
            return self.assemble_missing_preference_message('workspace')
        
        if not username:
            return self.assemble_missing_preference_message('username')
        
        if not password:
            return self.assemble_missing_preference_message('password')            
        
        query = event.get_argument() or ""

        if len(query) < 3:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=BITBUCKET_ICON,
                    name="Search Bitbucket",
                    description="Type at least 3 characters to search for a repository",
                    on_enter=DoNothingAction()
                )
            ])

        connector = BitbucketConnector(workspace, username, password)

        search_terms = query.lower().strip()
        try:
            repositories = connector.get_repositories(search_terms)
        except Exception as err:
            print(err)
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=ERROR_ICON,
                    name="Error fetching repositories",
                    description=f"{err}",
                    on_enter=DoNothingAction()
                )
            ])
        
        if len(repositories) == 0:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=BITBUCKET_ICON,
                    name="No repositories found",
                    description="Try a different search term",
                    on_enter=DoNothingAction()
                )
            ])
        
        for repo in repositories:
            items.append(ExtensionResultItem(
                icon=BITBUCKET_ICON,
                name=repo.name,
                description=repo.url,
                on_enter=ExtensionCustomAction(
                    data={ "name": repo.name, "url": repo.url },
                    keep_app_open=True
                )
            ))
        
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        url = event.get_data().get("url")
        name = event.get_data().get("name")
        items = [
            ExtensionResultItem(
                icon=CODE_ICON,
                name=f"{name} - Source",
                description="Go to main branch code explorer",
                on_enter=OpenUrlAction(url)
            ),
            ExtensionResultItem(
                icon=PULL_REQUEST_ICON,
                name=f"{name} - Pull Requests",
                description="Go to pull requests list",
                on_enter=OpenUrlAction(f"{url}/pull-requests")
            ),
            ExtensionResultItem(
                icon=PIPELINES_ICON,
                name=f"{name} - Pipelines",
                description="Go to pipelines executions list",
                on_enter=OpenUrlAction(f"{url}/pipelines")
            ),
            ExtensionResultItem(
                icon=SETTINGS_ICON,
                name=f"{name} - Settings",
                description="Go to repository settings",
                on_enter=OpenUrlAction(f"{url}/admin")
            )
        ]
        return RenderResultListAction(items)

if __name__ == '__main__':
    BitbucketSearch().run()
