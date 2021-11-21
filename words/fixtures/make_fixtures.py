import json

verbs = ['играть', 'прыгать', 'смотреть', 'крикнуть', 'брать']
nouns = ['время', 'край', 'друг', 'правда', 'гречка', 'алгоритм']
adjectives = ['трудный', 'красный', 'хороший', 'интересный', 'пряный']
words = verbs + nouns + adjectives


word_fixture = []

for i, w in enumerate(words, 1):
    word = {}
    word['model'] = 'words.word'
    word['pk'] = i
    word['fields'] = {}
    word['fields']['word'] = w
    pos = ''
    if w in verbs:
        pos = 'verb'
    elif w in nouns:
        pos = 'noun'
    elif w in adjectives:
        pos = 'adjective'
    word['fields']['part_of_speech'] = pos
    word['fields']['difficulty'] = 0
    word_fixture.append(word)


with open('words.json', 'w', encoding='utf-8') as fh:
    json.dump(word_fixture, fh, ensure_ascii=False, indent=4)
