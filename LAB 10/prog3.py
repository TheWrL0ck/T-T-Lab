class ReversedStrings:
    def reverseString(self, s):
        words = s.split(' ')
        string =[]
        for word in words:
            string.insert(0, word)
        print("Reversed String:",end="")
        print(" ".join(string))
        
obj = ReversedStrings()
obj.reverseString("Have a nice day")
    