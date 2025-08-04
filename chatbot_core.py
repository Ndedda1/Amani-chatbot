from knowledge_base import mental_health_knowledge_base
from chatbot_utils import (
    match_disorder,
    get_follow_up_questions,
    get_coping_mechanisms,
    personalize_response,
    generate_final_advice
)

def handle_user_input(user_input, demographics, current_disorder, question_index):
    if not current_disorder:
        predicted_disorder = match_disorder(user_input)

        if not predicted_disorder:
            return (
                "I'm here to help, but I couldn't identify a specific issue yet. "
                "Could you tell me a bit more about how you’re feeling?",
                None,
                0
            )

        follow_ups = get_follow_up_questions(predicted_disorder)
        if follow_ups:
            return (
                f"It sounds like you may be experiencing symptoms of **{predicted_disorder}**.\n\n"
                f"{follow_ups[0]}",
                predicted_disorder,
                1
            )
        else:
            coping_mechs = get_coping_mechanisms(predicted_disorder)
            advice = generate_final_advice(predicted_disorder, demographics)
            full_response = (
                f"It sounds like you may be experiencing symptoms of **{predicted_disorder}**.\n\n"
                f"Here are some coping mechanisms:\n"
                + "\n".join(f"- {tip}" for tip in coping_mechs)
                + "\n\n" + advice
            )
            return personalize_response(full_response, demographics), predicted_disorder, 0

    else:
        follow_ups = get_follow_up_questions(current_disorder)
        if question_index < len(follow_ups):
            return follow_ups[question_index], current_disorder, question_index + 1
        else:
            coping_mechs = get_coping_mechanisms(current_disorder)
            advice = generate_final_advice(current_disorder, demographics)
            full_response = (
                f"Thanks for sharing more. Based on what you've said, you may be experiencing **{current_disorder}**.\n\n"
                f"Here are some coping mechanisms:\n"
                + "\n".join(f"- {tip}" for tip in coping_mechs)
                + "\n\n" + advice
            )
            return personalize_response(full_response, demographics), current_disorder, question_index
