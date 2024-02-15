import unittest
from detecteurPalindrome import DetecteurPalindrome

class TestPalindrome(unittest.TestCase):
    def test_miroir(self):
        #ETANT donne une chaine de caractere
        str1="salut"

        #QUAND on dmd si c un palindrome
        resultat= DetecteurPalindrome.isPalindrome(str1)

        #ALORS on obtient son miroir
        attendu=str1[::-1]
        self.assertIn(attendu, resultat)

    



if __name__ == '__main__':
    unittest.main()
