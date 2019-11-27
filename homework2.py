# #Question 1
#getting number as string 
input_number_quest1 = int(input('Type number for question 1, please : '))
start_number = input_number_quest1 
#creating variable
num_sum = 0;
#looping 
while input_number_quest1 > 0:
    num_sum+=input_number_quest1%10
    input_number_quest1 = input_number_quest1//10
    
print('The sum of digits of', start_number, 'is' , num_sum , );
# # --------------------------------------------------------

# #Question 2
input_number_quest2 = int(input('Type number for question 2, please : '))
#set variable for price
price = 0;

while input_number_quest2 > 0:
     # if Given the number plate is biger 10^9 
    if input_number_quest2 > 10**9 :
        print(' Given the number plate is big 10^9')
        break
    #if in car plate numbers we have 8 adding 1000 yuans 
    elif input_number_quest2%10 == 8:
        price += 1000
    input_number_quest2 = input_number_quest2//10
print('Price :' , price , 'yuans')

# # --------------------------------------------------------
# #Question 3
input_number_quest3 = int(input('Type number for question 3, please : '))
#creating checking variable 
check = True
#looping
b = []
while input_number_quest3 > 0 and input_number_quest3 >= 10:
  b.append(input_number_quest3 % 10)
  input_number_quest3 = input_number_quest3 // 10
b = b[::-1] 
if(input_number_quest3 < 10):
    for i in range(len(b)-1) :

        if b[i] < b[i + 1] :
            check = False;
            break;
    #checking
    if check == True :
        print('no')
    else:
        print('yes')
else:
    print('no')
# --------------------------------------------------------
#Question 4

input_number_quest4 = int(input('Type number for question 4, please : '))
#create variable for storing even and add index`s numbers
even = 0;
odd = 0;
#looping
cnt = 0
while input_number_quest4 > 0 :
    #if even
    cnt+=1
    if cnt%2 == 0:
        even+=input_number_quest4%10
    #if odd
    else:
        odd+=input_number_quest4%10
    input_number_quest4=input_number_quest4//10
#checking
if even == odd :
    print('Yes , Lucky')
else :
    print('No , Unlucky')

# --------------------------------------------------------
#Question 5
input_number_quest5 = int((input('Type number for question 5, please : ')))
print(input_number_quest5)
while True :
    if input_number_quest5 < 0 :
        break
    while input_number_quest5 >= 10:
        n_sum = 0
        while input_number_quest5>0:
            d = input_number_quest5 % 10
            input_number_quest5 = input_number_quest5 // 10
            n_sum += d
        input_number_quest5=n_sum  
        print(n_sum)
    break;
# --------------------------------------------------------
#Question 6
input_number_quest6 = int((input('Type number for question 6, please : ')))
#creating variables for 2 different digits 
fe = []
while input_number_quest6 > 0:
  fe.append(input_number_quest6 % 10)
  input_number_quest6 = input_number_quest6 // 10
fe = fe[::-1] 

first_digit = int(fe[0])
second_digit = None
#boolean variable for checking

ch = True
#first loop finding different second variable and store
for x in range(len(fe)) :
    if(first_digit != int(fe[x])):
        second_digit = int(fe[x])
        break;
#second loop just checking are all elements in number  equal or this two or not
for x in range(len(fe)) :
    if first_digit != int(fe[x]) and second_digit != int(fe[x]) :
        ch=False
        break;
#here just checking and typing 
if(second_digit == None):
    print('Dual')
elif(ch == False):
    print('Not dual')
else:
    print('Dual')
