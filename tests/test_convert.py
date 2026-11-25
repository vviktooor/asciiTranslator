import unittest

from ascii_translator.convert import ascii_to_text, text_to_ascii


class ConvertTest(unittest.TestCase):
    def test_text_to_ascii(self):
        self.assertEqual(text_to_ascii("Hi!"), "72 105 33")

    def test_ascii_to_text(self):
        self.assertEqual(ascii_to_text("72  105\n33 "), "Hi!")

    def test_round_trip_unicode(self):
        text = "Zażółć gęślą jaźń"
        self.assertEqual(ascii_to_text(text_to_ascii(text)), text)

    def test_empty(self):
        self.assertEqual(text_to_ascii(""), "")
        self.assertEqual(ascii_to_text("   "), "")

    def test_invalid_token(self):
        with self.assertRaises(ValueError) as ctx:
            ascii_to_text("72 abc")
        self.assertEqual(str(ctx.exception), "abc")

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            ascii_to_text("99999999")


if __name__ == "__main__":
    unittest.main()
