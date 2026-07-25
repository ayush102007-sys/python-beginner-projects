"""
This project steps up the functional structure by introducing  — smaller functions that perform
Helper Functions-> single specialized jobs (like cleaning input or scoring a single question) that get called inside a master function.
"""

"""
📝 QUIZ ENGINE ARCHITECTURE
       
 [ Question Bank (List of Dicts) ] ──► [ Helper 1: clean_text() ]
                                   ──► [ Helper 2: evaluate_answer() ]
                                   ──► [ Helper 3: calculate_grade() ]
"""

"""
Automated Quiz & Scoring Engine
Uses modular helper functions to handle text normalization, answer evaluation, and grading.
"""

quiz_data = [
    {
        "question": "Which Python library is primarily used for numerical arrays?",
        "options": ["A) Pandas", "B) NumPy", "C) Matplotlib", "D) Requests"],
        "answer": "B"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for integer floor division in Python?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) define", "C) def", "D) function"],
        "answer": "C"
    },
    {
        "question": "Which Python library is primarily used for numerical arrays?",
        "options": ["A) Pandas", "B) NumPy", "C) Matplotlib", "D) Requests"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for integer floor division in Python?",
        "options": ["A) /", "B) //", "C) %", "D) **"],
        "answer": "B"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A) .python", "B) .pt", "C) .py", "D) .pyt"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Set", "D) Tuple"],
        "answer": "D"
    },
    {
        "question": "What is the output of len('Python 3')?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C"
    },
    {
        "question": "Which built-in function returns the total number of items in a list?",
        "options": ["A) count()", "B) len()", "C) size()", "D) total()"],
        "answer": "B"
    },
    {
        "question": "Which method is used to add an item to the end of a list?",
        "options": ["A) append()", "B) push()", "C) insert()", "D) add()"],
        "answer": "A"
    },
    {
        "question": "How do you start a single-line comment in Python?",
        "options": ["A) //", "B) /*", "C) #", "D) <!--"],
        "answer": "C"
    },
    {
        "question": "What will bool('') evaluate to in Python?",
        "options": ["A) True", "B) False", "C) None", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation (power) in Python?",
        "options": ["A) ^", "B) **", "C) pow", "D) *"],
        "answer": "B"
    },
    {
        "question": "Which function converts a string or number to a floating-point value?",
        "options": ["A) str()", "B) int()", "C) float()", "D) double()"],
        "answer": "C"
    },
    {
        "question": "What collection type uses key-value pairs in Python?",
        "options": ["A) List", "B) Tuple", "C) Set", "D) Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which statement is used to exit a loop prematurely?",
        "options": ["A) continue", "B) exit", "C) break", "D) stop"],
        "answer": "C"
    },
    {
        "question": "Which function removes whitespace from both ends of a string?",
        "options": ["A) strip()", "B) clean()", "C) trim()", "D) cut()"],
        "answer": "A"
    },
    {
        "question": "What is the index of the first element in a Python list?",
        "options": ["A) 1", "B) -1", "C) 0", "D) 2"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["A) catch", "B) except", "C) error", "D) handle"],
        "answer": "B"
    },
    {
        "question": "Which built-in function returns an enumerated object containing index and value?",
        "options": ["A) zip()", "B) enumerate()", "C) range()", "D) index()"],
        "answer": "B"
    },
    {
        "question": "What keyword is used to import a module into your Python script?",
        "options": ["A) include", "B) import", "C) require", "D) load"],
        "answer": "B"
    },
    {
        "question": "What value does a Python function return by default if no return statement is executed?",
        "options": ["A) 0", "B) False", "C) None", "D) Empty string"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to skip the rest of the current loop iteration and move to the next one?",
        "options": ["A) break", "B) pass", "C) continue", "D) skip"],
        "answer": "C"
    },
    {
        "question": "Which method removes and returns the last item from a list?",
        "options": ["A) remove()", "B) pop()", "C) delete()", "D) discard()"],
        "answer": "B"
    }
]


def clean_text(text):
    return text.strip().lower()


def evaluate_answer(user_ans, correct_ans):
    # Cleans both inputs and returns True or False
    return clean_text(user_ans) == clean_text(correct_ans)


def calculate_grade(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage >= 90:
        return f"{percentage:.1f}% -> A (Outstanding!)"
    elif percentage >= 75:
        return f"{percentage:.1f}% -> B (Good!)"
    elif percentage >= 50:
        return f"{percentage:.1f}% -> C (Pass)"
    else:
        return f"{percentage:.1f}% -> F (Needs Improvement)"


def run_quiz(question_bank):
    score = 0
    total_questions = len(question_bank)

    for ques_no, item in enumerate(question_bank, 1):
        print(f"\nQuestion [{ques_no}/{total_questions}]: {item['question']}")
        print("Options:", " | ".join(item["options"]))

        user_ans = input("Give your answer (A, B, C, or D): ")

        if clean_text(user_ans) in ["a", "b", "c", "d"]:
            # Evaluate using helper function
            if evaluate_answer(user_ans, item["answer"]):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect! The correct answer was: {item['answer']}")
        else:
            print("⚠️ Invalid option selected! Question marked incorrect.")

        print(f"Current Score: {score}/{total_questions}")

    # Final Grade Summary
    grade_report = calculate_grade(score, total_questions)
    print("\n" + "=" * 30)
    print("      FINAL QUIZ REPORT      ")
    print("=" * 30)
    print(f"Final Score : {score}/{total_questions}")
    print(f"Grade       : {grade_report}")
    print("=" * 30)
    print("Thanks for trying the quiz! :)")


# Run Engine
run_quiz(quiz_data)

