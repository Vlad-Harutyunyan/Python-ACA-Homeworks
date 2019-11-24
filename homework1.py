#Question 1 
# initializing number  
num = int(input("Please enter number : "))
  
# printing number  
print ("The original number is " + str(num)) 
  
# to convert number to list of integers 
l = list(map(int, str(num))) 

#getting sum of number
res = l[0]+l[1]+l[2] 

# printing result  
print ("The sum of list from numbers " + str(res))

#Question 2
# initializing numbers a1,a2,n  
a1 = int(input("Please Enter a1 : "))
a2 = int(input("Please Enter a2 : "))
n  = int(input("Please Enter n : "))
#geting  difference
d = a2-a1
#geting an number
a_n = a1 + (n - 1) * d
#printing result 
print(" a[" + str(n) + "] = " + str(a_n))

#Question 3
a = int(input("Please Enter a : "))
b = int(input("Please Enter b : "))
c = int(input("Please Enter c : "))

#sorting
if a < b :
    temp = a
    a = b
    b = temp
if a < c :
    temp = a
    a = c
    c = temp

#getting height    
h = b*b+c*c

if (a>=b+c):
    print("%d No Triangle")
elif (h<a*a):
    print("%d Obtuse Triangle")
elif (h>a*a):
    print("%d Acute Triangle")
else :
    print("%d Right Triangle")

#Question 4
year = int(input("Please Enter the Year Number : "))

if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d Leap Year" %year)
else:
    print("%d Normal Years" %year)



