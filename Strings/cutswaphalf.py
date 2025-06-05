a = input("Enter a string : ")
n = len(a)
if n % 2 != 0:
    print(f"Your string length {n} is an odd number.")
    mid = n // 2
    print("After reversing :")
    new_string = a[mid+1:]  + a[:mid]
    print("Result:", new_string)

elif n % 2 == 0:
    print(f"Your string length {n} is an even number.")
    mid = n // 2
    print("After reversing :")
    new_string = a[mid:] + a[:mid]
    print("Result:", new_string)

else:
    print(a)
