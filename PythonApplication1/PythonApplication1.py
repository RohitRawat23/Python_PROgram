#print("Hello,World!!")

##
##

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print("sum:",sum)



a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
difference=a-b
print("difference:",difference)


s1 = 'Apple'
s2 = 'Pie'
s3 = 'Sauce'
s4 = s1 + s2 + s3
print(s4)


# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))


def Pig_Latin(word):
    first_letter = word[0]
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
        return pig_word









