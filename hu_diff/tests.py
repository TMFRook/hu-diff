from hu_diff import *
from unittest import TestCase
from StringIO import StringIO


class TestHuDiff(TestCase):
    heredoc1 = StringIO("""The is the first doctument
it contains this common line
and this one too
""")

    heredoc2 = StringIO("""The is the second doctument
it contains this common line
but not this one
or this one
""")

    def test_is_tuple_result(self):
        expected_result = [
                ('- ', 'The is the first doctument\n'),
                ('? ', '           --- ^\n'),
                ('+ ', 'The is the second doctument\n'),
                ('? ', '            ^^^^^\n'),
                ('  ', 'it contains this common line\n'),
                ('- ', 'and this one too\n'),
                ('+ ', 'but not this one\n'),
                ('+ ', 'or this one\n'),
        ]
        hu_diff = HuDiff()
        result = hu_diff.compare(self.heredoc1.readlines(), self.heredoc2.readlines())
        self.assertEqual(result, expected_result)
