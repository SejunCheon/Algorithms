# 정렬할 배열
a = [6, 1, 7, 8, 9, 3, 5, 4, 2]

def select_sort(arr):
    # 배열의 길이만큼 반복문 실행
    for i in range(len(arr) -1): 
        # 가장 작은 값 변수에 i 초기화
        min_idx = i
        for j in range(i + 1, len(arr)) :
            # 만약 다음 인덱스가 가장 작은 값 변수보다 작을 때 
           if arr[j] < arr[min_idx]:
               # 값 변경
               arr[j], arr[min_idx] = arr[min_idx], arr[j]
               print(arr)
    return arr


print(a)
print(select_sort(a))

    