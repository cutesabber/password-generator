import random
import re
chara = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '1','2','3','4','5','6','7','8','9','0',
          '@',',','!','"','£','$','%','^','&','*',')',')','-','_','+','=','[',']','{','}','<','>','.','/','?','~','#',':',';','¬','`']
passlength = int(input("How characters do you want your password to have?: "))
password = [ ]
while True:
 for x in range(1,passlength):
    characters = random.sample(chara, passlength)
    password = "".join(characters)
 x = re.findall("[a-z]", password)
 y = re.findall("[A-Z]", password)
 z = re.findall("[0-9]", password)
 a = re.findall("[$#@]", password)
 if x and y and z and a:
    print(password)
    break
 else:
  continue