import os
import pandas as pd
from flask import Flask, render_template, request
from interview_engine import get_question
from scoring_engine import evaluate_answer
from database import save_result
app = Flask(__name__)
current_question = None
correct_answer = None
FILE_PATH = "dataset/questions.csv"
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
if not os.path.exists(FILE_PATH):
    df = pd.DataFrame(columns=["question", "answer"])
    df.to_csv(FILE_PATH, index=False)
@app.route("/", methods=["GET", "POST"])
def interview():
    global current_question, correct_answer
    score = None
    if request.method == "GET":
        current_question, correct_answer = get_question()
        if current_question is None:
            current_question = "No questions available. Please add from admin panel."
    elif request.method == "POST":
        user_answer = request.form.get("answer", "")
        score = evaluate_answer(user_answer, correct_answer)
        save_result(user_answer, correct_answer, score)
        current_question, correct_answer = get_question()
        if current_question is None:
            current_question = "No questions available. Please add from admin panel."
    return render_template("interview.html", question=current_question, score=score)
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = request.form.get("answer", "")
        df = pd.read_csv(FILE_PATH)
        new_row = {"question": question, "answer": answer}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(FILE_PATH, index=False)

    return render_template("admin.html")
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
