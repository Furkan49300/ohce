class LangueAnglaise():
    def biendit(self):
        return "well said"
    
    def bonjour(self,moment):
        if moment=='matin':
            return "good morning"
        elif moment=='apresmidi':  
            return "goog afternoon"
        elif moment=='soiree':
            return "good evening"
        elif moment=='nuit':
            return "good night" 
        else:
            return "hello"
    
    def aurevoir(self):
        return "good bye"