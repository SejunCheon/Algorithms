class Word():
    def __init__(self, name, ex1, ex2, answer):
        self.name = name  # 신조어
        self.ex1 = ex1  # 보기1
        self.ex2 = ex2  # 보기 2
        self.answer = answer  # 정답선택

    def show_question(self):  # 질문 내용
        print(f"\"{self.name}\"의 뜻은?")
        print(f"1.{self.ex1}")
        print(f"2.{self.ex2}")

    def check_answer(self, user_input):  # 정답선택 및 확인
        if user_input == self.answer:
            print("정답입니다")
        else:
            print("틀렸습니다")


word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=> ")))
