a = input("Enter a string: ")
n = len(a)
m = a[0:n]
n = a[::-1]
if n == m:
    print("String is palindrome")
else:
    print("String is not palindrome")