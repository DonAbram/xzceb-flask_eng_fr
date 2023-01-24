import unittest

from translator import englishToFrench, frenchToEnglish

class test_translator (unittest.TestCase):

    def test_englishToFrench(self):

        self.assertEqual(englishToFrench(None), None)

        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):

        self.assertEqual(frenchToEnglish(None), None)
        
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__=='_main_':
    unittest.main()

#Inorder to avoid running this program on CLI to get any response
#the following code can be used

suite = unittest.TestLoader().loadTestsFromTestCase(test_translator)
unittest.TextTestRunner(verbosity=2).run(suite)
