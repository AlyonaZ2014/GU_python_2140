number_dict = {'one':'один',
             'two':'два',
             'three':'три',
             'four':"четыре",
             'five':'пять',
             'six':'шесть',
             'seven':'семь',
             'eight':'восемь',
             'nine':'девять',
             'ten':'десять'}
user_namber = input('Введите число на egl: ').lower()
def num_translate(user_namber):
    eng = number_dict.get(user_namber)
    if eng:
        return number_dict.get(user_namber)
print(num_translate(user_namber))
