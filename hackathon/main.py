from initialize import db
import random

def main():
    unit_1_1 = [
        {"equation": "15x = 75", "value": 5},
        {"equation": "6x = 42", "value": 7},
        {"equation": "7x + 12 = 40", "value": 4},
        {"equation": "9x + 15 = 4x + 5", "value": -2},
        {"equation": "2x + 5 = 11", "value": 3},
        {"equation": "3x + 7 = 2x + 12", "value": 5},
        {"equation": "2x + 9 = 5x - 6", "value": 5},
        {"equation": "16x + 11 = 75", "value": 4}
    ]

    chosen_equations = []

    user = db.collection("users").document("Dorian0G")
    unit_1 = user.collection("Algebra 1").document("Unit 1")
    unit_lesson = input("Lesson: ")
    lesson = unit_1.collection(f"Lesson {unit_lesson}").get()
    score = 0

    for question in lesson:
        remaining_equations = [eqn for eqn in unit_1_1 if eqn['equation'] not in chosen_equations]
        random_equation = random.choice(remaining_equations)
        question.reference.set(random_equation)
        chosen_equations.append(random_equation['equation'])

        answer = int(input(f"{random_equation['equation']}\nx = "))
        
        if answer == random_equation['value']:
            question.reference.update({'Correct': True})
            print("Correct!")
            score += 1
        else:
            question.reference.update({'Correct': False})
            print("Incorrect")
    
    print(f"Score: {score}/5")
    unit_1.update({f"`Lesson {unit_lesson}`.Score": score})

if __name__ == "__main__":
    main()

