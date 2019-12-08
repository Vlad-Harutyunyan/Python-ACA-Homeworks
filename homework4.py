#question 1
#--------------------------------------------------------------------------------
#Getting numbers 
qst1_inp = (input('please input numbers : '))
qst1_inp = qst1_inp.split(' ')
#temp variable for storing biggist number 
temp = 0
for i in range(len(qst1_inp)):
    if int(qst1_inp[i]) > temp :
        temp = int(qst1_inp[i])
print(sum([temp-int(qst1_inp[i]) for i in range(len(qst1_inp)) ]))

#question 2 
#-------------------------------------------------------------------------------
qst2_inp = (input('please input numbers : '))
qst2_inp = qst2_inp.split(' ')

summ1 = 0
summ2 = 0

for i in range(len(qst2_inp)):
    summ1 += int(qst2_inp[i])
for i in range(1,len(qst2_inp)+2):
    summ2 += i
print(summ2 - summ1)

#question 3 
#-----------------------------------------------------------------------------------
n = int(input('please input number : '))
temp = int(input('please input numbers : '))
acc = dec = 1
for i in range(n-1): 
    n = int(input('please input numbers : '))
    if n == temp : 
        acc = 0 
        dec = 0 
    elif n < temp : 
        acc = 0  
    else :
        dec = 0
if acc :
    print ('Ascending')
elif dec :
    print ('Descending')
else :
    print ('Neither')

#question 4
#-----------------------------------------------------------------------------------
qst4_list = [1.5,2.5,3]
qst4_result = []

for i in range(len(qst4_list)):
    temp = 0;
    for j in range(i,len(qst4_list)):
        temp += qst4_list[j]
    qst4_result.append(temp)
 
print(qst4_result)

#question 5 
#-------------------------------------------------------------------------------------
qst5_list = [1,2,3,4,5,6]
n = 5
#just simple and pytonic way to move array to right | by Vlad
def moveRight(seq, n):
    a = n % len(seq)
    return seq[-a:] + seq[:-a]
print(moveRight(qst5_list,n))
         