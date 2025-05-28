from token import STRING

a = input("Enter Person Name : ")
a1 = int(input("Enter Value  : "))
string = "Hello {} ! Nice to meet you . I love your work please take {}$ Bag A gift from mee ".format(a,a1)
print(string)



values = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in values]
length = len(numbers)

for i in range(length):
    average = sum(numbers[:i+1]) / (i+1)
    print(f"Average after {i+1} number(s): {average}")


def makecoffee(sugar, water, milk, ginger, teapowder):
    name = input("Enter person name: ")
    print(f"{name}, do you want to make coffee with me?")
    a = input("Enter your answer (yes/no): ").strip().lower()

    if a == "yes":
        print("Let's do it! Have fun!")
    else:
        print("Okay!")

    return (
        f"Done! Here's our special tea:\n"
        f"- {sugar} teaspoon(s) of sugar\n"
        f"- {water} ml of water\n"
        f"- {milk} ml of milk\n"
        f"- {ginger} of ginger\n"
        f"- {teapowder} of tea powder"
    )

# Taking inputs
sugar = int(input("Enter how many teaspoons of sugar you want: "))
water = input("Enter your water amount (ml): ")
milk = input("Enter your milk amount (ml): ")
ginger = input("Enter your ginger amount: ")
teapowder = input("Enter your tea powder amount: ")

# Calling the function and printing the result
print(makecoffee(sugar, water, milk, ginger, teapowder))


def makecoffee():
    while True:
        name = input("Enter person name: ")
        print(f"{name}, do you want to make coffee with me?")
        a = input("Enter your answer (yes/no): ").strip().lower()

        if a == "yes":
            print("Let's do it! Have fun!")

            # Take coffee ingredients input
            sugar = int(input("Enter how many teaspoons of sugar you want: "))
            water = input("Enter your water amount (ml): ")
            milk = input("Enter your milk amount (ml): ")
            ginger = input("Enter your ginger amount: ")
            teapowder = input("Enter your tea powder amount: ")

            print("\nDone! Here's our special tea:")
            print(f"- {sugar} teaspoon(s) of sugar")
            print(f"- {water} ml of water")
            print(f"- {milk} ml of milk")
            print(f"- {ginger} of ginger")
            print(f"- {teapowder} of tea powder\n")

        else:
            print("Okay! Maybe next time.")
            break  # Exit the loop when user says 'no'


# Call the function
makecoffee()

