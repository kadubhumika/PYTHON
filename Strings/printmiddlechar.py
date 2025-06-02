a = input("Enter a string: ")
n = len(a)

if n == 0:
    print("Your string is empty")

elif n % 2 == 0:
    print("Your string is even")
    print("Your Middle character(s) are: ", end="")
    # Extracting the two middle characters
    print(a[n//2 - 1 : n//2 + 1])

else:
    print("Your string is odd")
    print("Your Middle character is: ", end="")
    # Extracting the single middle character
    print(a[n//2])
