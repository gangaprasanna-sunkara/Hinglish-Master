import random
words = [
    {"Hindi": "namaste", "English": "Hello"},
    {"Hindi": "haan", "English": "Yes"},
    {"Hindi": "nahin", "English": "No"},
    {"Hindi": "dhanyavaad", "English": "Thank you"},
    {"Hindi": "kripya", "English": "Please"},
    {"Hindi": "maaf kijiye", "English": "Sorry"},
    {"Hindi": "accha", "English": "Good"},
    {"Hindi": "bura", "English": "Bad"},
    {"Hindi": "sundar", "English": "Beautiful"},
    {"Hindi": "sachcha", "English": "True"},
    {"Hindi": "jhootha", "English": "False"},
    {"Hindi": "aap", "English": "You"},
    {"Hindi": "main", "English": "I"},
    {"Hindi": "vah", "English": "He/She"},
    {"Hindi": "hum", "English": "We"},
    {"Hindi": "yah", "English": "This"},
    {"Hindi": "vah", "English": "That"},
    {"Hindi": "kaun", "English": "Who"},
    {"Hindi": "kya", "English": "What"},
    {"Hindi": "kahaan", "English": "Where"},
    {"Hindi": "kyon", "English": "Why"},
    {"Hindi": "kaise", "English": "How"},
    {"Hindi": "kab", "English": "When"},
    {"Hindi": "sab", "English": "All"},
    {"Hindi": "kuchh", "English": "Some"},
    {"Hindi": "ek", "English": "One"},
    {"Hindi": "do", "English": "Two"},
    {"Hindi": "teen", "English": "Three"},
    {"Hindi": "chaar", "English": "Four"},
    {"Hindi": "paanch", "English": "Five"},
    {"Hindi": "bada", "English": "Big"},
    {"Hindi": "chhota", "English": "Small"},
    {"Hindi": "lamba", "English": "Tall"},
    {"Hindi": "thanda", "English": "Cold"},
    {"Hindi": "sasta", "English": "Cheap"},
    {"Hindi": "mahenga", "English": "Expensive"},
    {"Hindi": "aasaan", "English": "Easy"},
    {"Hindi": "kathin", "English": "Difficult"},
    {"Hindi": "purana", "English": "Old"},
    {"Hindi": "naya", "English": "New"},
    {"Hindi": "tez", "English": "Fast"},
    {"Hindi": "dheema", "English": "Slow"},
    {"Hindi": "khush", "English": "Happy"},
    {"Hindi": "dukhi", "English": "Sad"},
    {"Hindi": "bhukha", "English": "Hungry"},
    {"Hindi": "pyasa", "English": "Thirsty"},
    {"Hindi": "saaf", "English": "Clean"},
    {"Hindi": "ganda", "English": "Dirty"},
    {"Hindi": "kholna", "English": "Open"},
    {"Hindi": "band", "English": "Close"},
    {"Hindi": "kharidna", "English": "Buy"},
    {"Hindi": "bechna", "English": "Sell"},
    {"Hindi": "sochna", "English": "Think"},
    {"Hindi": "jaanna", "English": "Know"},
    {"Hindi": "samajhna", "English": "Understand"},
    {"Hindi": "chahna", "English": "Want"},
    {"Hindi": "karna", "English": "Do"},
    {"Hindi": "lena", "English": "Take"},
    {"Hindi": "dena", "English": "Give"},
    {"Hindi": "dekhna", "English": "See"},
    {"Hindi": "sunna", "English": "Hear"},
    {"Hindi": "padhana", "English": "Read"},
    {"Hindi": "likhna", "English": "Write"},
    {"Hindi": "chalna", "English": "Walk"},
    {"Hindi": "daudna", "English": "Run"},
    {"Hindi": "baithna", "English": "Sit"},
    {"Hindi": "khada hona", "English": "Stand"},
    {"Hindi": "sona", "English": "Sleep"},
    {"Hindi": "khana", "English": "Eat"},
    {"Hindi": "peena", "English": "Drink"},
    {"Hindi": "pyaar karna", "English": "Love"},
    {"Hindi": "nafrat karna", "English": "Hate"},
    {"Hindi": "khelna", "English": "Play"},
    {"Hindi": "kaam karna", "English": "Work"},
    {"Hindi": "seekhna", "English": "Learn"},
    {"Hindi": "padhai karna", "English": "Study"},
    {"Hindi": "bolna", "English": "Speak"},
    {"Hindi": "rukna", "English": "Stop"},
    {"Hindi": "shuru karna", "English": "Start"},
    {"Hindi": "samaapt karna", "English": "Finish"},
    {"Hindi": "milna", "English": "Meet"},
    {"Hindi": "dikhana", "English": "Show"},
    {"Hindi": "dhoondna", "English": "Search"},
    {"Hindi": "khojna", "English": "Find"},
    {"Hindi": "yaad karna", "English": "Remember"},
    {"Hindi": "bhoolna", "English": "Forget"},
    {"Hindi": "hona", "English": "Be"},
    {"Hindi": "jana", "English": "Go"},
    {"Hindi": "aana", "English": "Come"},
    {"Hindi": "rehna", "English": "Stay"},
    {"Hindi": "jeetna", "English": "Win"},
    {"Hindi": "harna", "English": "Lose"},
    {"Hindi": "pasand karna", "English": "Like"},
    {"Hindi": "naapasand karna", "English": "Dislike"},
    {"Hindi": "uthna", "English": "Get up"},
    {"Hindi": "sahi", "English": "Right"},
    {"Hindi": "galat", "English": "Wrong"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words :
        print(f"What is the english translation of {word["Hindi"]} ?")
        user_answer = input("Enter your answer: ").strip().lower()
        correct_answer = word["English"].lower()

        if user_answer == "quit":
            print("\nYou chose to quit the quiz.")
            print("Keep learning and improving your vocabulary. Goodbye!")
            return
        
        if user_answer == correct_answer :
            print("Undeniably True")
            score += 1

        else :
            print("Wrong ! Learn this word and Expand your vocabulary ")
            print(f"The correct word for {word['Hindi'].upper()} is {word['English'].upper()}")
        

    print(f"Quiz completed ! Your Accuracy :{score}/{len(words)}")

def main():
    print("Welcome to Hinglish Master Language Learning App!!!!")
    print("Type 'quit' anytime to exit the app.")
    print("Press enter to learn language through quiz....")
    input()
    quiz_user(words)

if __name__ == "__main__":
    main()