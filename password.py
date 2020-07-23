class Password():
    def __init__(self, value,
        decimal = {'0','1','2','3','4','5','6','7','8','9'},
        upperLetters = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'},
        lowerLetters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'},
        accentedLetters = {'À','Á','Â','Ã','Ä','Å','Æ','Ç','È','É','Ê','Ë','Ì','Í','Î','Ï','Ð','Ñ','Ò','Ó','Ô','Õ','Ö','Ù','Ú','Û','Ü','Ý','Þ','ß','à','á','â','ã','ä','å','æ','ç','è','é','ê','ë','ì','í','î','ï','ð','ñ','ò','ó','ô','õ','ö','ù','ú','û','ü','ý','ÿ'},
        symbolMostUsed = {'!','@','#','$','%','^','&','*'},
        symbol128 = {'~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?','|',' ','\'','"','\\','`'},
        symbol256 = {'~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?','|',' ','\'','"','\\','`','¡','¢','£','¤','¥','¦','§','¨','©','ª','«','¬','®','¯','°','±','²','³','´','µ','¶','·','¸','¹','º','»','¼','½','¾','¿','×','Ø','÷','ø','þ'}):

        self.value = value # plain password
        self.lenght = len(value) # password lenght

        self.unionCharClass = self.calcUnionCharClass(decimal=decimal,upperLetters=upperLetters,lowerLetters=lowerLetters,accentedLetters=accentedLetters,symbolMostUsed=symbolMostUsed,symbol128=symbol128,symbol256=symbol256)
        self.nbOfPossibleChar = len(self.unionCharClass)

        self.complexity = self.nbOfPossibleChar**self.lenght # password complexity = c^n with c the number of potential symbol contained in the password and n the password lenght
        self.strenght = self.calcStrenght() # password strenght in bits such that complexity is less than 2^n with n the strenght in bits

    def calcUnionCharClass(self, decimal, upperLetters, lowerLetters, accentedLetters, symbolMostUsed, symbol128, symbol256):
        """ Calculate the password complexity depending of its lenght and its characters """
        unionCharClass = set() # Use set instead list to make mathematical operations like union, intersection or somethings else
        for char in self.value:
            if char in decimal:
                unionCharClass = unionCharClass.union(decimal)
            elif char in upperLetters:
                unionCharClass = unionCharClass.union(upperLetters)
            elif char in lowerLetters:
                unionCharClass = unionCharClass.union(lowerLetters)
            elif char in accentedLetters:
                unionCharClass = unionCharClass.union(accentedLetters)
            elif char in symbolMostUsed:
                unionCharClass = unionCharClass.union(symbolMostUsed)
            elif char in symbol128:
                unionCharClass = unionCharClass.union(symbol128)
            elif char in symbol256:
                unionCharClass = unionCharClass.union(symbol256)
        return unionCharClass

    def calcStrenght(self):
        """ Calculate the password strenght in bits from the its complexity """
        n = 0
        while(self.complexity >= 2**n):
            n+=1
        return n

    def show(self):
        """ Show results """
        print()
        print('Lenght : {}'.format(self.lenght))
        print('Possible characters : {}'.format(sorted(self.unionCharClass)))
        print('Number of possible characters : {}'.format(self.nbOfPossibleChar))
        print('Complexity : {} (={}^{})'.format(self.complexity, self.nbOfPossibleChar, self.lenght))
        print('Strenght : {} bits (2^{} <= {} < 2^{})'.format(self.strenght, self.strenght-1, self.complexity, self.strenght))
        print()