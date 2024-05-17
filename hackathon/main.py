from initialize import db
import random

def main():
    unit_1_1 = [
        {
            'question': '15x = 75',
            'options': ['3', '5', '6', '10'],
            'answer': '5'
        },
        {
            'question': 'Solve for x: 5x - 2 = 13',
            'options': ['1', '2', '3', '4'],
            'answer': '3'
        },
        {
            'question': 'Solve for x: 4x + 6 = 18',
            'options': ['1', '2', '3', '4'],
            'answer': '3'
        },

        {
            'question': 'Solve for x: 6x = 42',
            'options': ['6', '7', '8', '12'],
            'answer': '7'
        },
        {
            'question': 'Solve for x: 3x + 5 = 14',
            'options': ['2', '3', '4', '5'],
            'answer': '3'
        },
        {
            'question': 'Solve for x: 6x - 9 = 15',
            'options': ['2', '3', '4', '5'],
            'answer': '4'
        },
        {
            'question': 'Solve for x: 4x + 5 = 2x + 11',
            'options': ['1', '2', '3', '4'],
            'answer': '3'
        },
        {
            'question': 'Solve for x: 6x + 3 = 4x + 9',
            'options': ['2', '3', '4', '5'],
            'answer': '3'
        },
        {
            'question': 'Solve for x: 5x - 2 = 3x + 4',
            'answer': '3'
        },
        {
            'question': 'Solve for x: 2x + 3 = x + 7',
            'answer': '3'
        },
        {
            'question': 'Solve for x: 9x + 25 = 5x + 65',
            'answer': '10'
        },
        {
            'question': 'Solve for x: 7x + 15 = 3x + 35',
            'answer': '5'
        },
        {
            'question': 'Solve for x: 8x + 20 = 100',
            'answer': '10'
        },
        {
            'question': 'Solve for x: 7x + 49 = 98',
            'answer': '7'
        },
        {
            'question': 'Solve for x: 11x - 33 = 88',
            'answer': '11'
        }
]

    chosen_equations = []

    user = db.collection("users").document("Dorian0G")
    unit_1 = user.collection("Algebra 1").document("Unit 1")
    lesson = unit_1.collection(f"Lesson 1").get()
    score = 0

    for question in lesson:
        remaining_equations = [eqn for eqn in unit_1_1 if eqn['question'] not in chosen_equations]
        random_equation = random.choice(remaining_equations)
        question.reference.set(random_equation)
        chosen_equations.append(random_equation['question'])

        print(f"{random_equation['question']}")
        answer = input("x = ")
        
        if random_equation['options'].exists:
            for option in random_equation['options']:
                print(option)

        if answer == random_equation['answer']:
            question.reference.update({'Correct': True})
            print("Correct!")
            score += 1
        else:
            question.reference.update({'Correct': False})
            print("Incorrect")
    
    print(f"Score: {score}/5")
    unit_1.update({"`Lesson 1`.Score": score})

if __name__ == "__main__":
    main()

