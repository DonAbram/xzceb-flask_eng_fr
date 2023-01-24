import unittest

from translator import english_to_french, french_to_english

class test_translator (unittest.TestCase):

    def test_english_to_french(self):

        self.assertEqual(english_to_french(None), None)

        self.assertEqual(english_to_french('Hello'), 'Bonjour')

        self.assertNotEqual(english_to_french('Hello'), 'Hola')

    def test_french_to_english(self):

        self.assertEqual(french_to_english(None), None)

        self.assertEqual(french_to_english('Bonjour'), 'Hello')

        self.assertNotEqual(french_to_english('Bonjour'), 'How')

if __name__=='_main_':
    unittest.main()

#Inorder to avoid running this program on CLI to get any response
#the following code can be used

suite = unittest.TestLoader().loadTestsFromTestCase(test_translator)
unittest.TextTestRunner(verbosity=2).run(suite)
