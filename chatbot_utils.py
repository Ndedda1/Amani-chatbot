from knowledge_base import mental_health_knowledge_base as knowledge_base

def match_disorder(user_input):
    user_input_lower = user_input.lower()
    for disorder, data in knowledge_base.items():
        for sign in data.get("signs", []):
            if sign.lower() in user_input_lower:
                return disorder
    return None

def get_follow_up_questions(disorder):
    return knowledge_base.get(disorder, {}).get("follow_up_questions", [])

def get_coping_mechanisms(disorder):
    data = knowledge_base.get(disorder, {})
    return data.get("coping_mechanisms", ["No coping mechanisms found."])

def personalize_response(response, demographics):
    age = demographics.get("age", "unknown age")
    gender = demographics.get("gender", "unknown gender")
    occupation = demographics.get("occupation", "unknown occupation")
    stress = demographics.get("stress_level", 5)

    return (
        f"{response}\n\n"
        f"_You're a {age}-year-old {gender.lower()} working as a {occupation}. "
        f"Your reported stress level is {stress}/10._"
    )

def generate_final_advice(disorder, demographics):
    occupation = demographics.get("occupation", "").lower()
    advice_samples = {
        "student": "As a student, balancing academics and mental health is vital. Consider speaking with a counselor at school.",
        "teacher": "As a teacher, burnout is common. Set aside quiet time and talk to a mental health professional if needed.",
        "doctor": "Even caregivers need care. Don’t hesitate to reach out for support — your well-being matters too.",
        "engineer": "With a demanding job, mental fatigue can sneak up. Regular breaks and mindfulness may help manage stress.",
    }
    return advice_samples.get(occupation, "Remember, it's okay to seek support — you're not alone in this.")
