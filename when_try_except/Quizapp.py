# Authentication process
def authenticate():
    def decorator(function):
        def wrapper():
            name = input("Enter your name: ")
            password = input("Create a password: ")
            email = input("Enter your email: ")
            print("Authentication successful\n")
            return function(name, email)
        return wrapper
    return decorator

@authenticate()
def splash(name, email):
    print(f"Welcome to the 'Know Me' app, {name}! Are you excited to play?")
    a = input("(yes/no): ").lower()
    if a == "yes":
        gamezone(name)
    else:
        print("Thank you!")

def gamezone(name):
    print(f"\n{name}, You have been given 5 questions about Bhumika!\nEach question has 5 options. Get ready!\n")

    questions = [
        {
            "question": "What is Bhumika's favorite free time activity?",
            "options": ["Eating", "Photography", "Spending time with special one", "Modelling", "Watching mobile"],
            "answer": "Photography"
        },
        {
            "question": "What will Bhumika choose first?",
            "options": ["Party/Dj night", "Hanging out with friends", "Travelling/Trip with friends", "Sleeping", "Muze kya pata !"],
            "answer": "Travelling/Trip with friends"
        },
        {
            "question": "What’s a phrase Bhumika says often nowadays?",
            "options": ["Gandu", "Abe", "Dimag kharab", "Dammn!", "Cool!"],
            "answer": "Dammn!"
        },
        {
            "question": "When is Bhumika's birthday?",
            "options": ["2", "5", "7", "9", "21"],
            "answer": "7"
        },
        {
            "question": "When did you and Bhumika meet offline first (face-to-face)?",
            "options": ["At college event", "During first Interview", "During first meet", "While debugging my compiler problem in lab", "Open house meet"],
            "answer": "During first meet"
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i + 1}: {q['question']}")
        for j, opt in enumerate(q["options"], 1):
            print(f"{j}. {opt}")

        try:
            user_choice = int(input("Enter your choice (1-5): "))
            if 1 <= user_choice <= len(q["options"]):
                if q["options"][user_choice - 1].lower() == q["answer"].lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {q['answer']}")
            else:
                print("Invalid choice. Skipping question.")
        except ValueError:
            print("Invalid input. Skipping question.")

    print(f"\ Your final score: {score}/5")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        gamezone(name)
    else:
        print("Thanks for playing!")


splash()


