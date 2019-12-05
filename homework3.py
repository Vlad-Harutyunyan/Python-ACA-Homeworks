#   QUESTION 1 #
# --------------------------------------------------------- #
# getting numbers
length = int(input('enter length , please : '))
height = int(input('enter height , please : '))
#calculate center for i and j 
center = (height-length)//2
# temp var for decrising 
cnt = length
for i in range(height):
    #temp var for decrising 
    cnt2 = length
    print('\n')
    if i > center :
        cnt -= 1
    for j in range(height):
        if j >= center and cnt2 > 0:
            cnt2-=1
            print("*",end=" ")        
        elif i > center and cnt > 0 :
            print("*",end=" ")
        elif i == center : 
            print("*",end=" ")      
        else :    
            print(' ',end=' ')

#   QUESTION 2 #
# --------------------------------------------------------- #
x1 = float(input('type x1 :')) 
y1 = float(input('type y1 :')) 
x2 = float(input('type x2 :')) 
y2 = float(input('type y2 :')) 
x3 = float(input('type x3:')) 
y3 = float(input('type y3 :')) 
x4 = float(input('type x4 :')) 
y4 = float(input('type y4 :'))

def SegmentLength(x1 , x2 , y1 , y2):
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2) , 0.5)

print(SegmentLength(x1,y1,x2,y2) +  SegmentLength(x2,y2,x3,y3) + SegmentLength(x3,y3,x4,y4) + SegmentLength(x1,y1,x4,y4)) 

#   QUESTION 3 #
# --------------------------------------------------------- #
#getting input
inp = int(input('>'))
#function for cheking are number prime or not with true or false 
def is_prime_number(x):
    #numbers higher or equal 2
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else: 
	    return False
    return True

cnt = 0  
#finding prime numbers the amount of which equal enetered number 
for i in range(inp+1//2) :
    for j in range(inp):
        if is_prime_number(i) and is_prime_number(j) and i + j == inp and cnt < 1 :
            cnt+=1
            print(i," + ",j,"=",inp) 

#   QUESTION 4 #
# --------------------------------------------------------- #
#getting inputs
inp_start = int(input('type start : '))
inp_stop = int(input('type stop : '))
# function for getting divisors count for n number
def divCount (num) :
    cnt = 0
    for i in range(1,(num)//2) :
        if num % i == 0 :
            cnt+=1
    return cnt+2;

# calculate number that has the largest number of divisors.
temp_count = 0
temp_num = 0
for i in range(inp_start,inp_stop):
    if temp_count < int(divCount(i)):
        temp_count = int(divCount(i))
        temp_num = i 
print(temp_num)

#   QUESTION 5 #
# --------------------------------------------------------- #
#getting inputs
input_num_for_quest5_1 = int(input("Enter first number : "))
input_num_for_quest5_2 = int(input("Enter second number : "))
#temp arr for store all palindrome numbers from interval [a, b], 
temp_arr = []
#functon for cheking palindrome numbers
def isPalindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n //= 10
    return temp == rev

#looping a:b interval for getting all palindrome munbers 
for i in range(input_num_for_quest5_1,input_num_for_quest5_2):
    if isPalindrome(i):
        temp_arr.append(i)
print(temp_arr) 


#   QUESTION 6 #
# --------------------------------------------------------- #
#getting inputs
inp_number_for_quest6 = int(input('type number ,pleas :'))
 
# a given number n 
def primeFactors(n): 
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2,end=" ")
        n = n / 2
    for i in range(3,int(n**2)+1,2): 
        # while i divides n , print i ad divide n 
        while n % i == 0: 
            print(i,end=" ")
            n = n / i 
    # number greater than 2 
    if n > 2: 
        print(n) 
    print('\n')
 
primeFactors(inp_number_for_quest6) 