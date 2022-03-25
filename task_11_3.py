class OwnError(Exception):

    def __init__(self, user_namber):
        self.user_namber = user_namber

def number(str):
    if str.isdigit():
        return str
    else:
        try:
            float(str)
            return str
        except ValueError:
            raise OwnError(f'Error: {str} Введите число')

user_namber = ''
i = 1
list = []
print("Введите число, прекращение 'stop'")
while user_namber != 'stop':
    try:
        user_namber = input(f"{i}: ")
        list.append(number(user_namber))
        i += 1
    except OwnError as e:
        if user_namber != 'stop':
            print(e.user_namber)

print(f"Результат:\n{list}")

