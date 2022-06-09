names = ["헐크", "토르", "아이언맨", "배트맨"]

for i in names:
    with open(f"{i}.txt", "w", encoding="utf8")as email_file:
        contents = (f"안녕하세요? {i}님.\n\n"
                    "(주)나도출판 편집자 나코입니다.\n"
                    "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
                    f"{i}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
                    "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n"
                    "좋은 하루 보내세요 ^ ^"
                    "감사합니다.\n\n"
                    "- 나코 드림.\n")
        email_file.write(contents)
