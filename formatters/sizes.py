from os.path import getsize, join

from tree.common import TreePathInfo
from tree.formatters.formatter import Formatter


class Sizes(Formatter):
    """Get filesize and set its value"""
    def format(self, tpi:TreePathInfo):
        try:
            tpi.size = str(getsize(join(tpi.root, tpi.name)))
        except FileNotFoundError:
            pass
