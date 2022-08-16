"""
Created on Mon June 6 11:57:21 2022
Excercise for Python 3.9
https://techlent.com/cn/courses/Python39 

There are five groups of excercises:
    1). Python kick-off
    2). List - I
    3). List - II
    4). String 
    5). Dictionary 

@author: jingduhouston

"""
import math

#---------------------------------------------------------------
""" Python Kick-off - Ex. 3 """
def Odd(in_num):
    if in_num % 2 == 0:  # even number (2,4,6)
        return False
    if in_num % 2 == 1: # odd number (1,3,5)
        return True

#---------------------------------------------------------------
""" Python Kick-off - Ex. 4 """
def FizzBuzz(in_num):
    if in_num % 3 == 0 and in_num % 5 == 0:
        return "FizzBuzz"
    elif in_num % 3 == 0:
        return "Fizz"
    elif in_num % 5 == 0:
        return "Buzz"
    else:
        return in_num
"""    
print(FizzBuzz(45))
print(FizzBuzz(9))
print(FizzBuzz(25))
print(FizzBuzz(17))
""" 
#---------------------------------------------------------------
""" Python Kick-off - Ex. 5 """
def sqrt(num):
    sqrt_num = math.sqrt(num)
    if isinstance(sqrt_num, int): # check if it is an integer
        return sqrt_num
    return math.floor(sqrt_num)

#---------------------------------------------------------------
# List I - Ex.1
def LstComp(n1, n2):
    lst = [n1 + i for i in range(n2-n1+1) ]
    return lst
#print(LstComp(1,5))

#---------------------------------------------------------------
# List I - Ex.2
def OddNums(i, j):
    lst = []
    for ind in range (i, j+1):
        if Odd(ind):
            lst.append(ind)
    return lst
        
#---------------------------------------------------------------
# List I - Ex.3
def C2F(lst_c):
    return [c * 1.8 + 32 for c in lst_c]
#print(C2F([0,38]))
    
#---------------------------------------------------------------
# List I - Ex.4
def FibLst(n):
    if n < 1: return -1
    elif n == 1:
        return [0] 
    else:
        lst = [0] * n 
        lst[1] = 1
        for i in range(2, n):
            lst[i] = lst[i-1] + lst[i-2]
        return lst 

"""
#--- test Fiblst()
print(FibLst(1))
print(FibLst(3))
print(FibLst(6))
print(FibLst(-3))
print(FibLst(10))
""" 
#---------------------------------------------------------------
# List I - Ex.5
def RevLst(lst):
    rev_lst = [a for a in reversed(lst)]
    return rev_lst 
#print(RevLst([3, 1, 9, 8, 4]))

#---------------------------------------------------------------
# List I - Ex.6
def IsIn(lst, a):
    return a in lst 
#print(IsIn([1,2,3,4,5], 6))

#---------------------------------------------------------------
# List I - Ex.7
def RmEl(lst, a):
    if a in lst:
        ind = lst.index(a) 
        del lst[ind]
    return lst
#print(RmEl([1, 2, 3, 4, 5], 2))

#---------------------------------------------------------------
# List I - Ex.8
def SepNum(lst):
    oddNum = [] 
    evenNum = [] 
    for a in lst:
        if a % 2 == 0:
            oddNum.append(a) 
        else:
            evenNum.append(a) 
    return oddNum + evenNum 
#print(SepNum([1, 2, 3, 4, 5, 6]))
        
#---------------------------------------------------------------
# List I - Ex.9
def RmDuplicate(lst):
    s = set()
    for a in lst:
        s.add(a)
    return list(s)
"""
print(RmDuplicate([3, 1, 2, 3, 4, 5, 6]))
print(RmDuplicate([1, 3, 5]))
"""

#---------------------------------------------------------------
# List-II Ex.1 (sort a list)
def SortLst(lst):
    lst.sort()
    return lst

#---------------------------------------------------------------
# List-II Ex.2 (insert a number in a sorted list)
def NumInsert(sorted_lst, a):
    sorted_lst.sort()
    for ind in range(0, len(sorted_lst)):
        if sorted_lst[ind] >= a :
            sorted_lst.insert(ind, a)
            return sorted_lst
    sorted_lst.insert(len(sorted_lst), a)
    return sorted_lst

#---------------------------------------------------------------
# List-II Ex.3 (remove duplicates from a sorted list)
from collections import Counter
def SortRm(sorted_lst):
    dic = Counter(sorted_lst)
    return list(dic)
#print(SortRm([1, 2, 2, 3, 4, 4, 5, 6]))

#---------------------------------------------------------------
# List-II Ex. 4 (merge two sorted lists)
def MergeSorted(lst1, lst2):
    lst1.sort()
    lst2.sort()
    for ind in range(0, len(lst2)):
        NumInsert(lst1, lst2[ind])
    return lst1
    
#---------------------------------------------------------------
# List-II Ex. 5 (list to number)
def Lst2Num(lst):
    str_lst = [str(s) for s in lst]
    return int("".join(str_lst))

"""
print(Lst2Num([1, 3, 5]))
print(Lst2Num([0, 1, 2, 0, 3]))
"""

#---------------------------------------------------------------
# List-II Ex.6 (Max stock gain)
def MaxGain(lst):
    """
    Build a function MaxGain to find the maximum you can gain by buying 
    and selling stocks. The strock prices represented as a list of numbers.
    You need to buy stocks before you sell them.
    """
    max_gain = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)-1):
            max_gain = max((lst[j] - lst[i]), max_gain)
    return max_gain
"""           
a = MaxGain([7,1,5,3,6,4])     # expect 5
print(a) 
a = MaxGain([3, 4, 1, 5, 7, 2])     # expect 6
print(a) 
a = MaxGain([5, 4, 3, 2, 1])    # expect 0
print(a) 
"""

#---------------------------------------------------------------
# List-II Ex.7 (sort a list of lists by their last elements)
def SortLL(lst_lst):
    for i in range(len(lst_lst)-1):
        for j in range(i+1, len(lst_lst)):
            if lst_lst[i][-1] > lst_lst[j][-1]:
                lst_lst[i], lst_lst[j] = lst_lst[j], lst_lst[i]        
    return lst_lst
"""
a = [[1, 3, 5], [2, 4], [9, 7], [3]]
print(SortLL(a))
"""

#---------------------------------------------------------------
# List-II Ex.8 (Build a function PascalsT which takes an integer
# n as an input and generate a n layer Pascals Triangle.)
def PascalsT(n):
    lst = [[1]]
    for i in range(n-1):
        temp = [0] + lst[-1] + [0]
        new_row = []
        for j in range(len(lst[-1])+1):
            new_row.append(temp[j] + temp[j+1])
        lst.append(new_row)
    return lst
"""
print(PascalsT(2))
a = [[1], [1, 1]]
a.append([1,2,1])
print(a)
c = a + [[1,2,1]]
print(c)
"""

#---------------------------------------------------------------
# String Ex.1 (Build a function AllRed that takes a list of strings as input,
# returns a boolean indicating whether all the strings containing word "red")
"""
AllRed(["red hat", "a pair of red shoes", "three red apples"]) returns True
AllRed(["red hat", "white shirt", "black eyes"]) returns False
AllRed([]) returns False
"""
def AllRed(lst_strings):
    if len(lst_strings) == 0:
        return False
    for ind in range(0, len(lst_strings)):
        if "red" not in lst_strings[ind].lower():
            return False
    return True

#---------------------------------------------------------------
# String Ex.2 (Build a function RevStr to reverse a string)
# RevStr("abcd") returns "dcba"
def RevStr(string):
    lst = [s for s in string]
    idx1 = 0
    idx2 = len(lst)-1
    while idx1 < idx2:
        lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
        idx1 += 1
        idx2-= 1
    return "".join(lst)
    
#---------------------------------------------------------------
def RevStr1(string):
    str_out = ""
    if string == "": return True 
    else:   
        for s in reversed(string):
            str_out += s 
        return str_out

"""
a = "abcd"
a = RevStr(a)
print(a)
"""

#---------------------------------------------------------------
# String Ex.3 (Build a function RevSen to reverse a sentence)
# RevSen("we are all friends") returns "friends all are we”
def RevSen(string):
    str_lst = string.split(" ")
    return " ".join(RevLst(str_lst))

#---------------------------------------------------------------
def RevSen1(string):
    str_lst = string.split(" ")
    new_str = ""
    for s in reversed(str_lst):
        if s != str_lst[0]:
            new_str += s + " "
        else: 
            new_str += s    # no need to add space for first word
    return new_str

#print(RevSen("we are all friends"))

#---------------------------------------------------------------
# String Ex.4 (Build a function RevWords to reverse each word of a sentence)
# RevWords("we are all friends") returns "ew era lla sdneirf"
def RevWords(string):
    words_lst = string.split() 
    return " ".join([RevStr(s) for s in words_lst])

#---------------------------------------------------------------
def RevWords1(string):
    words_lst = string.split() 
    new_string = ""
    for ind in range(0, len(words_lst)):
        new_string = new_string + RevStr(words_lst[ind]) + " "       
    new_string = new_string.strip() 
    return new_string    

#print(RevWords("we are all friends"))   
 
#---------------------------------------------------------------
# String Ex.5 (Build a function CapLett to capitalize first letters)
# CapLett("we are all friends") returns "We Are All Friends"
def CapLett(string):
    new_str = ""
    str_lst = string.split(" ")
    for s in str_lst:
        if s != str_lst[-1]:
            new_str += s.capitalize() + " "
        else:
            new_str += s.capitalize()
    return new_str
# string = "we are all friends"
# print(CapLett(string))    

#---------------------------------------------------------------
# String Ex.6 (Build a function RmPunct to remove punctuations from a string)
# RmPunct("He said, that is great!!") returns "He said that is great"
def RmPunct(string):
    new_str = ""
    for s in string:
        if s.isalpha() or s == " ":
            new_str += s 
    return new_str             
#print(RmPunct("He said, that is great!!")) 

#---------------------------------------------------------------
# String Ex.7 (Build a function NGram to which takes a string s and 
# an integer n as inputs, returns a list of n grams of s.)
"""
NGram("techlent", 2) returns ["te", "ec", "ch", "hl", "le", "en", "nt"]
NGram("abc", 3) returns ["abc"]
NGram("abc", 4) returns [   ]
NGram("abc", 1) returns ["a", "b", "c"]
"""
def NGram(string, n):
    str_out = []
    if n > len(string):
        return []
    else:
        for i in range(len(string)-n+1):
            str_out.append(string[i:i+n])
    return str_out
"""
print(NGram("techlent", 2)) 
print(NGram("abc", 4))          
"""            
#---------------------------------------------------------------
# String Ex.8 (Build a function isPalindrome which takes a string as an input
# and returns boolin value telling wheter the string is a palindrome
"""
isPalindrome("abcba") returns True
isPalindrome("abba") returns True
isPalindrome("a") returns True
isPalindrome("") returns True
isPalindrome("abcd") returns False
"""
def  isPalindrome(str):
    if str == RevStr(str):
        return True
    return False
#---------------------------------------------------------------
# String Ex.9 (Build a function LettPalind to determine a string is a palindrome or not.
# We only consider letters this time
"""
LettPalind("909@,.") returns True
LettPalind("He is Sieh!") returns True
LettPalind("His name is Sieh.") returns False
"""
def  LettPalind(str):
    new_str = ""
    for s in str:
        if s.isalnum(): new_str += s.lower() 
    rev_str = ""
    for s in reversed(new_str):
        rev_str += s 
    if new_str == rev_str: 
        return True 
    else: 
        return False
"""    
a ="909@,." 
b = LettPalind(a)
print(b)
a ="He is Sieh!"
b = LettPalind(a)
print(b)
a ="His name is Sieh."
b = LettPalind(a)
print(b)
"""
#---------------------------------------------------------------
# String Ex.10 (Build a function ValidParenthesis to determine the parenthesis in a string are valid.)
"""
ValidParenthesis("((()))()") returns True
ValidParenthesis("()()()") returns True
ValidParenthesis("()()()(") returns False
ValidParenthesis("((())))") returns False
"""
def ValidParenthesis(string):
    stack = []
    for s in string:
        if s == ")": 
            if not stack :
                return False 
            elif stack[-1] == "(":
                stack.pop()
        else:
            stack.append(s)
    return True

#---------------------------------------------------------------
def ValidParenthesis1(string):
    stack = []
    dic = {")":"("}
    for s in string:
        if s in dic: # s=")"           
            if stack and stack[-1] == dic[s]: # last one in stack = "(" 
                stack.pop()
            else:
                return False     
        else: # s="(" 
            stack.append(s)
    if not stack:
        return True 
    else:
        return False
"""
a = "((()))()"
print (ValidParenthesis(a))
a = ")()("
print (ValidParenthesis(a))
"""
#---------------------------------------------------------------
""" 
Dictionary Ex.1 (Build a function kvSwitch to switch the keys and values of a dictionary.)

kvSwitch({"a": "1", "b": "2", "c": "3"}) returns {"1": "a", "2": "b", "3": “c"}
"""
def kvSwitch(dictionary):
    return {dictionary[d]:d for d in dictionary}
#print(kvSwitch({"a": "1", "b": "2", "c": "3"}))

#---------------------------------------------------------------
"""
Dictionary Ex.2 (Build a function RankK which takes a dictionary as input
returns a list of keys which sorted by their values)

RankK({"a": 7, "b": 5, "c": 9}) returns ["b", "a", "c"]
"""
def RankK(dict):
    rev_dict = kvSwitch(dict) #switch key and value
    sorted_dict = sorted(rev_dict) # sort value in the orig dict
    return [rev_dict.get(d) for d in sorted_dict]          
#print(RankK({"a": 7, "b": 5, "c": 9}))

#---------------------------------------------------------------
"""
Dictionary Ex.3 (Build a function ChaFreq to calculate the frequencies 
of characters in a string. Store the results in a dictionary.)

ChaFreq("techlent") returns {"c": 1, "e": 2, "h": 1, "l": 1, "n": 1, "t": 2}
"""
#from collections import Counter
def ChaFreq(str):
    return dict(Counter(str))
#print(ChaFreq("techlent"))

#---------------------------------------------------------------
""" 
Dictionary Ex.4 (Build a function UniqueOnly to detect whether a string 
only contains unique characters.)

UniqueOnly("techlent") returns False
UniqueOnly("abcde") returns True
"""
#from collections import Counter
def UniqueOnly(str):
    str_count = dict(Counter(str))
    if len(str_count) == sum(str_count.values()): 
        return True
    return False

#---------------------------------------------------------------
"""
Dictionary Ex.5 (Build a function SamePattern takes two strings 
as inputs and determines whether they are in the same pattern.)

SamePattern("egg", "zoo") returns True
SamePattern("abb", "ab") returns False
SamePattern("hello", "agree") returns False
SamePattern("aaa", "abc") returns False
SamePattern("abc", "aaa") returns False
"""
def SamePattern(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        for i in range(len(string1)):
            if string1.count(string1[i]) != string2.count(string2[i]):
                return False
        return True
"""
a = SamePattern("egg", "zoo")
print(a)
a = SamePattern("abb", "ab")
print(a)
a = SamePattern("hello", "agree") 
print(a)
a = SamePattern("aaa", "abc") 
print(a)
SamePattern("abc", "aaa") 
print(a)
"""
#---------------------------------------------------------------
"""
Dictionary Ex.6 (Build a function anagrams to determine whether 
two given strings are anagrams.

anagrams("abc", "cba") returns True
anagrams("ab", "abc") returns False
anagrams("abccba", "aabbbc") returns False
"""
def anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        return True 
    return False
"""        
a = anagrams("abc", "cba")
print(a)
a = anagrams("ab", "abc")  
print(a)
a = anagrams("abccba", "aabbbc")  
print(a)
"""
#---------------------------------------------------------------
""" 
Dictionary Ex.7 (Build a function TargetSum which takes a list 
and a target number as inputs. If there are two numbers in the 
list whose sum equals to the target number, the function returns
the indice of the two numbers in list, otherwise returns -1.

TargetSum([1, 2, 5, 9, 8, 11], 6) returns [0, 2] (1+5=6)
TargetSum([1, 2, 5, 9, 8, 11], 11) returns [1, 3]
TargetSum([1, 2, 5, 9, 8, 11], 5) returns -1
TargetSum([1, 2, 5, 9, 8, 11], 14) returns [2, 3]
"""
def TargetSum(lst, target):
    dic = {num for num in lst}
    for num in dic:
        if (target - num) in dic:
            idx_i = lst.index(num)
            idx_j = lst.index(target-num)
            return [idx_i, idx_j]
    return -1 
#print(TargetSum([1,8,5,11, 2, 5, 9, 8, 11], 11) )

