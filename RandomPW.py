import random

#A function the scramble the characters of a given string
def shuffle(string):
    momList = list(string)
    random.shuffle(momList)
    return ''.join(momList)

upLetter1 = chr((random.randint(65,90))) #Generate a random uppercase letter in the ASCII code
upLetter2 = chr((random.randint(65,90)))
upLetter3 = chr((random.randint(65,90)))
downLetter1 = chr((random.randint(97,122))) #Generate a random lowercase letter in the ASCII code
downLetter2 = chr((random.randint(97,122)))
downLetter3 = chr((random.randint(97,122)))
spcLetter1 = chr((random.randint(35,38))) #Generate a random special character in the ASCII code
spcLetter2 = chr((random.randint(63,64)))
spcLetter3 = chr((random.randint(33,33)))
spcNumber1 = chr((random.randint(48,57))) #Generate a random number in the ASCII code
spcNumber2 = chr((random.randint(48,57)))
spcNumber3 = chr((random.randint(48,57)))

#Generate a password concatenating everything in a random order.
password = (upLetter1 + upLetter2 + upLetter3 + downLetter1 + downLetter2 +
            downLetter3 + spcLetter1 + spcLetter2 + spcLetter3 + spcNumber1 +
            spcNumber2 + spcNumber3)
password = shuffle(password)

Ai_cin = input("Do you want a new password? ")

if Ai_cin == 'yes' or Ai_cin == 'Yes':
    print(f"here is the password: {password}")
else:
    print(f"Here is the password anyway: {password} - We are not taking it back!!")
