# for seat in range(1, 21):
#     if seat % 2 == 1:
#         print("A" + str(seat), end=" ")

for seat in range(1, 21)[::2]: # 2 칸씩 건너 뛰어서
    print("A" + str(seat), end=" ")
