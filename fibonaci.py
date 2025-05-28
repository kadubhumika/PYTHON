def reverse_string(s):
    if s == "":
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

name = input("Enter your name: ")
print("Reversed name using recursion:", reverse_string(name))





