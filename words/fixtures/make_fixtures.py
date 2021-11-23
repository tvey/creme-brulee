import json

from data import (
    verbs,
    nouns,
    adjectives,
    expressions_1,
    expressions_4,
    expression_types,
)


def dump_to_file(data, filename):
    with open(f'{filename}.json', 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=4)


def make_words():
    words = verbs + nouns + adjectives
    word_fixture = []

    for i, w in enumerate(words, 1):
        word = {}
        word['model'] = 'words.word'
        word['pk'] = i
        word['fields'] = {}
        word['fields']['content'] = w
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

    dump_to_file(word_fixture, 'words')


def make_expression_types():
    e_type_fixture = []

    for i, e_type in enumerate(expression_types, 1):
        et = {}
        et['model'] = 'words.expressiontype'
        et['pk'] = i
        et['fields'] = {}
        et['fields']['e_type'] = e_type
        e_type_fixture.append(et)

    dump_to_file(e_type_fixture, 'expression_types')


def make_expressions():
    expressions = expressions_1 + expressions_4
    expression_fixture = []

    for i, expr in enumerate(expressions, 1):
        e = {}
        e['model'] = 'words.expression'
        e['pk'] = i
        e['fields'] = {}
        e['fields']['content'] = expr
        e_type = []
        if expr in expressions_1:
            e_type.append(1)
        if expr in expressions_4:
            e_type.append(4)
        e['fields']['e_type'] = e_type
        expression_fixture.append(e)

    dump_to_file(expression_fixture, 'expressions')


make_words()
make_expression_types()
make_expressions()