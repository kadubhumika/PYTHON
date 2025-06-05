# program to print BHUMkadu
a = input("Enter a string : ")
n = len(a)
if n % 2 != 0:
    print(f"Your string length {n} is an odd number.")
    mid = n // 2
    first_half = a[:mid]
    second_half = a[mid:]
    print("After capitizing first half and lowering second half gives :")
    new_string = first_half.upper() +  second_half.lower()
    print("Result:", new_string)

elif n % 2 == 0:
    print(f"Your string length {n} is an even number.")
    mid = n // 2
    first_half = a[:mid]
    second_half = a[mid:]
    print("After capitizing first half and lowering second half gives :")
    new_string = first_half.upper() +  second_half.lower()
    print("Result:", new_string)

else:
    print(a)
    