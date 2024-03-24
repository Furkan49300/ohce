from detecteurPalindrome import DetecteurPalindrome
from langueStub import LangueStub


class DetecteurPalindromeBuilder():
    __langue = LangueStub()
    __moment= LangueStub()
    
    def build(self):
        return DetecteurPalindrome(self.__langue, self.__moment)

    def isLangue(self, langue):
        self.__langue = langue
        return self
    
    def isMoment(self, moment):
        self.__moment=moment
        return self