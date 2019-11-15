from keyword import iskeyword


def contains_keyword(*args):
    for arg in args:
        if iskeyword(arg):
            return True
    else:
        return False


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol"))
print(contains_keyword("four", "flour", "flower", "for"))
