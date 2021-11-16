
  
import random as r


class encrypter:
    """     docstring for encrypter      """

    def __init__(self):
        self.a = "abcdefghijklmnopqrstuvwxyz#*&@$"     #len = 31
        self.b = "%wqertyuiop*asdf-ghjkl4zxcvb#nm"     #len = 31    %*#-4
        self.c = "0123456789.%-"       #len = 13
        self.d = "50@239^$7&681"       #len = 13
        self.rand = 0

    def setUniqueID(self):
        min = 1
        max = 6
        return (min + r.randint(min, max))  #random

    def joiner(self, Str, letter_sp):
        Str += str(letter_sp)
        return Str

    def rev(self, x):
      return x[::-1]

    def encodeAlter(self):
        self.a = self.__rev(self.a)

        self.t = self.a[0]
        self.a = self.a[1:]
        self.a += self.t

        self.a = self.__rev(self.a)


    def encode(self, inp):
        self.rand = self.__setUniqueID()

        inp = inp.lower()
        letter_sp = '0'

        string = str(self.rand)
        letter_sp = string[0]
        for i in range(1, self.rand+1):
            match = self.c[i]
            if letter_sp == match:
                letter_sp = self.d[i]
                break


        for i in range(self.rand):
            self.__encodeAlter()

        temp = ""
        for Str in range(len(inp)):
            letter = inp[Str]
            if letter.isalpha() or letter=='#' or letter=='*' or letter=='&' or letter=='@' or letter=='$':
                for i in range(31):
                    match = self.a[i]
                    if letter == match:
                        temp += str(self.b[i])
                        self.__encodeAlter()
                        break

            elif letter.isnumeric() or letter=='.' or letter=='%' or letter=='-': # Encrypting Digits
                for i in range(13):
                    match = self.c[i]
                    if letter == match:
                        temp += str(self.d[i])
                        self.__encodeAlter()
                        break

            elif letter == '\n':
                temp += str('\n')

            else:
                temp += str(letter)


        return self.__joiner(temp, letter_sp)




    __setUniqueID = setUniqueID
    __joiner = joiner
    __rev = rev
    __encodeAlter = encodeAlter
# ends class

def mainFun(msg):
    begin = encrypter()
    return begin.encode(msg)
# ends main