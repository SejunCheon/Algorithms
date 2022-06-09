# 프로그래머스 Lv1 수박수박수

# def solution(n):
#     answer = ""
# for i in range(n):
#     if i % 2 == 0:
#         answer += "수"
#     else:
#         answer += "박"
# return answer

# print(solution(3))
# print(solution(10))

# def solution1(n):
#     return ('수박' * n) [:n]

# print(solution1(3))

# 프로그래머스 Lv1 평균구하기
# def solution(arr):
#     return sum(arr)/len(arr)


# arr = [5, 5]
# print(f"평균값: {solution(arr)}")

# 완주하지 못한 선수
def solution(particpant, completion):
    p = sorted(particpant)  # 참가자 선수 명단
    c = sorted(completion)  # 완주한 선수 명단
    for pp, cc in zip(p, c):
        if pp != cc:
            return pp

    return p[-1]  # 다 같으면 맨 마지막에 정렬된 값이 나온다.


particpant = ["c", "a", "b", "d", ]
completion = ["a", "b", "c"]
print(solution(particpant, completion))
