string = input("Enter a string: ")
new_string = string.split(" ")
print(new_string)
n=len(new_string)
alternate = new_string[0:n:2]
print("After silicing alternate string : ")
print(alternate)