def thesaurus(args, length):
    my_tuple = {args[0][0]: args[0]}
    for index in range(length):
        tuple_names = {args[index][0]: args[index]}
        my_tuple.update(tuple_names)
        for jndex in range(index):
            if args[index][0] == args[jndex][0]:
                tuple_names = {args[index][0]: [args[index],  args[jndex]]}
                my_tuple.update(tuple_names)
    print("{")
    for key, value in my_tuple.items():
        print(f'   "{key}": "{value}"')
    print("}")


def thesaurus_adv(args, length):
    tuple_surname = {}
    tuple_name = {}
    for index in args:
        name = args
        surname = index.split(' ')
        surname_key = {surname[-1][0]: name}
        tuple_surname.update(surname_key)
        """
    for index_1 in range(length):
        for key in tuple_surname.keys():
            for index in args:
                surname = index.split(' ')
                if key == surname:
                    tuple_names = {args[index_1][0]: args[index_1]}
                    tuple_name.update(tuple_names)
                    for jndex in range(index_1):
                        if args[index_1][0] == args[jndex][0]:
                            tuple_names = {args[index_1][0]: [args[index_1], args[jndex]]}
                            tuple_name.update(tuple_names)"""
    print(tuple_surname)

"""
count = input("Сколько имен будет в списке? ")
list_names = []
for i in range(int(count)):
    list_names.append(input("Введите имена: "))
thesaurus(list_names, int(count))
"""

count = input("Сколько имен будет в списке? ")
list_names = []
for i in range(int(count)):
    list_names.append(input("Введите имена: "))
thesaurus_adv(list_names, int(count))
