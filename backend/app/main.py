from datetime import datetime, timedelta

from fastapi import FastAPI

from app.schemas import Word

app = FastAPI()


@app.get('/words', response_model=list[Word])
def register(n=5):
    import json
    import random

    with open('app/words.json') as f:
        words = json.load(f)

    word_sample = random.sample(words, k=n)
    return [Word(**i) for i in word_sample]
