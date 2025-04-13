# 1.Reverse a string.

def reverse_string(s):
    s=list(s)
    start=0
    end=len(s)-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return "".join(s)
# print(reverse_string("hi hello"))



# 2.Check if a string is a palindrome.


def is_palindrome(s):
    start=0
    end=len(s)-1
    while start<end:
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
    return True
# print(is_palindrome("mamam"))


# 3.Count the number of vowels and consonants in a string.

def count_vc(s):
    vowels='aeiouAEIOU'
    v_count=0
    c_count=0
    for i in range(len(s)):
        char=s[i]
        if ('a'<=char<='z' or 'A'<=char<='Z'):
            if char in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count
# print(count_vc("Hello World"))


# 4.Remove spaces from a string.


def remove_spaces(s):
    result=[]
    for i in range(len(s)):
        if s[i]!=' ':
            result.append(s[i])
    return ''.join(result)
# print(remove_spaces('hello hii rakesh garu'))


# 5.count the occurence of a character in string

def occurence_String(s,char):
    count=0
    for i in s:
        if i==char:
            count+=1
    return count
# print(occurence_String("keerthiRakesh","k"))


# 6.count no.of vowels,consonants,spaces in string

def count_VCS(s):
    V=0
    C=0
    S=0
    vowels="A","E","I","O","U","a","e","i","o","u"
    for i in s:
        if i in vowels:
            V+=1
        elif i==' ':
            S+=1
        elif i.isalpha():
            C+=1
    return V,C,S
# print(count_VCS("keerthi keerthana good girl"))


# 7.Remove all vowels from the string

def remove_vowels(s):
    vowels="AEIOUaeiou"
    new_string=""
    for i in s:
        if i not in vowels:
            new_string+=i
    return new_string
# print(remove_vowels("keerthi keerthana"))

# 8.remove characters from string except alphabets


def remove_char(s):
    new_s=""
    for i in s:
        if i.isalpha():
            new_s+=i
    return new_s
# print(remove_char("keerthi@kerthana!!"))

# 9.Checking if Two Strings are Anagrams of each other

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    c1={}
    c2={}
    for i in s1:
        if i in c1:
            c1[i]+=1
        else:
            c1[i]=1
    for i in s2:
        if i in c2:
            c2[i]+=1
        else:
            c2[i]=1
    return c1==c2
# print(is_anagram("listen", "silent"))

# 10.maximum occurence character in string

def max_occurence(string):
    count={}
    max=0
    most_occurence=None
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        if count[i]>max:
            max=count[i]
            most_occurence=i
    return most_occurence
# print(max_occurence("keerthi"))



            

def longest_consecutive(s):
    longest_char=s[0]
    longest_char_count=1
    current_char=s[0]
    current_char_count=1
    for i in range(1,len(s)):
        if s[i]==current_char:
            current_char_count+=1
        else:
            current_char=s[i]
            current_char_count=1
    if current_char_count>longest_char_count:
        longest_char_count=current_char_count
        longest_char=current_char
    return longest_char
# print(longest_consecutive("keeeerthiiiiiii"))





