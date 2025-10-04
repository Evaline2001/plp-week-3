def get_response(user_input):
    responses = {
        "hi": "Hello! I’m MindEase, your mental health companion. How are you feeling today?",
        "stress": "I’m sorry to hear you’re feeling stressed. Would you like a few relaxation tips?",
        "anxiety": "Anxiety can be tough. Try deep breathing for 2 minutes — inhale deeply, hold, and exhale slowly.",
        "sad": "It’s okay to feel sad sometimes. Writing down your thoughts might help. Do you want journaling prompts?",
        "bye": "Take care of yourself. Remember, you’re not alone. 💙"
    }
    return responses.get(user_input.lower(), "I understand. Tell me more about how you’re feeling.")
