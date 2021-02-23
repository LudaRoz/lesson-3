def num_translate(word):
    key = ''
    for key, value in vocabulary.items():
        if word == key:
            print(f"{value}")
            break
    if word != key:
        print("None")


def num_translate_adv(word):
    key = ''
    for key, value in vocabulary.items():
        if word == key:
            print(f"{value}")
            break
        elif word.lower() == key:
            print(f'{value.title()}')
            break
    word = word.lower()
    if word != key:
        print("None")


vocabulary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

print('Простой перевод')
user_word = input("Введите словом число, которое хотите перевести: ")
num_translate(user_word)

print('-------')

print('Продвинутый перевод')
user_word = input("Введите словом число, которое хотите перевести: ")
num_translate_adv(user_word)
