import os
import unittest
from unittest import mock

from ascii_translator import i18n


class I18nTest(unittest.TestCase):
    def test_same_keys(self):
        self.assertEqual(set(i18n.load("en")), set(i18n.load("pl")))

    def test_no_empty_strings(self):
        for lang in i18n.LANGUAGES:
            self.assertTrue(all(i18n.load(lang).values()), lang)

    def test_app_lang_wins(self):
        with mock.patch.dict(os.environ, {"APP_LANG": "pl"}):
            self.assertEqual(i18n.default_language(), "pl")

    def test_unknown_falls_back_to_english(self):
        with mock.patch.dict(os.environ, {"APP_LANG": "de"}):
            self.assertEqual(i18n.default_language(), "en")


if __name__ == "__main__":
    unittest.main()
