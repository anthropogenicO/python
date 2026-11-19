word = "YouWillSolveThePracticeProblemsOfChapterEight"

new_sentence = ""
i = 0
while i < len(word):
    letter = word[i]

    if i == 0:
        new_sentence += letter
    elif letter.isupper():
        new_sentence += " " + letter.lower()
    else:
        new_sentence += letter

    i += 1
print(new_sentence)