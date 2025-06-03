a = input("Enter any string: ")
vowels = "aeiouAEIOU"
new_string = ""

for char in a:
    if char not in vowels:
        new_string += char

if new_string == a:
    print("There is no vowel in your string.\n")
else:
    m = len(new_string)
    slice = new_string[0:m]  # or any portion like new_string[0:5]
    print(f"After removing vowels from '{a}', the string is: '{slice}'")
