class LangueFrancaise():
    def biendit(self):
        return "bien dit"
    
    def bonjour(self, moment):
        if moment=='matin':
            return "bonjour_am"
        elif moment=='apresmidi':  
            return "bonjour_pm"
        elif moment=='soiree':
            return "bonjour_soir"
        elif moment=='nuit':
            return "bonjour_nuit"  
        else:
            return 'bonjour'    
    
    def aurevoir(self):
        return "au revoir"