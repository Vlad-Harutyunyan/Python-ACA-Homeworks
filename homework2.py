# #Question 1
#getting number as string 
input_number_quest1 = (input('Type number for question 1, please : '))
#creating variable
num_sum = 0;
#looping 
for x in range(len(input_number_quest1)):
    if int(input_number_quest1[x]) != 0  :
        num_sum += int(input_number_quest1[x])
    
print('The sum of digits of', input_number_quest1, 'is' , num_sum , );
# # --------------------------------------------------------

# #Question 2
input_number_quest2 = (input('Type number for question 2, please : '))
#set variable for price
price = 0;

for x in range(len(input_number_quest2)):
    if int(input_number_quest2[x])==8 :
    #if in car numbers we have 8 adding 1000 yuans 
        price += 1000


# if Given the number plate is biger 10^9 
if int(int(input_number_quest2)) > 10**9 :

    print(' Given the number plate is big 10^9')
else :
    print('Price :' , price , 'yuans')
# # --------------------------------------------------------
# #Question 3
input_number_quest3 = (input('Type number for question 3, please : '))
#creating checking variable 
check = True
#looping
for i in range(len(input_number_quest3)-1) :

    if input_number_quest3[i] < input_number_quest3[i + 1] :
        check = False;
        break;
#checking
if check == True :
    print('no')
else:
    print('yes')    

# --------------------------------------------------------
#Question 4
input_number_quest4 = (input('Type number for question 4, please : '))
#create variable for storing even and add index`s numbers
even = 0;
odd = 0;
#looping
for x in range(len(input_number_quest4)):
    #if even
    if x%2==0 :
        even+= int(input_number_quest4[x])
    #if odd
    else :
        odd += int(input_number_quest4[x])
#checking
if even == odd :
    print('Yes , Lucky')
else :
    print('No , Unlucky')

# --------------------------------------------------------
#Question 5
input_number_quest5 = int((input('Type number for question 5, please : ')))
print(input_number_quest5)
n_sum = 0;
while True :
    if input_number_quest5 < 0 :
        break
    while input_number_quest5 >= 10:
        n_sum = 0
        while input_number_quest5>0:
            d = input_number_quest5 % 10;
            input_number_quest5 = input_number_quest5 // 10;
            n_sum += d;
        input_number_quest5=n_sum  
        print(n_sum)
        break;
     
# --------------------------------------------------------
#Question 6
input_number_quest6 = ((input('Type number for question 6, please : ')))
#creating variables for 2 different digits 
first_digit = int(input_number_quest6[0])
second_digit = None
#boolean variable for checking
ch = True
#first loop finding different second variable and store
for x in range(len(input_number_quest6)) :
    if(first_digit != int(input_number_quest6[x])):
        second_digit = int(input_number_quest6[x])
        break;
#second loop just checking are all elements in number  equal or this two or not
for x in range(len(input_number_quest6)) :
    if first_digit != int(input_number_quest6[x]) and second_digit != int(input_number_quest6[x]) :
        ch=False
        break;
#here just checking and typing 
if(second_digit == None):
    print('Dual')
elif(ch == False):
    print('Not dual')
else:
    print('Dual')
