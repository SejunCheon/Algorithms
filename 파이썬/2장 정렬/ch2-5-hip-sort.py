# 정렬할 배열
from string import printable


a = [5,2,7,3,6,1,4]

def heapify(arr, idx, n):
    m_idx = idx # 가장 큰 index
    l = 2 * idx + 1    # 왼쪽 index
    r = 2 * idx + 2    # 오른쪽 index
    
    if l < n and arr[m_idx] < arr[l]: # 왼쪽자식 노드가 index보다 작을 때
        m_idx = l
    if r < n and arr[m_idx] < arr[r]:
        m_idx = r
    if m_idx != idx: # 처음에 m_idx를 idx로 초기화했기에 바뀌게 되면
        arr[idx], arr[m_idx] = arr[m_idx], arr[idx]
        print(arr)
        return heapify(arr, m_idx, n)
    
          

def heap_sort(arr):
    print('변경 전 힙 : ', arr)
    n = len(arr) # 7

    for i in range(n//2 -1, -1, -1): # // 은 나머지가 아닌 몫을 반환하는 연산자
        heapify(arr, i, n)
    print('변경 후 힙 : ', arr)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i],arr[0] # 배열의 첫 숫자와 마지막 숫자 교환
        heapify(arr, 0, i)
    return arr
        
print(heap_sort(a))
