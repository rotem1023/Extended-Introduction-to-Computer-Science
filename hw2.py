#Skeleton file for HW2 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw2_ID.py).


############
# QUESTION 1
############

# 1a
def sum_divisors(n):
    if n==1:
        return 0
    if n==2:
        return 1
    sqr=int((n**0.5) //1)       #the number of loops
    set1=set()
    for dev in range (2,sqr+1):
        if n%dev==0:            #adding the divided number
            set1.add(dev)
            k= int(n/dev)       #adding the oppsite numbrt that divided n
            set1.add(k)
    return (sum(set1)+1)

# 1b
def legal_par(st):
    length=len(st)
    if length%2>0:
        return (False)
    lst1=[]
    
    for dig in st:      # adding digits to a list (the oppsite direction)
        if dig=='<':
            lst1.append('>')
        elif dig=='(':
            lst1.append(')')
        elif dig=='[':
            lst1.append(']')
        elif dig=='{' :
            lst1.append('}')   
        else:
            i= len(lst1)-1
            if i<0:
                return(False)
            if dig== lst1[i]:
                lst1.pop()
            else:
                return(False)
    if len(lst1) ==0:   # check in the end if its equal to 0
        return (True)
    else:
         return (False)
    


# 1c
def spiral_sum(k):
    sum1=1
    d=1
    for i in range (3,k+1,2):   # counter for the "circels" in the matrix
        t=i-1
        for cnt in range (0,4):     #count the numbers in each circle. 
            sum1= sum1+(d+t)
            d=d+t
    return (sum1)


############
# QUESTION 2
############

# 2b
def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin: 
        if bit=='1':
            result=result*a
        a=a*a
    return result

# 2c
def modpower_new(a, b, c):
    """ computes a**b mod c using iterated squaring
        assumes b is nonnegative integer  """

   

    result = 1 # a**0
    while b > 0:
        if b % 3 == 0:
            result = (result) % c
            a = (a**3) % c
        if b % 3 == 1:
            result = (result*a) % c
            a = (a**3) % c
        if b % 3 == 2:
            result = (result*a*a) % c
            a = (a**3) % c
        b = b // 3
    return result


############
# QUESTION 3
############

# 3a
def inc(binary):
    length= len(binary)
    i=length-1
    st=''
    if binary=='0':     # unusal case
        return ('1')
    elif binary=='1':   # unusal case
        return ('10')
    while i>-1:
        if binary[i]=='0':      # if the first digit is 0 just add 1
            st=binary[0:i]+'1'+st
            return (st) 
        else:                   # if the first digit is 1 switch to 0 and continue
            st='0'+st
            i=i-1
    if len (st)>1 and st[0]=='0':   #if the numbers are all zero's just add 1 in the begginig
        return ('1'+st)

# 3b
def dec(binary):
    dig=len(binary)-1
    st=''
    if binary[dig]=='1':       
        return( binary[:dig]+'0')       # if first digit is 1 just return 0
    else:
        while dig > -1:
            if binary[dig] =='0':       # if the digit is 0 start to build a string of 1's
                st +='1'
                dig=dig-1
            else:                       #if the digit is 1 add 0 to the string nd return mix of the input and string
                st='0'+st
                st= binary[:dig]+st
                break
        if st[0]=='0':                  # i case when the last digit of the number is 0 ' cut it.
            st=st[1:(len(st))]
        return (st)

# 3c
def sub(bin1, bin2):
    bin1=list(bin1[::-1])
    bin2=list(bin2[::-1])
    bin3=list()
    bin4=''
    i=0
    while i <len(bin2):
       if bin2[i]=='0':
           
           bin3.append(bin1[i])
           i+=1
       else:
           if bin1[i]=='1':
               bin3.append('0')
               i+=1
           else:
               bin3.append('1')
               d=i+1
               while bin1[d]=='0':
                   bin1[d]='1'
                   d+=1
               bin1[d]='0'
               i+=1
    if len(bin1)>len(bin3):
        bin3+=bin1[i:]
    for dig in bin3:
        bin4+=dig
    while (len(bin4)>1) and (bin4[-1]=='0'):
        bin4=bin4[:len(bin4)-1]
    return (bin4[::-1])


# 3d
def leq(bin1, bin2):
    if len(bin1)<len(bin2):    # if there are more digits in thr second number return true 
        return (True)
    if len(bin1)>len(bin2):     #the opposite of the upper comment
        return (False)
    if bin2==bin1:
        return (True)       
    while bin2!='0':        # if the by decreasing the we get to bin2 return true
        bin2=dec(bin2)
        if bin2==bin1:
            return (True)
    return(False)  


# 3e
def div(bin1, bin2):
    if bin2=='1' and bin1 !='0':
        return (bin1)
    cnt='0'
    while leq(bin2,bin1)== True: #check if bin1 is bigger than bin 2
        cnt=inc(cnt)
        bin1=sub(bin1, bin2)   
    return(cnt)
        
############
# QUESTION 4
############

# 4a
def has_repeat1(s, k):
    if k==0:
        return (True)
    set1=set()
    dig=0
    while dig< (len(s)-k+1):        
        max1= dig+k
        st=s[dig:max1]       #splits the sting into saller strings at the length of k
        if st in set1:
            return (True)   # if string is already in the set
        else:
            set1.add(st)    #adding strrings that are not in set
        dig+=1
    return (False)

# 4b
def has_repeat2(s, k):
    if k==0:
        return (True)   #unusal case
    dig=0
    while dig< (len(s)-k+1):    #take a tring from the original in the length of k and compare to all the others
        max1= dig+k
        st=s[dig:max1]
        dig2=dig+1
        while dig2< (len(s)-k+1):   #the compare strings
            max2=dig2+k
            if s[dig2:max2]==st:
                return (True)
            dig2+=1
        dig+=1
    return(False)
 
    
############
# QUESTION 5
############

def reading(n):
    num1=str(1)         #R(1)
    for i in range (1,n):
        t=0
        num=''
        cnt=1
        while t<len(num1):
            if (t+1>=len(num1)) or (num1[t]!=num1[t+1]):    #when the digits are changed
                num =num+str(cnt)+ num1[t]
                cnt=1
                t+=1
            elif num1[t]==num1[t+1]:                    #when the digits are the same.
                cnt+=1
                t+=1
        num1=num
    return(num1)

############
# QUESTION 6
############
def max_div_seq(n, k):
    n1=str(n)
    set1=set()
    cnt=0
    i=0
    for i in n1:
        if int(i)% k > 0:   #check if a number in the string divided by k,
            set1.add(cnt)            
            cnt=0               #add the counter to the set
        else:
            cnt+=1              #if the number divided by k, it increase the counter
    set1.add(cnt)               # to prevent a situation that the strike is in the end
    return (max(set1))           

########
# Tester
########

def test():
    if sum_divisors(4) != 3 or \
       sum_divisors(220) != 284:
        print("error in sum_divisors")
        
    if not legal_par("<<>>") or legal_par("<{>}"):
        print("error in legal_par")
    if not legal_par("<<{}<>()[<>]>>") or legal_par("{{{]}}"):
        print("error in legal_par")

    if spiral_sum(3) != 25 or spiral_sum(5) != 101:
        print("error in spiral_sum")
        
    if power_new(2,3) != 8:
        print("error in power_new()")

    if modpower_new(3, 4, 5) != pow(3, 4, 5) or \
       modpower_new(5, 4, 2) != pow(5, 4, 2):
        print("error in modpower_new()")
    
    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc()")

    if dec("1") != "0" or \
       dec("10") != "1" or \
       dec("110") != "101" or \
       dec("1000") != "111" or \
       dec(dec("1001")) != "111":
        print("error in dec()")
        
    if sub("0", "0") != "0" or \
       sub("1000", "0") != "1000" or \
       sub("1000", "1000") != "0" or \
       sub("1000", "1") != "111" or \
       sub("101", "100") != "1":
        print("error in sub()")

    if leq("100","11") or not leq("11", "100"):
        print("error in leq")
    if div("1010","10") != "101" or div("11001", "100") != "110":
        print("error in div")
        
    if not has_repeat1("ababa", 3) or \
       has_repeat1("ababa", 4) or \
       not has_repeat1("aba",1):
        print("error in has_repeat1()")

    if not has_repeat2("ababa", 3) or \
       has_repeat2("ababa", 4) or \
       not has_repeat2("aba",1):
        print("error in has_repeat2()")
                
    if [reading(i) for i in range(1, 6)] != ['1', '11', '21', '1211', '111221']:
        print("error in reading")

    if max_div_seq(23300247524689, 2) != 4:
        print("error in max_div_seq()")
    if max_div_seq(1357, 2) != 0:
        print("error in max_div_seq()")        












 
