print("Guten tag welcome to a function that counts")
def count_spaces(s):
    return s.count(" ")

def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    numY = s.count("y")
    sumVowels = numA + numE + numO + numU + numY
    return sumVowels

    def count_total(s):
        return count_spaces + count_vowels

print(count_spaces("Guten tag, nice that you came"))

countNum = count_vowels("Guten tag, nice nice that you came")
print(countNum)
print(count_total)
