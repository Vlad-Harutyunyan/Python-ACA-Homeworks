##sorting 
def sorting(arr): 
    if len(arr) > 1: 
        mid = len(arr)//2
        L = arr[:mid]  
        R = arr[mid:] 
        sorting(L) 
        sorting(R) 
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr  

######### QUESTION 1 ###########
#------------------------------------------------------------------------------------#


qst1_l = input('enter array for question 1: ')
qst1_l = qst1_l.split(' ')
qst1_l = [int(qst1_l[ind]) for ind in range(len(qst1_l))]
qst1_l2 = [[],[]]
qst1_l = sorting(qst1_l)
qst1_l = qst1_l[::-1] 
for i in range(len(qst1_l)) :
    if i%2 == 0: 
        qst1_l2[0].append(qst1_l[i])
    else :
        qst1_l2[1].append(qst1_l[i])
print(qst1_l2)  
 

######### QUESTION 2 ###########
#------------------------------------------------------------------------------------#
qst2_l = input('enter array for question 2 : ')
qst2_tmp = int(input('enter backpack capacity, please : '))
qst2_l = qst2_l.split(' ')
qst2_l = [float(qst2_l[ind]) for ind in range(len(qst2_l))]
qst2_l = sorting(qst2_l)
qst2_l = qst2_l[::-1]
cnt = 0
if qst2_tmp > len(qst2_l) :
    qst2_tmp = len(qst2_l)

for i in range (qst2_tmp):
    cnt += qst2_l[i]
print(cnt)  


######### QUESTION 3 ###########
#------------------------------------------------------------------------------------#

qst3_l = input('enter array for question 3 : ')
qst3_l = qst3_l.split(' ')
qst3_l = [int(qst3_l[ind]) for ind in range(len(qst3_l))]
qst3_l2 = [int(qst3_l[ind]) for ind in range(len(qst3_l))]
qst3_l = sorting(qst3_l) 

tmp = []

for i in range(len(qst3_l)) :

    for j in range(len(qst3_l2)):

        if qst3_l[i] == qst3_l2[j] :
            tmp.append(j+1)    
            #set None because 2 person can be same age , so that the index does not repeat
            qst3_l2[j] = None  
 
print(tmp)


######### QUESTION 4 ###########
#------------------------------------------------------------------------------------#
lines = []
with open('AsteroidsDatabase.txt') as f:
        lines = f.read()


lines = lines.split('\n')
temp = []  

for i in lines : 
    temp.append(i.split(' '))
sorted_by_danger = []

#getting most danger asteroids
for i in range(len(temp)):
    sorted_by_danger.append(0)
    for j in range(len(temp[i])):
        temp[i][j] = int(temp[i][j])
        sorted_by_danger[i] += int(temp[i][j]) ** 2

#sort by danger 
swapped = True
while swapped:
    swapped = False
    for i in range(len(sorted_by_danger) - 1):
        if sorted_by_danger[i] > sorted_by_danger[i + 1]:
            sorted_by_danger[i], sorted_by_danger[i + 1] = sorted_by_danger[i + 1], sorted_by_danger[i]
            temp[i],temp[i+1] = temp[i+1],temp[i]
            swapped = True
 
#write asteroids sorted by danger group 

f = open('AsteroidsSortedByDanger.txt','w')
for i in range (len(temp)):
    for j in range(len(temp[i])):
        f.write(str(temp[i][j])+ ' ') 
    f.write('\n')  
f.close()

######### QUESTION 5 ###########
#------------------------------------------------------------------------------------#

## by VLad, a calculator for mode with several elements for searching
##but work only for postive numberrs
n = 10
l = [1,2,3,1,2,3,1,2,1,2]
def count_of_element(l): 
    buckets = []
    res = dict()
    if l[-1] <= 0 :
        for i in range(abs(l[-1])+1) :
            buckets.append(0)
    else:
         for i in range((max(l)+1)) :
            buckets.append(0)
    for i in range(len(buckets)):
        for j in range(len(l)):  
            if i == l[j]: 
                buckets[i] += 1
    for i in range(len(buckets)):
        if buckets[i] > 0 :
            res.update({i:buckets[i]}) 
    return res   
  
l_counted = count_of_element(l)
print(l_counted)
inverse = [(value, key) for key, value in l_counted.items()]
max_count_for_elements = max(inverse)[0]
finallyyyyy = [key  for (key, value) in l_counted.items() if value == max_count_for_elements]
print (finallyyyyy)



######### QUESTION 6 ###########
#------------------------------------------------------------------------------------#

chars = 26 
def countfr(inp, fr, _len): 
  
    for i in range(_len): 
        fr[ord(inp[i]) - ord('a')] += 1 
  
def canMakePalindrome(fr, _len): 

    count_odd = 0 
    for i in range(chars):  
        if (fr[i] % 2 != 0): 
            count_odd += 1 
  
    if (_len % 2 == 0): 
        if (count_odd > 0): 
            return False 
        else: 
            return True 
    if (count_odd != 1): 
        return False 
  
    return True 
  
def findOddAndRemoveItsfr(fr): 
  
    odd_str = "" 
    for i in range(chars): 
        if (fr[i]%2 != 0): 
            fr[i]-=1 
            odd_str += chr(i+ord('a')) 
            return odd_str 
    return odd_str 
  
def findPalindromicString(inp): 
    _len = len(inp) 
  
    fr=[0]*chars 
    countfr(inp, fr, _len) 
  
    if (canMakePalindrome(fr, _len) == False): 
        return "impossible" 

    odd_str = findOddAndRemoveItsfr(fr) 
  
    f_str = "" 
    r_str = " " 
  
    for i in range(chars): 
        temp = "" 
        if (fr[i] != 0): 
            ch = chr(i + ord('a')) 
  
            for j in range(1,int(fr[i]/2)+1): 
                temp += ch 
  
            f_str += temp 
  
            r_str = temp+r_str 
  
    return (f_str + odd_str+r_str) 
qst6_inp = input('type string for cheking polindorme :  ')
print(findPalindromicString(qst6_inp)) 
 