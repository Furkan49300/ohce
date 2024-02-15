import unittest
import os
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

    def test_palindrome(self):
        #ETANT donne un palindrome
        str1="kayak"

        #QUAND on dmd si c un palindrome
        resultat=DetecteurPalindrome.isPalindrome(str1)

        #ALORS il est renvoyé suivi de "bien dit"
        attendu=str1 + os.linesep + 'bien dit'
        self.assertIn(attendu, resultat)
    
    def test_bonjour(self):
        #ETANT donne une chaine de caractere
        str1="salut"

        #QUAND on dmd si c un palindrome
        resultat=DetecteurPalindrome.isPalindrome(str1)

        #ALORS bonjour est envoyé avant
        attendu='bonjour'
        res=resultat.split(os.linesep)[0]
        self.assertEqual(attendu, res)



if __name__ == '__main__':
    unittest.main()
