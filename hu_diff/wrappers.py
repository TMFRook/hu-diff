import difflib


class HuDiff(difflib.Differ):
    def compare(self, *args, **kwargs)
        result = super(HuDiff, self).compare(*args, **kwargs)
        return [(i[:2], i[2:]) for i in result]
