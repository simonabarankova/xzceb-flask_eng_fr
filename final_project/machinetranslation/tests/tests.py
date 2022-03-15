import sys
import unittest

sys.path.append("/Users/simonabarankova/Documents/coding/languages/python/flask_exercise/xzceb-flask_eng_fr/final_project/machinetranslation/libs")

from translator import french_to_english, english_to_french


class TestTranslations(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNotNone(french_to_english(None))
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNotNone(english_to_french(None))

unittest.main()