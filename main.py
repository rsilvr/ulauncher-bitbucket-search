from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import \
    RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

BITBUCKET_ICON = "images/bitbucket.png"
MAX_ITEMS_IN_LIST = 8

class BitbucketSearch(Extension):
    def __init__(self):
        super(BitbucketSearch, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        items = []
        query = event.get_argument() or ""
        keyword = event.get_keyword()

        for kwId, kw in extension.preferences.items():
            if kw == keyword:
                keyword_id = kwId

        if (keyword_id == 'bitbucket'):
            return RenderResultListAction([ExtensionResultItem(icon=BITBUCKET_ICON,
                                                               name="Search for a Bitbucket repository",
                                                               description="Type a repository name",
                                                               on_enter=DoNothingAction())])

if __name__ == '__main__':
    BitbucketSearch().run()
