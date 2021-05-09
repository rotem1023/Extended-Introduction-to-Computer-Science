
#Skeleton file for HW1 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw1_ID.py).

from primes_lst import *  #loading the list of primes into a variable named primes


#Question 3
def max_word_len(filename):
    inFile = open(filename, "r")
    outFile = open("output.txt", "w")
    for i in inFile:
        lst1=i.split()
        lst2=[]
        for t in lst1:
            k=len(t)
            list.append(lst2,k)
            lst2.sort()
        if len(lst2)==0:
            r=0
            r=str (r)
        else:
            r=str(lst2[-1])
        outFile.write(r+"\n")
        
    inFile.close()
    outFile.close()                          
    
    




#**************************************************************
#Question 5
def k_boom(start, end, k):
    t1=str(k)
    str1= ""
    for i in range(start,end+1):
        t=str(i).count(t1)
        if t>0 and i%k==0:               #check if the number has k digit and division by k
             str1+="bada-boom! " 
        elif t>0 and (i%k!=0):             #check if the number has k digit and not division by k
            str1+="boom-"*(t-1)+"boom!"+" "   
        elif t==0 and i%k==0:               # check if the number division by k and has no k digit
            str1+="boom! "
        else:                               # if the number has no k digit and not division by k
            str1+= str(i)+" "
    r=len(str1)
    str2=""
    d=1
    while d<r:                          # to prevent the space bar in the end
        str2+=str1[d-1]
        d=d+1
    return(str2)






#**************************************************************
#Question 6

# 6a
def check_goldbach_for_num(n, primes_lst):          # it runs on all of the numbers in the prime list without order and checks if n equal to the sum
    for i in primes_lst:
        for j in primes_lst:
            if (j+i)==n:
                return (True)
    return (False)
    

# 6b
def check_goldbach_for_range(limit, primes_lst):        # it takes any 2 numbers from the prime lisit and checks if its equal to the numbers in the range of the limit
    set1=set(range(4,limit,2))
    set2=set()
    
    for i in primes_lst:
        for j in primes_lst:
            if (i+j) in set1:
                set2.add(i+j)
    if set1==set2:
        return (True)
    else:
        return(False)


# 6c
def check_goldbach_for_num_stats(n, primes_lst):
    k=len(primes_lst)
    t=0
    j=0
    r=1
    d=0
    for i in primes_lst:
        while j<k:
            d=int(i)+int(primes_lst[j])
            if d==n:
                t=t+1
            j=j+1
        j=r
        r=r+1
    return(t)





########
# Tester
########

def test():
    #testing Q5
    s = k_boom(797, 802, 7)
    if s != 'boom-boom! bada-boom! boom! 800 801 802':
        print("error in k_boom()")

    

    #testing Q6
    if not check_goldbach_for_num(10, [2, 3, 5, 7]):
        print("error in check_goldbach_for_num()")

    if check_goldbach_for_num(10, [2, 3]):
        print("error in check_goldbach_for_num()")

    if not check_goldbach_for_range(20, [2, 3, 5, 7, 11]):
        print("error in check_goldbach_for_range()")

    if check_goldbach_for_range(21, [2, 3, 5, 7, 11]):
        print("error in check_goldbach_for_range()")
        
    if check_goldbach_for_num_stats(20, primes) != 2:
        print("error in check_goldbach_for_num_stats()")

    if check_goldbach_for_num_stats(10, primes) != 2:
        print("error in check_goldbach_for_num_stats()")







print(k_boom(2,700,4))
