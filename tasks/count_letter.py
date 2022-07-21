def count_letter(words: list, letter: str):
    counter = 0
    for word in words:
        if letter in word:
            counter += 1
    return counter

words = ['python', 'c++', 'c', 'scala', 'java']
letter = 'c'
print(count_letter(words, letter))