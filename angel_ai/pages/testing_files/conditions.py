
# Load or create a file to store the state
state_file = "quiz_state.json"
if not st.session_state.get('loaded_state'):
    st.session_state.loaded_state = True
    with open(state_file, 'w') as f:
        json.dump({"current_question_index": 0, "questions_answered": 0}, f)

# Load questions from a JSON file or any other source
        
# Shuffle the problems


# Streamlit UI
st.title('Quiz')

num_questions = min(2, len(questions))  # Limit the quiz to 4 questions or less if there are fewer questions available
correct_answers = 0

# Load the state from the file
with open(state_file, 'r') as f:
    state = json.load(f)

# Check if the "Retake Quiz" button is clicked
if st.button("Retake Quiz"):
    state['current_question_index'] = 0
    state['questions_answered'] = 0



# Check if all questions have been answered
if state['questions_answered'] >= num_questions:
    st.write("Quiz Finished!")
else:
    # Display the current question number
    st.write(f'Question {state["current_question_index"] + 1} of {num_questions}')
    current_question = questions[state['current_question_index']]

    st.header(f"Question {state['current_question_index'] + 1}:")
    st.write(current_question['question'])

    if current_question['type'] == 'mc':
        selected_options = st.multiselect(
            'Select the correct answer(s):', 
            options=current_question['options'], 
            key=f"options_{state['current_question_index']}"
        )

        if st.checkbox('Select all options', key=f"all_options_{state['current_question_index']}"):
            selected_options = current_question['options']
        
        submit_button = st.button('Submit', key=f"submit_{state['current_question_index']}")

        if submit_button:
            state['questions_answered'] += 1
            if set(selected_options) == set([current_question['answer']]):
                st.success('Correct!')
                correct_answers += 1
            else:
                st.error(f"Incorrect! The correct answer is: {current_question['answer']}")
            
            state['current_question_index'] += 1

    elif current_question['type'] == 'sr':
        st.subheader("Use this feature for users to submit answers")
        
        if f"my_input_{state['current_question_index']}" not in st.session_state:
            st.session_state[f"my_input_{state['current_question_index']}"] = ""

        my_input = st.text_input("Input your answer here", key=f"input_{state['current_question_index']}")
        submit = st.button("Submit", key=f"submit_sr_{state['current_question_index']}")

        if submit:
            state['questions_answered'] += 1
            st.session_state[f"my_input_{state['current_question_index']}"] = my_input
            if my_input.strip().lower() == current_question['answer'].strip().lower():
                st.success('Correct!')
                correct_answers += 1
            else:
                st.error(f"Incorrect! The correct answer is: {current_question['answer']}")
            
            state['current_question_index'] += 1

    # Save the updated state to the file
    with open(state_file, 'w') as f:
        json.dump(state, f)

    # Button to move to the next question
    if state['questions_answered'] > 0 and state['current_question_index'] < len(questions):
        next_button = st.button("Next Question")
        if next_button:
            state['current_question_index'] += 1

# Display the result
if state['questions_answered'] >= num_questions:
    st.subheader("Quiz Summary:")
    st.write(f"Number of correct answers: {correct_answers}")
    st.write(f"Questions answered: {state['questions_answered']}")
    if state['questions_answered'] > 0:
        accuracy_ratio = correct_answers / state['questions_answered']
        st.write(f"Accuracy Score: {100 * accuracy_ratio:.2f}%")
    else:
        st.write("Accuracy Ratio: N/A (No questions answered)")
