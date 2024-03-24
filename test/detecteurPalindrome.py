import os

class DetecteurPalindrome:
    def __init__(self, langue,moment):
        self.__langue = langue
        self.__moment=moment

    def isPalindrome(self, str):
        return self.__langue.bonjour(self.__moment) + os.linesep+ str[::-1] + os.linesep+ self.__langue.biendit() + os.linesep+ self.__langue.aurevoir()
        