import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from image_logic import rand_img_set_size
###Authentication###
import yaml
from yaml.loader import SafeLoader

with open('pages/config.YAML') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
authenticator.login()
if st.session_state["authentication_status"]:
    st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout()
    
else:
    # Create a column for the register button
    col1, col2 = st.columns([1, 3])  # Adjust the ratio to position the button on the left
    with col1:
        register_button = st.button("Register")

    if register_button:
        st.switch_page('pages/register.py')
        
class Question:
    def __init__(self, id, quest, op1, op2, op3, op4, ans):
        self.id = id
        self.question = quest
        self.option1 = op1
        self.option2 = op2
        self.option3 = op3
        self.option4 = op4
        self.answer = ans

class Assignment:
    def __init__(self, excel_file):
        self.questions = list()
        self.loadAssignment(excel_file)

    def numQuestions(self):
        return len(self.questions)
    
    def getQuestion(self, index):
        return self.questions[index]
    
    def loadAssignment(self, excel_file):
        self.questions.clear()
        dataframe = pd.read_excel(excel_file)
        num_rows = dataframe.shape[0] 
        for row in range(num_rows):
            id = dataframe.iat[row, 0]
            quest = dataframe.iat[row, 1]
            op1 = dataframe.iat[row, 2]
            op2 = dataframe.iat[row, 3]
            op3 = dataframe.iat[row, 4]
            op4 = dataframe.iat[row, 5]
            ans = dataframe.iat[row, 6]
            self.questions.append(Question(id, quest, op1, op2, op3, op4, ans))
        st.session_state["NumQuestions"] = self.numQuestions()

def initSessionVariables():
    if "Assignment" not in st.session_state:
        st.session_state["Assignment"] = None
    if "NumQuestions" not in st.session_state:
        st.session_state["NumQuestions"] = 0
    if "Attempted" not in st.session_state:
        st.session_state["Attempted"] = 0
    if "Correct" not in st.session_state:
        st.session_state["Correct"] = 0
    if "Wrong" not in st.session_state:
        st.session_state["Wrong"] = 0
    if "Submitted" not in st.session_state:
        st.session_state["Submitted"] = False
    if "Answers" not in st.session_state:
        st.session_state["Answers"] = {}
    if "IncorrectAnswers" not in st.session_state:
        st.session_state["IncorrectAnswers"] = {}

def validateAnswers():
    assignment = st.session_state["Assignment"]
    total = assignment.numQuestions()
    correct = 0; not_attempted = 0
    correct_answer = ""
    answers = st.session_state["Answers"]
    incorrect_answers = {}
    
    for index in range(total):
        q = assignment.getQuestion(index)
        submitted_answer = answers[q.id]
        if submitted_answer == None:
            not_attempted += 1
            continue
        correct_choice = int(q.answer) - 1
        answer_list = [q.option1, q.option2, q.option3, q.option4]
        correct_answer = answer_list[correct_choice]
        if submitted_answer == correct_answer:
            correct += 1
        else:
            incorrect_answers[q.id] = {
                "question": q.question,
                "submitted": submitted_answer,
                "correct": correct_answer
            }
    
    st.session_state["Correct"] = correct
    attempted = total - not_attempted
    st.session_state["Attempted"] = attempted
    st.session_state["Wrong"] = attempted - correct
    st.session_state["IncorrectAnswers"] = incorrect_answers
    st.session_state["Answers"] = answers

def submitClicked():
    st.session_state["Submitted"] = True
    st.success("Your answers have been submitted!")
    validateAnswers()

def loadAssignment():
    if st.session_state["Assignment"] == None:
        st.session_state["Assignment"] = Assignment('math_problems/new_problems_Problems.xlsx') 
    return st.session_state["Assignment"]
    
def displayAssignment(assignment):
    answers = {}
    st.title("💀Math Quiz💀")
    df = pd.DataFrame({"Total Questions":[st.session_state["NumQuestions"]], 
                        "Attempted":[st.session_state["Attempted"]], 
                        "Correct":[st.session_state["Correct"]], 
                        "Wrong": [st.session_state["Wrong"]]})
    
    st.dataframe(df.set_index(df.columns[0]))
    rand_img_set_size(None, 'math_memes')
    for index in range(assignment.numQuestions()):
        q = assignment.getQuestion(index)
        st.subheader(f"Question-{index+1}")
        r = st.radio(q.question, [q.option1, q.option2, q.option3, q.option4], index=None, 
                    disabled=st.session_state["Submitted"], key=q.id)
        answers[q.id] = r
        st.divider()
    st.session_state["Answers"] = answers
    st.button('Submit', disabled=st.session_state["Submitted"], on_click=submitClicked)

    # Display incorrect answers if submitted
    if st.session_state["Submitted"] and st.session_state["IncorrectAnswers"]:
        st.subheader("Incorrect Answers")
        for qid, info in st.session_state["IncorrectAnswers"].items():
            st.write(f"**Question**: {info['question']}")
            st.write(f"**Your Answer**: {info['submitted']}")
            st.divider()

# -------- Entry Point --------
# Run: streamlit run MCQ.py
initSessionVariables()
displayAssignment(loadAssignment())

# Retake button logic
if st.session_state["Submitted"]:
    if st.button("Retake Quiz"):
        st.session_state["Attempted"] = 0
        st.session_state["Correct"] = 0
        st.session_state["Wrong"] = 0
        st.session_state["Submitted"] = False
        st.session_state["Answers"] = {}
        st.session_state["IncorrectAnswers"] = {}
        st.experimental_rerun()
