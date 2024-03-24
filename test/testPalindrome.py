import unittest
import os
from detecteurPalindrome import DetecteurPalindrome
from detecteurPalindromeBuilder import DetecteurPalindromeBuilder
from langueFrancaise import LangueFrancaise
from langueAnglaise import LangueAnglaise

class TestPalindrome(unittest.TestCase):
    def test_miroir(self):
        #ETANT donne une chaine de caractere
        str1="salut"

        #QUAND on dmd si c un palindrome
        resultat= DetecteurPalindromeBuilder().build().isPalindrome(str1)

        #ALORS on obtient son miroir
        attendu=str1[::-1]
        self.assertIn(attendu, resultat)

    def test_palindrome(self):
        langues = [[LangueFrancaise(), 'bien dit'],[LangueAnglaise(), 'well said']]
        #ETANT donne un palindrome et une langue
        str1="kayak"
        for i in langues:
            with (self.subTest(i[0])):
                langue=i[0]

        #QUAND on dmd si c un palindrome
                resultat=DetecteurPalindromeBuilder().isLangue(langue).build().isPalindrome(str1)

        #ALORS il est renvoyé suivi de "bien dit"
                attendu=str1 + os.linesep + i[1]
                self.assertIn(attendu, resultat)
    
    def test_bonjour(self):
        langues = [[LangueFrancaise(), 'bonjour'],[LangueAnglaise(), 'hello']]

        #ETANT donne une chaine de caractere et une langue
        str1="salut"
        for i in langues:
            with (self.subTest(i[0])):
                langue=i[0]

        #QUAND on saisit la chaine
        resultat=DetecteurPalindromeBuilder().isLangue(langue).build().isPalindrome(str1)

        #ALORS bonjour de cette langue est renvoyé avant
        attendu=i[1]
        res=resultat.split(os.linesep)[0]
        self.assertEqual(attendu, res)

    def test_aurevoir(self):
        langues = [[LangueFrancaise(), 'au revoir'],[LangueAnglaise(), 'good bye']]
        #ETANT donne une chaine de caractere et une langue
        str1="salut"
        for i in langues:
            with (self.subTest(i[0])):
                langue=i[0]

        #QUAND on dmd saisit la chaine
        resultat=DetecteurPalindromeBuilder().isLangue(langue).build().isPalindrome(str1)

        #ALORS au revoir est envoyé en dernier
        attendu=i[1]
        res= resultat.split(os.linesep)[-1]
        self.assertEqual(attendu, res)


if __name__ == '__main__':
    unittest.main()
