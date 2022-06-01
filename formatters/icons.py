from common import TreePathInfo

from formatters.formatter import Formatter

_EXT_TO_ICON = {
    ".py": '🐍',
    ".pyc": '🐍',
    ".cfg": '🛠',
}

_FILE_ICON = '📄'
_FOLDER_ICON = '📂'


class Icons(Formatter):
    """"""
    def format(self, tpi:TreePathInfo):
        if tpi.is_file:
            tpi.icon = _EXT_TO_ICON.get(tpi.ext, _FILE_ICON)
        else:
            tpi.icon = _FOLDER_ICON
