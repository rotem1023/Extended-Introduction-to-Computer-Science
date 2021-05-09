# Skeleton file for HW6 - Spring 2019/20 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).



############
# QUESTION 1
############

class ImprovedGenerator:
    def __init__(self, g):
        self.val=g   
        try:
            self.gen=next(self.val)
        except StopIteration:
            self.gen= StopIteration
        try:
            self.gen_next=next(self.val)
        except StopIteration:
            self.gen_next=StopIteration
        

    def has_next(self):
        if self.gen== StopIteration:
            return (False)
        else:
            return (True)

    def peek(self):
        return (self.gen)

    def __iter__(self):
        return self
        # yield next(self)

    def __next__(self):
        if isinstance (self.val, tuple):
            final=(next(self.val[0]),next(self.val[1]))
            self.gen=(self.val[0].gen,self.val[1].gen)
            self.gen_next=(self.val[0].gen_next,self.val[1].gen_next)
            return(final)
        if self.gen!= StopIteration:
            final=self.gen
            self.gen=self.gen_next
            try:
                self.gen_next=next(self.val)
            except StopIteration:
                self.gen_next=StopIteration
            return(final)
        else: 
            raise (StopIteration)

    def product(self, other):
        l=[0]
        l1=iter(l)
        z=ImprovedGenerator(l1)
        z.val=(self, other)
        z.gen=(self.gen, other.gen)
        z.gen_next=(self.gen_next, other.gen_next)
        return (z)


############
# QUESTION 3
############
def maxmatch(T, p, triple_dict, w=2**12-1, max_length=2**5-1):
    """ finds a maximum match of length k<=2**5-1 in a w long window, T[p:p+k] with T[p-m:p-m+k].
        Returns m (offset) and k (match length) """

    assert isinstance(T,str)
    n = len(T)
    maxmatch = 0
    offset = 0
    if p + 3 > len(T) or T[p:p+3] not in triple_dict:
        return offset, maxmatch
    lst=triple_dict[T[p:p+3]]
    for i in lst:
        k=3
        m=abs(i-p)
        if i<p and (p-i)<w:
            while k< min(n-p, max_length) and T[p-m+k]==T[p+k]:
                k+=1
            if k > maxmatch:
                maxmatch=k
                offset=m       
    return offset, maxmatch


def LZW_compress(text, w=2**12-1, max_length=2**5-1):
    """LZW compression of an ascii text. Produces a list comprising of either ascii characters
       or pairs [m,k] where m is an offset and k>=3 is a match (both are non negative integers) """
    result = []
    n = len(text)
    p = 0
    triple_dict = {}

    while p<n:
        m,k = maxmatch(text, p, triple_dict, w, max_length)
        if p+3<n:
            add_triple_to_dict(text, p, triple_dict)
        if k<3:
            result.append(text[p]) #  a single char
            p+=1
        else:
            result.append([m,k])   # two or more chars in match
            for i in range(k):
               add_triple_to_dict(text, p+i, triple_dict) 
            p+=k            
    return result  # produces a list composed of chars and pairs

def add_triple_to_dict(text, p, triple_dict):
    """ Adds to the dictionary mapping from a key T[p:p+2] to a new
        integer in a list p."""
    if p+3 > len(text): return
    triple = text[p:p+3]
    if triple in triple_dict:
        triple_dict[triple].append(p)
    else:
        triple_dict[triple] = [p]




############
# QUESTION 6
############

###### CODE FROM LECTURE - DO NOT CHANGE ######
def fingerprint(text, basis=2 ** 16, r=2 ** 32 - 3):
    """ used to compute karp-rabin fingerprint of the pattern
        employs Horner method (modulo r) """
    partial_sum = 0
    for ch in text:
        partial_sum = (partial_sum * basis + ord(ch)) % r
    return partial_sum


def text_fingerprint(text, m, basis=2 ** 16, r=2 ** 32 - 3):
    """ computes karp-rabin fingerprint of the text """
    f = []
    b_power = pow(basis, m - 1, r)
    list.append(f, fingerprint(text[0:m], basis, r))
    # f[0] equals first text fingerprint
    for s in range(1, len(text) - m + 1):
        new_fingerprint = ((f[s - 1] - ord(text[s - 1]) * b_power) * basis + ord(text[s + m - 1])) % r
        # compute f[s], based on f[s-1]
        list.append(f, new_fingerprint)  # append f[s] to existing f
    return f
##############################################


def help_fingerprint(text, m, basis=2 ** 16, r=2 ** 32 - 3):
    """ used to compute karp-rabin fingerprint of the pattern
        employs Horner method (modulo r) """
    partial_sum = 0
    for i in range(m,len(text)):
        partial_sum = (partial_sum * basis + ord(text[i])) % r
    for j in range(m):
        partial_sum = (partial_sum * basis + ord(text[j])) % r
    return partial_sum


def is_rotated_1(s, t, basis=2 ** 16, r=2 ** 32 - 3):
    if len(s) != len (t):
        return (False)
    n=fingerprint(s, basis=2 ** 16, r=2 ** 32 - 3)
    for i in range(len(s)):
        d= help_fingerprint(t,i, basis=2 ** 16, r=2 ** 32 - 3)
        if d==n:
            return (True)
    return (False)


def is_rotated_2(s, t):
    if len(s)!=len(t):
        reurn (False)
    if s==t:
        return (True)
    n=len(s)
    for i in range(1,len(s)):
        lst=text_fingerprint(s,i, basis=2 ** 16, r=2 ** 32 - 3)
        k=fingerprint(t[:i], basis=2 ** 16, r=2 ** 32 - 3)
        if k==lst[-1]:
            if fingerprint(t[i:], basis=2 ** 16, r=2 ** 32 - 3)==fingerprint(s[:n-i], basis=2 ** 16, r=2 ** 32 - 3):
                return (True)
    return (False)


############
# QUESTION 7
############

from matrix import Matrix

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


# (1)
def had(n):
    mat = Matrix(pow(2,n), pow(2,n))
    mat1=Matrix (1,1)
    for i in range(2**n):
        for j in range(2**n):
           t=had_local(2**n, i, j)
           if mat.rows[i][j]!=t:
               mat.rows[i][j]=t
##    one=had_complete(2**n)
##    for i in range(2**n):
##        mat.rows[i]=one[i]
    return mat


# (2)
def disj(n):
    mat = Matrix(pow(2,n), pow(2,n))
    """
         fill-in your code below here according to the instructions
    """
    return mat

# (3)
def id_image():
    """
         fill-in your code below here according to the instructions
         use Matrix.load() to load the images
    """

########
# Tester
########

def test():
        
    # Question 1

    g = (i for i in range(5))
    g2 = ImprovedGenerator(g)
    for i in range(5):
        if g2.peek() != i:
            print("error in peek")

        if next(g2) != i:
            print("error in next")

        if (i != 4 and (not g2.has_next())) or (i == 4 and g2.has_next()):
            print("error in has_next")

    try:
        next(g2)
        print("should throw stopiteration")
    except StopIteration:
        print("GOOD: raises StopIteration as should")
    except:
        print("not the correct exception")
    g1 = (i for i in range(3))
    g2 = (i for i in range(3))
    g3 = ImprovedGenerator(g1)
    g4 = ImprovedGenerator(g2)
    g5 = g3.product(g4)

    for i in range(3):
        if next(g5) != (i, i):
            print("error in product")

    # Question 3

    # first convert to tuple to make easy comparison
    compressed = tuple([el if isinstance(el, str) else tuple(el) for el in LZW_compress("abcdabc")])
    if compressed != ('a', 'b', 'c', 'd', (4, 3)):
        print("error in LZW_compress")

    # Question 6
    for func in [is_rotated_1, is_rotated_2]:
        if func("amirrub", "rubamir") != True or \
                func("amirrub", "bennych") != False or \
                func("amirrub", "ubamirr") != True:
            print("error in", func.__name__)

    # Question 7

    # (1)
    had1 = Matrix(2, 2)
    had1[1, 1] = 1
    if had(1)!=had1:
        print("error in had")

    # (2)
    disj1 = Matrix(2, 2, 1)
    disj1[1, 1] = 0
    if disj(1) != disj1:
        print("error in disj")
