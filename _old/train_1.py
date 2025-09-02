def check_wording(word: str) -> bool:
    list_default = []
    list_modify = []
    word_for_check_low = word.lower()

    for i in word_for_check_low:
        list_default.append(i)

    for i in list_default[::-1]:
        list_modify.append(i)

    return True if list_default == list_modify else False

def check_is_palindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]


print(check_wording('Топот'))
print(check_is_palindrome('Топот'))

word = 'тикет'
print(word[-1])

