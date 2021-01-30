def is_matched(expression):
    """
    Проверить валидность расстановки скобочек в выражении.
    Скобки могут быть всех трех видов - ()[]{}.
    На вход программа или функция должна принимать строку, а на выходе ответить правильно ли расставлены скобочки в ней.
    Те есть открывающиеся скобочки корректно закрываются скобочкой того же вида.

    Например:
    "([])" - true
    "{[(]}"- false
    """
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in expression:
        if letter in opening:
            queue.append(mapping[letter])

        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue


if __name__ == '__main__':
    t = input()
    print(is_matched(t))
