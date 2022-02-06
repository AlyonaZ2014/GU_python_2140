nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
user_namber = int(input('Введите количество шуток: '))


def get_jokes(t):
    from random import choice
    for noun in range(t):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        jokes = f'{noun} {adverb} {adjective}'
        print(jokes)

get_jokes(t = user_namber)

