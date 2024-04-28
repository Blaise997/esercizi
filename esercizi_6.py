string = input("Enter a string: ")


def isPalindrome(string):
    return string == string[::-1]


# Driver code
ans = isPalindrome(string)

if ans:
    print("Yes")
else:
    print("No")