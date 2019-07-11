name=raw_input("Enter your name: ")
print("Guten tag %s welcome to the function play thingy" %(name))


name1 = raw_input("Give me a word: ")
def reverse_string(x):
    return x[::-1]
print("This is your word backwards: " + reverse_string(name1))



















#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# word1 = raw_input("Give me a word: ")
# word2 = raw_input("Give me another one: ")
# word3 = raw_input("And another one: ")
#
# def lonest_word(w1, w2, w3):
#
#     if len(w1) > len(w2) and  len(w1) > len(w3):
#        print("%s is the largest word outa %s and %s" %(w1, w2, w3))
#        return longest_word
#     elif len(w2) > len(w1) and  len(w2) > len(w3):
#        print("%s is the largest word outa %s and %s" %(w2, w1, w3))
#        return longest_word
#     elif len(w2) > len(w1) and  len(w2) > len(w3):
#         print("%s is the largest word outa %s and %s" %(w3, w1, w2))
#         return longest_word
#     else:
#         print("yo why would you choose 3 words that are the same size REEEEEEEE")
#         return longest_word
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# num1 = int(raw_input("Give me a side length: "))
# num2 = int(raw_input("Give me another one: "))
# num3 = int(raw_input("And another one : "))
#
# def is_triangle(s1, s2, s3):
#     sum1 = s1 + s2 #test if greater than s3
#     sum2 = s2 + s3 #test if greater than s1
#     sum3 = s3 + s1 #test if greater than s2
#     if sum1 > s3 and sum2 > s1 and sum3 > s2:
#         print("You gett'em, %s got that triangle good" %(name))
#         return True #Triangle got
#
#     else:
#         print("Mission failed we'd get'em next time, triangle lost")
#         return False #Mission failed we'd get'em next time
#
#
#
# is_triangle(num1, num2, num3)
