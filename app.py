import os
from flask import Flask, render_template, request
from interview_engine import get_question
from scoring_engine import evaluate_answer
from database import save_result

app = Flask(__name__)

current_question = None
correct_answer = None

@app.route("/", methods=["GET","POST"])
def interview():

    global current_question, correct_answer

    score = None

    if request.method == "GET":
        current_question, correct_answer = get_question()

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


@app.route("/admin", methods=["GET","POST"])
def admin():

    import pandas as pd

    if request.method == "POST":

        question = request.form["question"]
        answer = request.form["answer"]

        df = pd.read_csv("dataset/questions.csv")

        new_row = {"question":question,"answer":answer}

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv("dataset/questions.csv", index=False)

    return render_template("admin.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
