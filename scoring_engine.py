from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_answer(user_answer, correct_answer):

    embeddings = model.encode([user_answer, correct_answer])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    score = similarity[0][0] * 100

    return round(score,2)