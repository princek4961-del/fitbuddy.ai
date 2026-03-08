
def generate_workout(user):

    plan=f"""
7 DAY WORKOUT PLAN

Goal: {user.goal}
Intensity: {user.intensity}

Day 1 – Cardio + Abs
Day 2 – Upper Body
Day 3 – Running + Core
Day 4 – Rest
Day 5 – Lower Body
Day 6 – Full Body
Day 7 – Yoga + Recovery
"""

    return plan


def nutrition_tip(goal):

    if goal=="Weight Loss":
        return "Eat high protein foods and reduce sugar intake."

    if goal=="Muscle Gain":
        return "Include protein in every meal and stay hydrated."

    return "Maintain balanced diet and drink enough water."
