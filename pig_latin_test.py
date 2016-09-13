import unittest
from pig_latin import *

class TestPigLatin(unittest.TestCase):

    def test_vowel(self):
        self.assertTrue(is_vowel('a'))
        self.assertFalse(is_vowel('t'))
        self.assertTrue(is_vowel('o'))
        self.assertTrue(is_vowel('e'))

    def test_cut(self):
        self.assertEqual(cut("String"), ("Str", "ing"))
        self.assertNotEqual(cut("brother"), ("bro", "ther"))
        self.assertEqual(cut("cake"), ("c", "ake"))
        self.assertEqual(cut("another"), ("", "another"))

    def test_piggify_word(self):
        self.assertEqual(piggify_word("apple"), "applehay")
        self.assertEqual(piggify_word("string"), "ingstray")
        self.assertNotEqual(piggify_word("apple"), "hayapple")
        self.assertEqual(piggify_word("airplane"), "airplanehay")
        self.assertEqual(piggify_word("make"), "akemay")


    def test_clean_word(self):
        self.assertEqual(clean_word("Wow!"), ("Wow","!"))
        self.assertNotEqual(clean_word("Nah~"), ("Na", "h~"))
        self.assertEqual(clean_word("Yeah!"), ("Yeah", "!"))
        self.assertEqual(clean_word("Now"), ("Now", ""))

    def test_get_raw_words(self):
        self.assertEqual(get_raw_words("Madam, I'm Adam."), ["Madam,", "I'm", "Adam."])
        self.assertEqual(get_raw_words("Get out!"), ["Get", "out!"])
        self.assertEqual(get_raw_words("Go~ to, hell!"), ["Go~", "to,", "hell!"])        

    def test_piggify_pairs(self):
        self.assertEqual(piggify_pairs([("hi", ""), ("there", "!")]), [("ihay", ""), ("erethay", "!")])
        self.assertEqual(piggify_pairs([("Look", " "), ("at", " "), ("that", ".")]), [("ookLay", " "), ("athay", " "), ("atthay", ".")])

    def test_reassemble(self):
        self.assertEqual(reassemble([("ihay", ""), ("erethay", "!")]),  "ihay erethay!")
        

    def test_piggify_sentence(self):
        self.assertEqual(piggify_sentence("hi, there!"), "ihay, erethay!")
    



unittest.main()
