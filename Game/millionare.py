questions_list = [
    ["What is the next number in the series: 2, 4, 8, 16, ?",
     "18", "24", "32", "30", "28", 3],

    ["A train running at 60 km/h crosses a pole in 30 seconds. What is the length of the train?",
     "300 m", "400 m", "500 m", "600 m", "200 m", 3],

    ["What will be the average of 10, 20, 30, 40, 50?",
     "25", "30", "35", "40", "45", 2],

    ["If the cost of 5 pens is ₹50, what is the cost of 12 pens?",
     "₹100", "₹110", "₹120", "₹130", "₹140", 3],

    ["Find the odd one out: 3, 5, 11, 14, 17",
     "3", "5", "11", "14", "17", 4],

    ["Which number is divisible by 9?",
     "12345", "34567", "891", "1002", "1567", 3],

    ["If A = 1, B = 2, ..., then what is the sum of the letters in the word 'DOG'?",
     "21", "22", "23", "24", "26", 4],

    ["A shopkeeper sells an article at ₹250 after giving a discount of 20%. What is the marked price?",
     "₹300", "₹310", "₹312.50", "₹320", "₹325", 3],

    ["Which figure comes next: 1, 4, 9, 16, ?",
     "20", "25", "24", "30", "36", 2],

    ["If 5x – 3 = 2, what is the value of x?",
     "0", "1", "2", "3", "4", 4],
]

score = 0

for i, question in enumerate(questions_list):
    print(f"\nQuestion {i + 1}: {question[0]}")
    print(f"a: {question[1]}")
    print(f"b: {question[2]}")
    print(f"c: {question[3]}")
    print(f"d: {question[4]}")
    print(f"e: {question[5]}")

    try:
        ans = int(input("Enter your answer (1-5): "))
        if ans == question[6]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    except Exception as e:
        print(" Invalid input! Please enter a number from 1 to 5.")

print(f"\nYour final score is: {score}/{len(questions_list)}")
