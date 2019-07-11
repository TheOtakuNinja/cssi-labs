print("Guten tag welcome to the loop playground")

myString = raw_input("Give me a string loop through: ")

letterNum = 1


for character in myString:
    print("this is letter number %d" %(letterNum))
    letterNum = letterNum + 1
    print(character)
