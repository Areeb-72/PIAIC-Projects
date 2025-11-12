
import datetime

def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    elif 18 <= current_hour < 22:
        return "Good evening"
    else:
        return "Good night"

def get_mood_and_message(text):
    mood_keywords = {
        "happy": ["happy", "joyful", "excited", "thrilled", "great", "good", "wonderful", "amazing", "fantastic", "awesome"],
        "sad": ["sad", "unhappy", "miserable", "depressed", "down", "blue", "crying", "lonely"],
        "angry": ["angry", "mad", "furious", "irritated", "annoyed", "pissed"],
        "anxious": ["anxious", "worried", "nervous", "stressed", "scared", "afraid"],
        "calm": ["calm", "relaxed", "peaceful", "chill", "content"],
        "tired": ["tired", "exhausted", "sleepy", "drained", "fatigued"],
        "motivated": ["motivated", "determined", "inspired", "ready", "focused"],
        "sick": ["sick", "ill", "unwell", "nauseous"],
        "confused": ["confused", "lost", "puzzled", "unsure"],
        "loved": ["loved", "cared", "appreciated", "cherished"]
    }

    mood_messages = {
        "happy": ("Positive 😊", "That's wonderful to hear! Keep shining and spreading that positivity."),
        "sad": ("Sad 😢", "I'm sorry to hear that. Remember that it's okay to not be okay. Things will get better."),
        "angry": ("Angry 😠", "It's understandable to feel angry sometimes. Take a deep breath and try to find a healthy outlet for that anger."),
        "anxious": ("Anxious 😟", "I understand that you're feeling anxious. Focus on the present moment and take things one step at a time."),
        "calm": ("Calm 😌", "It's great that you're feeling calm and relaxed. Enjoy this peaceful moment."),
        "tired": ("Tired 😴", "You sound tired. Make sure to get some rest and recharge your batteries."),
        "motivated": ("Motivated 💪", "That's the spirit! Keep that motivation high and you can achieve anything."),
        "sick": ("Sick 🤒", "I'm sorry you're not feeling well. Make sure to rest and take care of yourself."),
        "confused": ("Confused 😕", "It's okay to be confused sometimes. Take your time to figure things out, and don't be afraid to ask for help."),
        "loved": ("Loved 🥰", "It's a beautiful feeling to be loved. Cherish it and spread the love to others.")
    }

    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if keyword in text.lower():
                return mood_messages[mood]
    return ("Neutral 😐", "I see. Remember to take care of yourself. Every day is a new opportunity.")

def mood_checker():
    print("Welcome to the Mood Checker!")
    print(f"{get_time_based_greeting()}! How are you feeling today?")
    
    user_input = input("> ")
    
    mood, message = get_mood_and_message(user_input)
    
    print(f"\nYour detected mood is: {mood}")
    print(message)
    
    print("\nThank you for using the Mood Checker!")

if __name__ == "__main__":
    mood_checker()
