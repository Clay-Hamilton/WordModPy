'''
Created on Feb 17, 2019

@author: clayham
An aggregation of all of my word-modifying functions

TODO:
-add copy/paste functions
-add "help _" commands to explain what each function does to the user
-flesh out passStrengthTest (possibly include most common passwords)

'''
from functools import reduce
import re

#Isogram: checks if a word is an isogram (a word only containing each letter once):
def isIsogram(teststring):
    isIso = True
    for i in range(len(teststring)):
        isIso = isIso and teststring.count(teststring[i]) == 1
    return isIso

#camelCase: converts any teststring to camelCase:
def toCamelCase(teststring):
    new = "".join(teststring[i].upper() if (teststring[i-1] == "-" or teststring[i-1] == "_") else teststring[i] for i in range(len(teststring)))
    new2 = new.replace("-", "")
    new3 = new2.replace("_", "")
    return new3

#Persistence: tests how many times you have to multiply the digits of a number by each other 
# until you get a single digit number
def persistence(num):
    count = 0
    nums = []
    while True:
        if len(str(num)) > 1:
            nums = [int(d) for d in str(num)]
            num = reduce(lambda x,y: x*y, nums)
            count += 1
        else:
            break
    return count

#ParenthesisEncode: encodes each character in a string to ")" if the character appears
# more than once, or "(" if it only appears once
def parenthesisEncode(word):
    word = word.lower()
    s = ""
    for i in range(len(word)):
        if word.count(word[i]) > 1:
            s += ")"
        else:
            s += "("
    return s

#CipherEncode: Encodes the string using the given map.
def cipherEncode(words):
    cipher ={"A":"T","a":"T","B":"D","b":"D","C":"L","c":"L","D":"O","d":"O","E":"F","e":"F","F":"A","f":"A","G":"G","g":"G","H":"J","h":"J","I":"K","i":"K","J":"R","j":"R","K":"I","k":"I","L":"C","l":"C","M":"V","m":"V","N":"P","n":"P","O":"W","o":"W","P":"U","p":"U","Q":"X","q":"X","R":"Y","r":"Y","S":"B","s":"B","T":"E","t":"E","U":"Z","u":"Z","V":"Q","v":"Q","W":"S","w":"S","X":"N","x":"N","Y":"M","y":"M","Z":"H","z":"H"}
    result = ''
    for letter in words:
        if letter in cipher:
            result = result + cipher[letter]
        else:
            result = result + letter
    return result

#PassStrengthTest: uses regex to test if a given password is strong 
#  (contains at least 1 upper/lowercase letter, 1 number, and is at least 8 characters long)
def passStrengthTest(password):
    #inp = input("Do you want to test a password\n")

    regchekupper = re.compile("[a-z]\S*?[A-Z]|[A-Z]\S*?[a-z]")
    regcheknum = re.compile("\S*\d\S*")
    regcheklength = re.compile("\S{8,}")
    ret = ""
    isStrong = 0

    if (regchekupper.search(password)) == None:
        ret += "Your password does not have at least one upper and lowercase letter.\n"
        isStrong = isStrong + 1  
    if (regcheknum.search(password)) == None:
        ret += "Your password does not have a number.\n"
        isStrong = isStrong + 1
    if (regcheklength.search(password)) == None:
        ret += "Your password is not long enough.\n"
        isStrong = isStrong + 1
            
    if (isStrong == 0):
        print("Your password is strong!")
    else:
        print(ret)


inputstring = raw_input("Please enter a string, or type p to use the string from your clipboard.\n")
whichmod = input("Press 1 for Isogram, 2 for camelCase, 3 for Persistence, 4 for ParenEncode, \n5 for CipherEncode, or 6 for PassStrengthTest. Type q to quit.\n")
result = ""
if (whichmod == 1):
    result = isIsogram(inputstring)
elif (whichmod == 2):
    result = toCamelCase(inputstring)
elif (whichmod == 3):
    result = persistence(inputstring)
elif (whichmod == 4):
    result = parenthesisEncode(inputstring)
elif (whichmod == 5):
    result = cipherEncode(inputstring)
elif (whichmod == 6):
    passStrengthTest(inputstring)
    
if (whichmod != 6):
    print("You entered %s. \nYour result is %s" % (inputstring,result))
