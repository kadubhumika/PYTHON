from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of funny/cool/dirty nickname parts
adjectives = [
    "Crazy", "Happy", "Sleepy", "Savage", "Fluffy", "Cool", "Epic", "Silent",
    "Funky", "Brave", "Sassy", "Cheeky", "Naughty", "Dirty", "Wicked", "Horny",
    "Thirsty", "Saucy", "Spicy", "Wild"
]

animals = [
    "Panda", "Tiger", "Shark", "Penguin", "Lion", "Otter", "Eagle", "Wolf",
    "Cat", "Dog", "Fox", "Sloth", "Beaver", "Cougar", "Donkey", "Moose", "Snake",
    "Dragon", "Goat"
]

male_names = [
    "Arjun", "Rohan", "Karan", "Vikram", "Rahul", "Siddharth", "Aarav", "Vihaan",
    "Ishaan", "Kabir", "Dev", "Aditya", "Raj", "Krish", "Vikramaditya"
]

female_names = [
    "Prachi", "Divya", "Bhumika", "Siddhi", "Anushka", "Riya", "Simran", "Kavya",
    "Aditi", "Sneha", "Pooja", "Meera", "Isha", "Anjali", "Neha", "Tanvi"
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]

        if gender == "Male":
            adjectives = ["Brave", "Savage", "Cool", "Epic", "Macho"]
            animals = ["Tiger", "Lion", "Wolf", "Eagle", "Shark"]
        elif gender == "Female":
            adjectives = ["Lovely", "Graceful", "Sassy", "Queen", "Charming"]
            animals = ["Kitten", "Dove", "Butterfly", "Panda", "Fox"]
        else:  # Other
            adjectives = ["Epic", "Funky", "Cool", "Crazy", "Mysterious"]
            animals = ["Dragon", "Phoenix", "Panda", "Otter", "Hawk"]

        nickname = random.choice(adjectives) + " " + random.choice(animals)
        return render_template("index.html", nickname=nickname)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)