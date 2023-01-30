from fastapi import APIRouter

from app.words.schemas import Word

router = APIRouter()


@router.get('/words', response_model=list[Word])
def get_words(n: int = 5):
    import json
    import random
    from pathlib import Path

    words_path = Path(__file__).with_name('words.json')

    with open(words_path) as f:
        words = json.load(f)

    word_sample = random.sample(words, k=n)
    return [Word(**i) for i in word_sample]
