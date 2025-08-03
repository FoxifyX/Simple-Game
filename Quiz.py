import random


questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the boiling point of water (in Celsius)?", "100"),
    ("What is 9 x 8?", "72"),
    ("What does CPU stand for?", "Central Processing Unit"),
    ("Which ocean is the largest?", "Pacific"),
    ("What is the square root of 144?", "12"),
    ("Which gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
    ("Who painted the Mona Lisa?", "Da Vinci"),
    ("Which country is known as the Land of the Rising Sun?", "Japan"),
    ("How many continents are there on Earth?", "7"),
    ("Which planet is closest to the Sun?", "Mercury"),
    ("What is the chemical symbol for Gold?", "Au"),
    ("How many sides does a hexagon have?", "6"),
    ("In which year did World War II end?", "1945"),
    ("What is the currency of the United Kingdom?", "Pound"),
    ("Who discovered gravity?", "Newton"),
    ("What is the longest river in the world?", "Nile"),
    ("Which language is used to create web pages?", "HTML"),
    ("What is the freezing point of water?", "0"),
    ("Which animal is known as the King of the Jungle?", "Lion"),
    ("How many bones are there in the human body?", "206"),
    ("Which metal is liquid at room temperature?", "Mercury"),
    ("What is the smallest prime number?", "2"),
]

def selected_questions():
    number = False
    while not number:

        ques_number = input("👉 Select your question amount[5-20]: ")

        if ques_number.isdigit():
            ques_number = int(ques_number)
            if ques_number < 5:
                print("📝Please enter above 5!")
            elif ques_number > 20:
                print("📝Please enter less than 20!")
            else:    
                ques_number = int(ques_number)
                li = random.sample(questions, ques_number)
                number = True
                return li

        else:
            print("⚠️ Please select a valid number!")



    

     
def question_ans():
    score = 0

    print("\n✅ Game started..")
    for idx,(question,answer) in enumerate(li, start=1):
        
        print(f"\n{idx}.{question}")
        user_ans = input("Enter your answer: ")

        if user_ans.strip().lower() != answer.strip().lower():
            print(f"❌ Wrong\n✅ Correct answer: {answer}")

        else:
            print("✅ Correct")
            score += 1
    print(f"\nYour score: {score}\n")



            
    

print("\n---Game Rules---\n# You will get 1 point for each correct answer!\n")


reply = False

while not reply:
    li = selected_questions()
    question_ans()
    re_play = False

    while not re_play:
        again = input("Do you want to play again?[y/n]: ").strip().lower()    
        if again == "n":
            print("✅ You have successfully exited the quiz game...")
            reply = True
            re_play = True


        elif again == "y":
            print("\n🔄 Continuing...")
            re_play = True


        else:
            print("Please enter Y or N...")










