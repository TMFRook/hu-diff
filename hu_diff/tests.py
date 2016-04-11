from hu_diff import *
from unittest import TestCase


class TestHuDiff(TestCase):
    heredoc1 = """The is the first doctument
    it contains this common line
    and this one too
    """

    heredoc2 = """The is the second doctument
    it contains this common line
    but not this one
    or this one
    """

    def test_is_tuple_result(self):
        expected_result = [
                ('- ', 'The is the first doctument'),
                ('+ ', 'The is the second doctument'),
                ('  ', 'it contains this common line'),
                ('- ', 'and this one too'),
                ('+ ', 'but not this one'),
                ('+ ', 'or this one'),
        ]
        hu_diff = HuDiff()
        result = hu_diff.compare(heredoc1, heredoc2)
        self.assertEqual(result, expected_result)
