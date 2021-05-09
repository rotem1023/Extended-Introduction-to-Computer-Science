#Skeleton file for HW5 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to include your ID number (hw5_ID.py).


############
# QUESTION 1
############
class Permutation:
    def __init__(self, perm):
        lst=[0 for i in range(len(perm))]
        legal=True
        for j in range(len(perm)):
            if perm[j]>=len(perm):
                legal=False
                break
            if lst[perm[j]]==0:
                lst[perm[j]]=1
            else:
                legal=False
                break
        if legal:
            self.perm=perm
        else:
            self.perm= None
    
    def __getitem__(self,i):
        return(self.perm[i])

    def compose (self, other):
        final=[]
        for i in range(len(other.perm)):
           d=other.perm[i]
           final.append(self.perm[d])
        r=Permutation(final)
        return (r)
        
    def inv (self):
        lst=[None for i in range(len(self.perm))]
        for i in range(len(self.perm)):
            tmp=self.perm[i]
            lst[tmp]=i
        final=Permutation(lst)
        return (final)
    
    def __eq__(self, other):
        return self.perm == other.perm

    def __ne__(self, other):
        return self.perm != other.perm
                    
    def order(self):
        cnt=1
        check=[i for i in range(len(self.perm))]
        new=self               
        while new.perm != check:
            new=new.compose(self)
            cnt+=1
        return (cnt)


#This function is not part of the class Permutation
def compose_list(lst):
    if len(lst)==1:
        return(lst[0])
    if len(lst)==0:
        return (None)
    else:
        n=len(lst)
        new_p=lst[n-2].compose(lst[n-1])
        lst.pop()
        lst.pop()
        lst.append(new_p)
        return(compose_list(lst))  
        



############
# QUESTION 2
############

def printree(t, bykey = True):
        """Print a textual representation of t
        bykey=True: show keys instead of values"""
        #for row in trepr(t, bykey):
        #        print(row)
        return trepr(t, bykey)

def trepr(t, bykey = False):
        """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
        if t==None:
                return ["#"]

        thistr = str(t.key) if bykey else str(t.val)

        return conc(trepr(t.left,bykey), thistr, trepr(t.right,bykey))

def conc(left,root,right):
        """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""
        
        lwid = len(left[-1])
        rwid = len(right[-1])
        rootwid = len(root)
        
        result = [(lwid+1)*" " + root + (rwid+1)*" "]
        
        ls = leftspace(left[0])
        rs = rightspace(right[0])
        result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid*" " + "|" + rs*"_" + (rwid-rs)*" ")
        
        for i in range(max(len(left),len(right))):
                row = ""
                if i<len(left):
                        row += left[i]
                else:
                        row += lwid*" "

                row += (rootwid+2)*" "
                
                if i<len(right):
                        row += right[i]
                else:
                        row += rwid*" "
                        
                result.append(row)
                
        return result

def leftspace(row):
        """helper for conc"""
        #row is the first row of a left node
        #returns the index of where the second whitespace starts
        i = len(row)-1
        while row[i]==" ":
                i-=1
        return i+1

def rightspace(row):
        """helper for conc"""
        #row is the first row of a right node
        #returns the index of where the first whitespace ends
        i = 0
        while row[i]==" ":
                i+=1
        return i






class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"
    
    
    
class Binary_search_tree():

    def __init__(self):
        self.root = None


    def __repr__(self): #no need to understand the implementation of this one
        out = ""
        for row in printree(self.root): #need printree.py file
            out = out + row + "\n"
        return out

    
    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)


    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val     # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else: #key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return
        
        if self.root == None: #empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)


    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node


    def depth(self):
        ''' return depth of tree, uses recursion'''
        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)


    def size(self):
        ''' return number of nodes in tree, uses recursion '''
        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)

    def max_sum(self):
        if self.root== None:
            return (0)
        def max_sum_rec(node): 
            if (node.right==None) and (node.left== None):
                return (node.val)
            elif (node.right==None):
                return (node.val+max_sum_rec(node.left))
            elif (node.left== None):
                return (node.val+max_sum_rec(node.right))
            else:
                one=node.val+max_sum_rec(node.right)
                two=node.val+max_sum_rec(node.left)
                return (max(one,two))
        return max_sum_rec(self.root)

    def is_balanced(self):
        if self.root== None:
            return (True)
        n=self.depth()
        def long_tree(self, n):
            if (self.right==None) and (self.left== None):
                return (0)
            elif self.right==None:
                if (self.left.right== None) and (self.left.left== None) :
                    return(1)
                else:
                    return (2*n+5)
            elif self.left==None:
                if (self.right.right== None) and (self.right.left== None) :
                    return(1)
                else:
                    return (2*n+5)
            else:
                one=1+(long_tree(self.left,n))  
                two=1+(long_tree(self.right,n))
                if one-two>=-1 and one-two<=1:
                    return (max(one,two))
                else:
                    return (2*n+5)
        final=long_tree(self.root,n)
        if final==n:
            return (True)
        else:
            return (False)

    def diam(self):
        set1=set()
        if self.root==None:
            return (0)            
        def start(node,set1):
            if node==None:
                set1.add(0)
                return (0)
            if node.right==None and node.left==None:
                set1.add(1)
                return(1)
            else:
                right=start(node.right,set1)
                left=start(node.left,set1)
                set1.add(right+1)
                set1.add(left+1)
                if node.right!=None and node.left!=None:
                    set1.add(left+right+1)
                return (max(right,left)+1)
        t=start(self.root,set1)
        return (max(set1))


############
# QUESTION 3
############
def same_tree(lst1, lst2):
    if len(lst1)==0:
        return (True)
    t1=  Binary_search_tree()
    t2= Binary_search_tree()
    for i in lst1:
        t1.insert(i,i)
    for j in (lst2):
        t2.insert(j,j)
    def same_tree_rec(node1, node2):
        if (node1.left==None) and (node1.right==None):
            if (node2.left!= None) or (node2.right !=None):
                return (False)
            if node1.key != node2.key:
                return (False)
            return (True)
        elif node2.left==None and node2.right==None:
            if node1.left!= None or node1.right==None:
                return False
            if node1.key != node2.key:
                return (False)
            return (True)
        elif node1.right==None:
            if node2.right != None:
                return False
            if node1.key != node2.key:
                return (False)
            return (same_tree_rec(node1.left, node2.left))
        elif node2.right==None:
            if node1.right != None:
                return False
            if node1.key != node2.key:
                return (False)
            return (same_tree_rec(node1.left, node2.left))
        elif node1.left==None:
            if node2.left != None:
                return False
            if node1.key != node2.key:
                return (False)
            return (same_tree_rec(node1.right, node2.right))
        elif node2.left==None:
            if node1.left != None:
                return False
            if node1.key != node2.key:
                return (False)
            return (same_tree_rec(node1.right, node2.right))
        else:
            if node1.key != node2.key:
                return (False)
            one=same_tree_rec(node1.right, node2.right)
            two=same_tree_rec(node1.left, node2.left)
            if (one==False) or (two== False):
                return (False)
            return (True)
    return (same_tree_rec(t1.root, t2.root))



############
# QUESTION 4
############

class Node():
    
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
        
    def __repr__(self):
        return str(self.value) + "(" + str(id(self))+ ")"
	#This shows pointers as well for educational purposes


class DLList():

    def __init__(self, seq=None):
        self.head = None
        self.tail = None
        self.len = 0
        if seq != None:
            for item in seq:
                self.insert(item)
 
    def __len__(self):
        return self.len
     

    def __repr__(self):
        out = ""
        p = self.head
        while  p != None :
            out += str(p) + ", " # str(p) envokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"
        
            
    def insert(self, val, first = False):
        node1=Node(val)
        if len(self)==0:
            self.head=node1
            self.tail=node1
            node1.prev=None
            node1.next=None

        elif first== False:
            node1.prev=self.tail
            self.tail.next=node1
            self.tail=node1
        else:
            node1.next=self.head
            self.head.prev=node1
            self.head=node1

        self.len+=1
             
    def reverse(self):
        if len(self)==0 or len(self)==1 :
            return (None)
        n=len(self)
        tmp=self.head
        self.head, self.tail= self.tail, self.head
        for i in range(n):
           tmp.next, tmp.prev= tmp.prev, tmp.next
           tmp=tmp.prev 
    
    def rotate(self, k):
        if k==0 or len(self)==0:
            return None
        self.tail.next=self.head
        self.head.prev=self.tail
        if k<len(self)/2:
            for i in range(k):
                self.head=self.head.prev
                self.tail=self.tail.prev
        else:
            for i in range(len(self)-k):
                self.head=self.head.next
                self.tail=self.tail.next
        self.head.prev=None
        self.tail.next=None

    def delete_node(self, node):
        n=len(self)
        self.len-=1
        if n==1:
            self.head=None
            self.tail=None
            return None
        if self.head==node:
            tmp=self.head.next
            self.head.next=None
            self.head=tmp
            self.head.prev=None
            return None
        elif self.tail==node:
            tmp=self.tail.prev
            self.tail.prev=None
            self.tail=tmp 
            self.tail.next=None
            return None

        else:
            p=node
            one=p.next
            two=p.prev
            one.prev=two
            two.next=one
            p.next=None
            p.prev=None


############
# QUESTION 6
############
# a
def prefix_suffix_overlap(lst, k):
    n=len(lst)
    final=[]
    for i in range(n):
        compare=lst[i][0:k]
        for j in range(n):
            if j!=i:
                length=len(lst[j])
                check=lst[j][length-k:]
                if compare==check:
                    final.append((i,j))
    return (final)

# c
#########################################
### Dict class ###
#########################################

class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [ [] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])
              
    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key) #hash on key only
        item = [key, value]    #pack into one item
        self.table[i].append(item) 

    def find(self, key):
        i=self.hash_mod(key)
        final=[]
        for l in self.table[i]:
            if l[0]==key:
                final.append(l[1])
        return(final)


#########################################
### End Dict class ###
#########################################    

# d
def prefix_suffix_overlap_hash1(lst, k):
    m=len(lst)
    dic=Dict(m)
    for i in range(m):
        dic.insert(lst[i][:k],i)
    final=[]
    for j in range(m):
        last=lst[j][-k:]
        match=dic.find(last)
        for d in match:
            if d !=j:
                final.append((d,j))
    return(final)


# f
def prefix_suffix_overlap_hash2(lst, k):
    final=[]
    m=len(lst)
    dic=dict()
    for i in range(m):
        start=lst[i][:k]
        list1=[]
        if start not in dic:
            list1.append(i)
            dic[start]=list1
        else:
            dic[start].append(i)
    for end in range(m):
        last=lst[end][-k:]
        if dic.get(last) != None:
            match=dic[last]
            for num in match:
                if num!= end:
                    final.append((num,end))
    return (final)






   
    
########
# Tester
########

def test():
    #Testing Q1
    #Question 1
    p = Permutation([2,3,1,0])
    if p.perm != [2,3,1,0]:
        print("error in Permutation.__init__")
    q = Permutation([1,0,2,4])
    if q.perm != None:
        print("error in Permutation.__init__")
    if p[0] != 2 or p[3] != 0:
        print("error in Permutation.__getitem__")
        
    p = Permutation([1,0,2])
    q = Permutation([0,2,1])
    r = p.compose(q)
    if r.perm != [1,2,0]:
        print("error in Permutation.compose")

    p = Permutation([1,2,0])
    invp = p.inv()
    if invp.perm != [2,0,1]:
        print("error in Permutation.inv")
    
    p1 = Permutation([1,0,2,3])
    p2 = Permutation([2,3,1,0])
    p3 = Permutation([3,2,1,0])
    lst = [p1,p2,p3]
    q = compose_list(lst)
    if q.perm != [1,0,3,2]:
        print("error in compose_list")

    identity = Permutation([0,1,2,3])
    if identity.order() != 1:
        print("error in Permutation.order")
    p = Permutation([0,2,1])
    if p.order() != 2:
        print("error in Permutation.order")
    

    #Testing Q2
    #Question 2
    t = Binary_search_tree()
    if t.max_sum() != 0:
        print("error in Binary_search_tree.max_sum")        
    t.insert('e', 1)
    t.insert('b', 2)
    if t.max_sum() != 3:
        print("error in Binary_search_tree.max_sum")        
    t.insert('a', 8)
    t.insert('d', 4)
    t.insert('c', 10)
    t.insert('i', 3)
    t.insert('g', 5)
    t.insert('f', 7)
    t.insert('h', 9)
    t.insert('j', 6)
    t.insert('k', 5)
    if (t.max_sum() != 18):
        print("error in Binary_search_tree.max_sum")


    t = Binary_search_tree()
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("b", 10) 
    t.insert("d", 10) 
    t.insert("a", 10) 
    t.insert("c", 10) 
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("e", 10) 
    t.insert("f", 10)
    if t.is_balanced() != False:
        print("error in Binary_search_tree.is_balanced")

                
    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("error in Binary_search_tree.diam") 

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("error in Binary_search_tree.diam")



    #Testing Q3
    lst = DLList("abc")
    a = lst.head
    if a == None or a.next == None or a.next.next  == None:
        print("error in DLList.insert")
    else:
        b = lst.head.next
        c = lst.tail
        if lst.tail.prev != b or b.prev != a or a.prev != None:
            print("error in DLList.insert")

    lst.insert("d", True)
    if len(lst) != 4 or lst.head.value != "d":
        print("error in DLList.insert")

    prev_head_id = id(lst.head)
    lst.reverse()
    if id(lst.tail) !=  prev_head_id  or lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.value != "d":
        print("error in DLList.reverse")

    lst.rotate(1)
    if lst.head.value != "d" or lst.head.next.value != "c" or lst.tail.value != "a":
        print("error in DLList.rotate")
    lst.rotate(3)
    if lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.prev.value != "a":
        print("error in DLList.rotate")

    lst.delete_node(lst.head.next)    
    if lst.head.next != lst.tail.prev or len(lst)!= 3:
        print("error in DLList.delete_node")
    lst.delete_node(lst.tail)
    if lst.head.next != lst.tail or len(lst) != 2:
        print("error in DLList.delete_node")


        
    #Question 5
    s0 = "a"*100
    s1 = "b"*40 + "a"*60
    s2 = "c"*50+"b"*40+"a"*10
    lst = [s0,s1,s2]
    k=50
    if prefix_suffix_overlap(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap")
    if prefix_suffix_overlap_hash1(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap_hash1(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash1")
    if prefix_suffix_overlap_hash2(lst, k) != [(0, 1), (1, 2)] and \
       prefix_suffix_overlap_hash2(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash2")

def tree_keys_gen(tree):
    return tree_keys_gen_rec(tree.root)
def tree_keys_gen_rec(node):
    if node == None:
         return
    left_gen = tree_keys_gen_rec(node.left)
    for x in left_gen:
        yield(x)
    yield (node.key)
    right_gen = tree_keys_gen_rec(node.right)
    for y in right_gen:
        yield(y)

t = Binary_search_tree()
keys_to_insert = [40, 12, 60, 1, 31, 50, 70]
for key in keys_to_insert:
    t.insert(key, 'a') #all values are 'a'
gen = tree_keys_gen(t)

print([k for k in gen])



def mirror(T):
    def mirror_rec(node):
        if node.left==None and node.right==None:
            return node
        node.left,node.right=mirror_rec(node.right),mirror_rec(node.left)
        return(node)
    return(mirror_rec(T.root))

















 
