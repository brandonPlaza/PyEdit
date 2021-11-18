class Parser:
    def __init__(self):
        self.specialCharacterRaw = ['EXCLAMATION','AT''POUND',
                                  'DOLLAR','PERCENT','ASCIICIRCUM',
                                  'AMPERSAND','ASTERISK','PARENLEFT',
                                  'PARENRIGHT','MINUS','UNDERSCORE', 'PERIOD', 'EQUAL', 'PLUS']

        self.specialCharacterParsed = ['!','@''#',
                                  '$','%','^',
                                  '&','*','(',
                                  ')','-','_','.','=','+']        
    
    def ParseKey(self, keyPressed,character, forbiddenKeys, modifier):
        if keyPressed in forbiddenKeys:
            return ""
        elif '_' in character:
            return self.ParseInteger(character)
        else:
            return self.ParseCharacter(character, modifier)

    def ParseCharacter(self, character, modifier):
        if(character in self.specialCharacterRaw):
            for specialChar in self.specialCharacterRaw:
                if specialChar == character:
                    return self.specialCharacterParsed[self.specialCharacterRaw.index(specialChar)]
        elif(modifier == 0):
            return character.lower()
        elif(modifier > 0):
            return character
        

    def ParseInteger(self, integer):
        for number in range(0,10):
            if(integer.__contains__(str(number))):
                return str(number)
