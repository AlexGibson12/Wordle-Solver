class Wordle:
    def __init__(self,words,possiblewords):
        self.words = words
        self.possiblewords = set(possiblewords)
    def ComputeColours(self,word1,word2):
        letters = set([i for i in word2])
        colours = ''
        for index in range(len(word1)):
            if word1[index]==word2[index]:
                colours+='G'
            elif word1[index] in letters:
                colours+='Y'
            else:
                colours+='B'
        return colours
    def maxremainingwords(self,word):
        setlengths = {} 
        for j in self.possiblewords:
            colour = self.ComputeColours(word,j) 
            if not colour in setlengths.keys():
                setlengths[colour] = 1
            else:
                setlengths[colour]+=1
        maximum = max([setlengths[i] for i in setlengths.keys()])
        return maximum
    def getnextword(self):
        minmaximalwords = -1
        bestword = ''
        l = 0
        different = False
        for i in self.words:    
            maximum = self.maxremainingwords(i)
            if maximum>1:
                different = True
            if minmaximalwords == -1 or minmaximalwords >= maximum:
                bestword = i
                minmaximalwords = maximum    
        if different:
            return bestword
        else:
            return list(self.possiblewords)[0]

    def play(self,word,colourcode):
        wordstoerase = []
        for possibility in self.possiblewords:
            if self.ComputeColours(word,possibility)!=colourcode:
                wordstoerase.append(possibility)
        for word in wordstoerase:
            self.possiblewords.remove(word)

f = open("words.txt","r")
words = [i.strip() for i in f.readlines()]
f = open("possiblewords.txt","r")
possiblewords = [i.strip() for i in f.readlines()]
wordle = Wordle(words,possiblewords)
currentword = "serai"
while True:
    print(currentword)
    colourcode = input("Colour Combination:")
    wordle.play(currentword,colourcode)
    savedword = currentword
    currentword = wordle.getnextword()
    if currentword==savedword:
        break
print(f'Success! The word is {currentword}')
    

