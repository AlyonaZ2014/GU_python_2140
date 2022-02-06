name_tuple = ('Иван', 'Мария', 'Петр', 'Илья')
print(type(name_tuple))   #кортеж
print(name_tuple)


def thesaurus(*names_tuple):
    dict_name = {}
    for name in names_tuple:
        key = name[0]
        if key not in dict_name:
            dict_name[key] = []
            dict_name[key].append(name)
    return dict_name
print(thesaurus(*name_tuple))









