import os

class DetecteurPalindrome:
    def __init__(self, langue):
        self.__langue = langue

    def isPalindrome(self, str):
        return self.__langue.bonjour() + os.linesep+ str[::-1] + os.linesep+ self.__langue.biendit() + os.linesep+ self.__langue.aurevoir()
        