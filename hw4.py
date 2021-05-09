#Skeleton file for HW4 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to include your ID number (hw4_ID.py).


############
# QUESTION 2
############


# a
def win (n,m):
    if n==1 and m==1:
        return (False)
    if n==1 and m>1:
        return (True)
    if m==1 and n>1:
        return(True)
    for i in range(2,n+1):
        new_win=win(i-1,m)
        if new_win==False:
            return (True)
    for j in range(2,m+1):
        new_win=win(n,j-1)
        if new_win==False:
            return (True)
    return (False)


# c
def win_mem (n,m,mem):
    if n==1 and m>1:
        mem[(n,m)]=True
        return(mem[(n,m)])
    if m==1 and n>1:
        mem[(n,m)]=True
        return(mem[(n,m)])
    if (n,m) not in mem:
        for i in range(2,n+1):
            new_win=win_mem (i-1,m,mem)
            if new_win==False:
                mem[n,m]=True
                return(mem[n,m])
        for j in range(2,m+1):
            new_win=win_mem(n,j-1,mem)
            if new_win==False:
                mem[n,m]=True
                return(mem[n,m])
        mem[n,m]=False
    return(mem[n,m])
           
def win_fast(n,m):
    mem={(1,1):False}
    final=win_mem(n,m,mem)
    return(mem[n,m])


############
# QUESTION 3
############

# b
def had_local(n, i, j):
    if n==0:
        return(0)
    else:
        if i>=2**(n-1) and j>=2**(n-1):
            return (1-had_local(n-1, i-2**(n-1), j-2**(n-1)))
        elif i>=2**(n-1):
            return (had_local(n-1, i-2**(n-1), j))
        elif j>=2**(n-1):
            return(had_local(n-1, i, j-2**(n-1)))   
        else:
            return(had_local(n-1, i, j))

# d
had_complete = lambda n : [[had_local(n,i,j) for j in range(2**n)]for i in range (2**n)]



############
# QUESTION 4
############

def subset_sum_count(L, s):
    if s == 0 and L==[]:
        return (1)
    if L == []:
        return (0)
    
    with_first = subset_sum_count(L[1:], s - L[0])
    without_first = subset_sum_count(L[1:], s)
    return with_first + without_first


def making_sure (final):
    for i in range(len(final)):
        set1=set()
        if i<len(final):
            for num in final[i]:
                set1.add(num)
        j=i+1
        while j <len(final):
            set2=set()
            if j<len(final):
                for num1 in final[j]:
                    set2.add(num1)
            if set1==set2:
                final.remove(final[j])
            else:
                j+=1
    return(final)

def subset_sum_search_all(L, s):
    lst=[]
    orginal_lst=[]
    if L==[] and s!=0:
        return([])
    final1=subset_sum_search(orginal_lst,L,lst,s)
    final=[]
    for j in final1:
        if j not in final:
            final.append(j)
    final= making_sure (final)
    return (final)


def subset_sum_search(orginal_lst,L,lst,s):   
    if s==0 and  L==[]:
        value=[]
        for i in orginal_lst:
            value.append(i)
        return ([value])
    if L==[]:
        return (None)
    first=L[0]
    orginal_lst.append(first)
    with_first = subset_sum_search(orginal_lst,L[1:],lst,s-L[0])
    orginal_lst.pop()
    without_first = subset_sum_search(orginal_lst,L[1:],lst,s)
    if (with_first!= None) and (with_first not in lst):
        lst.extend(with_first)
        if len(lst)>0:
            lst=making_sure (lst)
    if (without_first!= None) and (without_first not in lst):
        lst.extend(without_first)
        if len(lst)>0:
            lst=making_sure (lst)
    return (lst) 


############
# QUESTION 6
############

def distance(s1, s2):
    if s1==s2:
        return(0)
    elif len(s1)==0:
        return (len(s2))
    elif len(s2)==0:
        return(len(s1))
    else:
        if  s1[0]==s2[0]:
            return(distance(s1[1:],s2[1:]))
        else:
            first=1+distance(s1[1:],s2[1:])
            second=1+distance(s1[1:],s2) 
            third=1+distance(s1,s2[1:])
        if first>0 and second>0 and third>0:
            return(min(first,second,third))
        else:
            lst=[]
            if first!= 0:
                lst.append(first)
            if second != 0:
                lst.append(second)
            if third!= 0:
                lst.append(third)
            return (min(lst))



def distance_fast(s1, s2,):
    mem={}
    mem[('','')]=0
    l=0
    r=0
    if s1==s2:
        mem[(s1,s2,l,r)]=0
        return (mem[(s1,s2,l,r)])
    elif len(s1)==0:
        mem[(s1,s2,l,r)]=len(s2)
        return( mem[(s1,s2,l,r)])
    elif len(s2)==0:
        mem[(s1,s2,l,r)]=len(s1)
        return( mem[(s1,s2,l,r)])
    return (distance_mem(s1, s2,mem,l,r))
   

def distance_mem(s1, s2,mem,l,r):
    if (s1, s2, l,r) in mem:
        return (mem[(s1, s2, l,r)])
    elif (len(s1)==l+1) and len(s2)==r+1: 
        if s1[l]==s2[r]:
            mem[(s1,s2,l,r)]=0
            return( mem[(s1,s2,l,r)]) 
        else:
            mem[(s1,s2,l,r)]=1
            return( mem[(s1,s2,l,r)])
    elif len(s1)==l+1:
        if s1[l]not in s2[r:]:
            mem[(s1,s2,l,r)]=len(s2)-(r)
            return( mem[(s1,s2,l,r)])
        else:
            mem[(s1,s2,l,r)]=len(s2)-(r+1)
            return( mem[(s1,s2,l,r)])
    elif len(s2)==r+1:
        if s2[r] not in s1[l:]:
            mem[(s1,s2,l,r)]=len(s1)-(l)
            return( mem[(s1,s2,l,r)])
        else:
            mem[(s1,s2,l,r)]=len(s1)-(l+1)
            return( mem[(s1,s2,l,r)])
    else:
        if  s1[l]==s2[r]:
            mem[(s1,s2,l,r)]=distance_mem(s1,s2,mem, l+1, r+1)
            return(mem[(s1,s2,l,r)])
        else:
            first=distance_mem(s1,s2, mem, l+1, r+1)+1
            second=1+distance_mem(s1,s2,mem, l+1,r)
            third=1+distance_mem(s1,s2,mem, l, r+1)
            final=min(first,second,third)
            mem[(s1,s2,l,r)]=final
            return(mem[(s1,s2,l,r)])
    return (mem[(s1,s2,l,r)])

########
# Tester
########

def test():
    if win(3,3) != False or\
       win(3,4) != True or\
       win(1,1) != False or\
       win(1,2) != True :
        print("Error in win()")

    if win_fast(3,3) != False or \
       win_fast(3,4) != True or\
       win_fast(1,1) != False or\
       win_fast(1,2) != True :
        print("Error in win_fast()")

    contains = lambda L, R : all(R.count(r) <= L.count(r) for r in R)
    L = [1, 2, 4, 8, 16]

    if subset_sum_count(L, 13) != 1 or subset_sum_count(L, 32) != 0 \
       or subset_sum_count([i for i in range(1, 10)], 7) != 5:
        print("Error in subset_sum_count")

    R_lst = subset_sum_search_all(L, 13)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 1:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 13 or not contains(L,R):
                print("Error in subset_sum_search_all")

    R_lst = subset_sum_search_all(L, 32)
    if not R_lst == []:
        print("Error in subset_sum_search_all")

    L = [i for i in range(1, 10)]
    R_lst = subset_sum_search_all(L, 7)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 5:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 7 or not contains(L,R):
                print("Error in subset_sum_search_all")

    if distance('computer','commuter') != 1 or \
       distance('sport','sort') != 1 or \
       distance('','ab') != 2 or distance('kitten','sitting') != 3:
        print("Error in distance")

    if distance_fast('computer','commuter') != 1 or \
       distance_fast('sport','sort') != 1 or \
       distance_fast('','ab') != 2 or distance_fast('kitten','sitting') != 3:
        print("Error in distance_fast")

    
















