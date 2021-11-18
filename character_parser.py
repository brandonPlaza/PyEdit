class Parser:
    def __init__(self):
        pass

    def ParseCharacter(self, character, modifier):
        print("{0} , {1}".format(character, modifier))
        if(character == 'EXCLAMATION'):
            return '!'
        elif(modifier == 0):
            return character.lower()
        elif(modifier > 0):
            return character
        

    def ParseInteger(self, integer):
        for number in range(0,10):
            if(integer.__contains__(str(number))):
                return str(number)
