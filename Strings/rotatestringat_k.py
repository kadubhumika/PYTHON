#example bhumika
#k=2
#output = umikabh
a = input("Enter a string: ")
n = len(a)
k = input("Enter a k value value from which to rotate string: ")
k = int(k)
print("After rotating string: ", end="")
print(a[k:] + a[:k])