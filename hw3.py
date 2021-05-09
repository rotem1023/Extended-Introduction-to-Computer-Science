# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random


############
# QUESTION 2
############

def cycle(n):
    lst=[]
    for j in range (n):
        lst1=[0 for i in range (n)]
        lst.append(lst1)
    for i in range(n):
        nh1=(i+1)%(n)
        nh2=(i-1)%(n)
        lst[i][nh1]=1
        lst[i][nh2]=1
    return(lst)


def complete_graph(n):
    lst=[]
    for j in range (n):
        lst1=[1 for i in range (n)]
        lst.append(lst1)
    return(lst)

def random_graph(n, p):
    lst=[]
    for j in range (n):
        lst1=[0 for i in range (n)]
        lst.append(lst1)
    for row in range (n):
        for col in range(n): 
            num=random.random()
            if num<=p:
                lst[row][col]=1
    return(lst)

def inv_cycle(n):
    lst = cycle(n)
    for i in range (1,n):
        j=(i**(n-2))%n
        lst[i][j]=1
    lst[0][0]=1
    return(lst)

def return_graph(n):
    lst=[]
    for j in range (n):
        lst1=[0 for i in range (n)]
        lst.append(lst1)
    for i in range(1,n):
        lst[i-1][i]=1
        lst[i][0]=1
    return(lst)

def random_step(adj, v):
    lst=adj[v]
    i=0
    lst1=[]
    while i<len(lst):
        if lst[i]==1:
           lst1.append(i)
        i+=1
    num=random.choice(lst1)
    return(num)

def walk_histogram(adj):
    n=len(adj)
    lst=[0 for i in range (n)]
    lst[0]=1
    log= False
    v=0
    lst[v]=lst[v]+1
    while log==False:
        lst1=[i for i in range(n)if adj[v][i]==1]
        u=random.choice(lst1)
        lst[u]=lst[u]+1
        v=u
        log= True
        for i in range(len(lst)):
            if lst[i]==0:
                log=False
                break
    return(lst)
print(walk_histogram([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [1, 0, 0,0,0]]))

print(walk_histogram([[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [1, 0, 0,0, 0]]))
def cover_time(adj):
    return(sum(walk_histogram(adj)))
print(cover_time([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [1, 0, 0,0,0]]))
############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):
    if len(lst)%k==0:
        length=(len(lst))//k
    else:
        length=(len(lst)//k)+1    #to choose the size of the small lists
    i=0
    lst2=[]
    while i <length:        
        lst1=lst[k*i:k*i+k]     # making a small list in the size of k
        selection_sort(lst1)
        lst2.append(lst1)       # adding the small list to a new list
        i+=1
    return(lst2)


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    if len(lst)==1:
        return(lst[0])
    elif len(lst)==2:
        return(merge(lst[0], lst[1]))
    else:
        mid=len(lst)//2
        return (merge(merge_sorted_blocks(lst[:mid]),(merge_sorted_blocks(lst[mid:]))))


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find_missing(lst, n):
    l=0
    r=len(lst)-1
    if len(lst)==0:
        return(0)
    if lst[r]<n:
        return(n)
    if lst[0]!=0:
        return(0)
    while r-l>1:
        mid=(r+l)//2
        if mid==lst[mid]:
            l=mid
            
        elif mid<lst[mid]:
            r=mid
            
    return(r)

def binary_search(lst,l,r, key):
    """ iterative binary search
        lst better be sorted for binary search to work """
    n = len(lst)
    left = l
    right = r

    while left <= right:
        middle = (right+left)//2 # middle rounded dow
        if key == lst[middle]:   # item found
            return middle
        elif key < lst[middle]:  # item cannot be in top half
            right = middle-1
        else:                    # item cannot be in bottom half
            left = middle+1           
    #print(key, "not found")
    return None

def find(lst, s):
    if len(lst)==0:
        return(None)
    r=len(lst)-1
    l=0
    if lst[l]<lst[r]:
        return(binary_search(lst,0,r, s))
    while lst[l]>lst[r]:    # finding where the rotate happend
        mid=(r+l)//2
        if lst[mid]==s:
            return(mid)
        elif lst[mid]>lst[l]:
            l=mid
        else:
            r=mid
    if s<lst[0]:                # decide in which part of the list to do bunary search
        return(binary_search(lst,l+1,len(lst)-1, s))
    else:
         return(binary_search(lst,0,l+1, s))


def find2(lst, s):
    i=0
    while i < len(lst):
        if lst[i]==s:
            return (i)
        i+=1
    return (None)


############
# QUESTION 5
############

# a
def string_to_int (s):
    k=len(s)
    s1=s[::-1]
    num=0
    dic = {'a':0,'b':1,'c':2,'d':3,'e':4}
    for i in range (0,k):
        t=s1[i]
        num=num+(dic[t]*(5**(i)))
    return(num)

# b
def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    str1=''
    for i in range (k):
        if n%5==0:
            str1=str1+'a'
            n=n//5
        elif n%5==1:
            str1=str1+'b'
            n=n//5
        elif n%5==2:
            str1=str1+'c'
            n=n//5
        elif n%5==3:
            str1=str1+'d'
            n=n//5
        else:
            str1=str1+'e'
            n=n//5
    return(str1[::-1])

# c
def sort_strings1(lst, k):
    lst1=[]
    help_lst=[0 for i in range(5**k)]
    for i in lst:
        cnt= string_to_int (i)
        help_lst[cnt]=1+help_lst[cnt]
    j=0
    while j  <len(help_lst):
        if help_lst[j]>0:
            lst1.append(int_to_string(k, j))
            help_lst[j]=help_lst[j]-1
        else:
            j+=1
    return(lst1)


# e
def sort_strings2(lst, k):
    lst1=[]
    for i in range (5**k):  #making the help list        
        
        for st in lst:      #checking if the sring in thr list
            t=int_to_string(k, i)
            if t==st:
                lst1.append(t)
    return(lst1)
            


########
# Tester
########

def test():
    # q2
    if complete_graph(4) != \
           [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]:
        print("error in complete_graph")

    if cycle(5) != \
           [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]:
        print("error in cycle")

    if sum(sum(random_graph(100, 0.8)[i]) for i in range(100)) < 200:
        print("error in random_graph")

    if inv_cycle(13) != \
       [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], \
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], \
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], \
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]:
        print("error in inv_cycle")

    if return_graph(5) != \
       [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], \
        [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0]]:
        print("error in return_graph")

    A = random_graph(100, 0.9)
    for _ in range(10):
        v = random.randint(0, 99)
        u = random_step(A, v)
        if not A[v][u]:
            print("error in random_step")

    if 0 in walk_histogram(inv_cycle(13)) or \
       0 in walk_histogram(cycle(10)):
        print("error in walk_histogram")

    
    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    missing = find_missing([0,1,2,3,5], 5)
    if missing != 4:
        print("error in find_missing")

    pos = find([30, 40, 50, 60, 10, 20], 60)
    if pos != 3:
        print("error in find")

    pos = find([30, 40, 50, 60, 10, 20], 0)
    if pos != None:
        print("error in find")

    pos = find2([30, 40, 50, 60, 60, 20], 60)
    if pos != 3 and pos != 4:
        print("error in find2")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")


print(walk_histogram([]))



