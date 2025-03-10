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




