# --------------
#Code starts here
#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
num = 8
rev=palindrome(num)
if num == rev:
	print("number is palindrome",rev)
else:
	print("number is not palindrome",rev)


# --------------
#Code starts here

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)


print(a_scramble("Tom Marvolo Riddle","Voldemort"))
print(a_scramble("ticket","chat"))


# --------------
import math
# if x is perfect square
def isPerfectSquare(x):
   s = int(math.sqrt(x))
   return s*s == x
# if n is a Fibinacci Number
def check_fib(num):
    n=num
    #if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

if (check_fib(145) == True):
    print ("True")
else:
    print ("False")


# --------------
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)
compress("abbs")


# --------------
#Code starts here

#Function to check existence of k distinct characters in string
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k

#Code ends here


