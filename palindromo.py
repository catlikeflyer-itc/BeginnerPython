def isPalindrome(s):
    return s == s[::-1]
 

s = input("Palabra: ")
ans = isPalindrome(s.lower().replace(' ', ''))

if ans:
    print("si")
else:
    print("no")