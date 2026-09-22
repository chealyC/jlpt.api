from fastapi import FastAPI
import vocab
import kanji
import questions

app = FastAPI()

@app.get("/vocabulary/{level}")
def get_vocabulary(level: str):
    results = vocab.get_vocab(level)

    return results

@app.get("/kanji/{level}")
def get_kanji(level: str):
    results = kanji.get_kanji(level)

    return results

@app.get("/questions/{level}")
def get_questions(level: str):
    results = questions.get_questions(level)

    return results