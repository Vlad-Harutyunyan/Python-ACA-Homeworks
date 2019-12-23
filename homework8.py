####### 1d logistics  ##########
#------------------------------------------------------------------------------#

#sorting algoritm
l = [1,1,7,1,2,1,7,6,-1,0]
def sorting(arr): 
    if len(arr) >1: 
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
  
l = sorting(l)

n = 10 ;
#function to get objects in given interval
def logistics (l,n):
    if n > 0 :
        n -= 1
        request = input('please type request : ')
        request = request.split()
        request = [int(request[i]) for i in range(len(request))]
        #upperbound lowerbound 
        result = [i for i in l if request[0] <= i <= request[1]]
        print(len(result))
        return logistics(l,n)
    else : 
        return 
logistics(l,n)