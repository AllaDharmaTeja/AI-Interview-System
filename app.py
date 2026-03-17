import os
import pandas as pd
from flask import Flask, render_template, request
from interview_engine import get_question
from scoring_engine import evaluate_answer
from database import save_result

app = Flask(__name__)

# Global variables
current_question = None
correct_answer = None


@app.route("/", methods=["GET", "POST"])
def interview():

    global current_question, correct_answer

    score = None

    # ✅ First load
    if request.method == "GET":
        current_question, correct_answer = get_question()

        if current_question is None:
            current_question = "No questions available. Please add from admin panel."

    # ✅ When user submits answer
    if request.method == "POST":

        user_answer = request.form["answer"]

        score = evaluate_answer(user_answer, correct_answer)

        save_result(current_question, user_answer, score)

        current_question, correct_answer = get_question()

    return render_template(
        "interview.html",
        question=current_question,
        score=score
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        question = request.form["question"]
        answer = request.form["answer"]

        file_path = "dataset/questions.csv"

        # ✅ Create file if it doesn't exist
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["question", "answer"])
            df.to_csv(file_path, index=False)

        # ✅ Read file safely
        df = pd.read_csv(file_path)

        # ✅ Add new question
        new_row = {"question": question, "answer": answer}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # ✅ Save back
        df.to_csv(file_path, index=False)

    return render_template("admin.html")


# ✅ REQUIRED FOR RENDER DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
