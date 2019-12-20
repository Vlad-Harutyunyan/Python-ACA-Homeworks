

# ###question 1 #####
# ------------------------------------------------------------------------------#
qst1_inp1 = int(input('please type number a : '))
qst1_inp2 = int(input('please type number n : '))
def power(a,n) :
    m = 0;
    if n == 0 :
        return  1
    if n % 2 == 0 :
        m = power(a,n/2)
        return m * m
    else :
        return a * power(a,n-1)
 

print(power(qst1_inp1,qst1_inp2))



# ###question 2 #####
# ------------------------------------------------------------------------------#
qst2_inp1 = int(input('please type number for calculate factorial : '))
def factorial(n):
    #1! = 1
    if n == 0:
        return 1 
    #n! = n * (n-1)!
    return n * factorial(n-1)

  
print(factorial(qst2_inp1))


# ###### question 3  ##########
# ------------------------------------------------------------------------------#

run = True
print('Hi !! ,please guess any number in range [1:999] ` ')
tmp1 = 500
tmp2 = 500
cnt = 1
max_num = 0
min_num = 0
while run : 
    
    print('My ',cnt , 'attempt, i thinking that number is ',tmp1,'is it true ? ')

    user_choise = int(input('if your number higher type 1 else -1 if it true type 0 : ')) 
    
    if cnt >= 10 :
        print('I cant lose!!! you cheated')
        run = False;
    elif user_choise == 1 :
        cnt +=1  
        tmp2 //= 2
        tmp1 += tmp2

    elif user_choise == -1 : 
        cnt += 1
        tmp2 //= 2
        tmp1 -= tmp2
    elif user_choise == 0 : 
        print('I won with ' ,cnt,' attempts!!!' )
        run = False; 
    

####### question 4  ##########
#------------------------------------------------------------------------------#
 


  