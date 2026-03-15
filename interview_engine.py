import pandas as pd

data = pd.read_csv("dataset/questions.csv")

def get_question():

    row = data.sample(1).iloc[0]

    return row["question"], row["answer"]