import keyword
words_to_check = ["for", "print", "break", "done", "bad"]
for word in words_to_check:
    if keyword.iskeyword(word):
        print(f"{word} jest słowem kluczowym w Pythonie.")
    else:
        print(f"{word} nie jest słowem kluczowym w Pythonie.")