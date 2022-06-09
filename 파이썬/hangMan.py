# import random은 random.?? 을 사용해야하고
# from random import *은 모듈을 사용할 때 random. 을 사용하지 않아도 된다.
from random import *

# 리스트에 3개이상의 단어를 추가
words = ["apple", "banana", "orange"]

# 리스트에서 랜덤으로 1개의 단어를 선택
word = choice(words)
print("answer :", word)

# 사용자로부터 지금까지 입력받은 모든 알파벳
letters = ""

# 단어의 길이에 맞게 밑줄 출력
while True:
    succeed = True
    print()
    for w in word:  # a p p l e
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success!")
        break

    letter = input("Input letter > ")  # 사용자 입력 받기
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
        continue
    else:
        print("Wrong")
        continue

    break
