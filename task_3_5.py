from random import randint


def get_jokes(count):
    joke = []
    new_joke_2 = []
    count = int(count)
    for index in range(count):
        num = randint(0, len(nouns)-1)
        joke.append(nouns[num])
        nouns.pop(num)
        num = randint(0, len(adverbs)-1)
        joke.append(adverbs[num])
        adverbs.pop(num)
        num = randint(0, len(adjectives)-1)
        joke.append(adjectives[num])
        adjectives.pop(num)
        new_joke = ' '.join(joke)
        joke.clear()
        new_joke_2.append(new_joke)
    print(new_joke_2)


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

number = int(input("Сколько шуток сгенерировать (максимум 5)? "))
get_jokes(number)
