a = input("Enter a string: ")
n = len(a)
char = input("Enter a character to insert: ")

if n % 2 != 0:
    print(f"Your string length {n} is an odd number.")
    mid = n // 2
    new_string = a[:mid] + char + a[mid + 1:]  # Replace middle character
    print("Result:", new_string)

elif n % 2 == 0:
    print(f"Your string length {n} is an even number.")
    mid = n // 2
    new_string = a[:mid] + char + a[mid:]  # Insert in the exact middle
    print("Result:", new_string)

else:
    print(a)
