import re
def email_parse(address):
    try:
        parsed = re.findall(r"(?P<username>([a-z0-9_-]+\.)*[a-z0-9_-].+)@(?P<domain>[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})", address)
        if not parsed:
            raise ValueError()
    except ValueError:
        name = 'wrong email {}'.format(str(address))
        raise ValueError(name)

    else:
        rez = re.findall(r"(?P<username>([a-z0-9_-]+\.)*[a-z0-9_-].+)@(?P<domain>[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})", address)
        rez = re.search(r"(?P<username>([a-z0-9_-]+\.)*[a-z0-9_-].+)@(?P<domain>[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6})", address)
        # print(f"{adress[rez.span()[0]:rez.span()[1]]}")
        print(f"{rez.groupdict()} ")
    return

print(email_parse('someone@geekbrains.ru'))