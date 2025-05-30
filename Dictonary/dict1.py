n = input('Enter a number: ')

tables = {f"{n} * {i}": n * i for i in range(1, 11)}
print(tables)
