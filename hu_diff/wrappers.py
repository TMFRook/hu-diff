import difflib


class HuDiff(object):
    differ = None

    def __init__(self):
        self.differ = difflib.Differ()

    def compare(self, *args, **kwargs):
        result = self.differ.compare(*args, **kwargs)
        return [(i[:2], i[2:]) for i in result]
