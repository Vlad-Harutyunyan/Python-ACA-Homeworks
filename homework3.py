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
        elif i > center and cnt > 1 :
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
# max number , uppercase becouse it is Constanta and cant changed .
MAX = 10000; 
#getting number for solving 
input_number = int(input('type number for solving Goldbach’s Conjecture : '))
# Array to store all prime less  
# than and equal to 10^6 
primes = []; 
  
def sieveSundaram(): 
    # primes smaller than (2*x + 2) for a  
    # number given number x. Since we want  
    # primes smaller than MAX, we reduce  
    # MAX to half. This array is used to  
    # separate numbers of the form i + j + 2*i*j  
    # from others where 1 <= i <= j 
    marked = [False] * (int(MAX / 2) + 100); 
    # number by doing 2*i+1 
    for i in range(1, int((MAX*2 - 1) / 2) + 1): 
        for j in range((i * (i + 1)) << 1,  
                        int(MAX / 2) + 1, 2 * i + 1): 
            marked[j] = True; 
    # Since 2 is a prime number 
    primes.append(2); 
    # Print other primes. Remaining primes  
    # are of the form 2*i + 1 such that  
    # marked[i] is false. 
    for i in range(1, int(MAX / 2) + 1): 
        if (marked[i] == False): 
            primes.append(2 * i + 1); 
            
# Function to perform Goldbach's conjecture 
def findPrimes(n): 
    # Return if number is not even  
    # or less than 3 
    if (n <= 2 or n % 2 != 0): 
        print("Invalid Input"); 
        return; 
    # Check only upto half of number 
    i = 0; 
    while (primes[i] <= n // 2): 
        # find difference by subtracting  
        # current prime from n 
        diff = n - primes[i]; 
        # Search if the difference is also 
        # a prime number 
        if diff in primes: 
            # Express as a sum of primes 
            print(primes[i], diff); 
            return; 
        i += 1; 

# Finding all prime numbers before limit 
sieveSundaram();  
findPrimes(input_number); 

#   QUESTION 4 #
# --------------------------------------------------------- #
#getting inputs
inp_start = int(input('type start : '))
inp_stop = int(input('type stop : '))

# function for getting divisors count for n number
def divCount(n): 
  
    # sieve method for 
    # prime calculation 
    hh = [1] * (n + 1); 
      
    p = 2; 
    while((p * p) < n): 
        if (hh[p] == 1): 
            for i in range((p * 2), n, p): 
                hh[i] = 0; 
        p += 1; 
    # Traversing through  
    # all prime numbers 
    total = 1; 
    for p in range(2, n + 1): 
        if (hh[p] == 1): 
            count = 0; 
            if (n % p == 0): 
                while (n % p == 0): 
                    n = int(n / p); 
                    count += 1; 
                total *= (count + 1); 
                  
    return total; 

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
        n = n // 10
    if(temp == rev):
        return True
    else:
        return False

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
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 

    for i in range(3,int(n**2)+1,2): 

        # while i divides n , print i ad divide n 
        while n % i == 0: 
            print(i,end=" ")
            n = n / i 
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n) 
    print('\n')
    
primeFactors(inp_number_for_quest6) 