from random import *

words = ["naver", "batman", "superman", "ironman"]
word = choice(words)
print("answer : " + str(word))

# 빈문자열 (지금까지 입력된 알파벳)
letters = ""

while True:
    succeed = True

    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False

    print()
    if succeed:
        print("Success!")
        break

    letter = input("문자열 하나 입력 > ")

    if letter not in letters:
        letters += letter

    if letter in word:
        print("Currect")
        continue
    else:
        print("Wrong")
        continue

    break
