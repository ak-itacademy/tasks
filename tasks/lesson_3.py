# Задание 3: Leson 3


sentence = input("Введите предложение")
words = sentence.split()
the_longest_word = max(words, key=len)
print(the_longest_word)


srtring = input("Введите строку")
srtring = srtring.replace(" ", "")
no_replay = "".join(set(srtring))
print(no_replay)


string = input()
upper_count = 0
lower_count = 0
for char in string:
    if char.isalpha() and char.isascii():
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
print(upper_count)
print(lower_count)
