# 0. 이분 탐색을 위해 리스트를 정렬시킨다.
# 1. 탐색을 할 때 매번 최소값, 최대값 인덱스를 구한다.
# 2. 탐색은 타깃 - 찾을 요소을 기준으로 삼는다. (이는 타깃으서 가장 가까운 값을 찾기 위함) 가장 가까운 값은 result에 넣어서 마지막에 min(result)
# 3. 이분 탐색은 총 N번 이루어 진다.

# 내가 만든 방법에는 C가 짝수일 때 답이 틀리는 한계가 있다.
####################################################################

# x축으로 정렬했을 때, x[1], ... , x[n]인 집들이 있다고 해 봅시다. 단 임의의 i<j에 대해, x[i]<=x[j]겠죠. (a)
# x[1] + L이상인 최초의 지점이 q라고 해 봅시다. 즉, x[1] + L <= x[q]이고, x[q-1] < x[1]+L인 셈이죠. (b)
# 그렇다면, x[2] + L이상인 최초의 지점이 t일 때, q<=t일 수 밖에 없습니다. 왜냐면, x[1] <= x[2]이기 때문입니다.

# L이라는 친구가 커질수록 설치할 수 있는 공유기의 갯수가 작아진다는 것 또한 증명할 수 있습니다.

# L1<L2라고 한다면

#x[1] + L1 = u<t = x[1] + L2라고 놓으시고, 천천히 대치법으로 증명해 보시면 좋을 듯 싶습니다.

#f(L)을 가장 인접한 두 공유기의 거리가 L일 때, 설치할 수 있는 최대 공유기 갯수라고 한다면

#f(x)는, x가 커짐에 따라 단조 증가, 혹은 단조 감소 함수이므로 이분 탐색을 적용할 수 있습니다.

# 2110 질문 - chogahui05

def install(distance):  # 거리로 최대 설치할 수 있는 공유기 갯수를 구하는 함수.
    count = 1
    tmp = lst[0]
    for i in range(1, N):
        if lst[i] - tmp >= distance:
            tmp = lst[i]
            count += 1
    return count
        
def binary_search(target):  # target 만큼 공유기를 설치하는 거리중 최대값을 구하는 함수.
    start = 1  # 1부터 (최소 거리)
    end = lst[-1] - lst[0] # (최대 거리) 까지
    while start <= end:
        mid = (start + end) // 2
        instal = install(mid)
        if instal >= target:
            start = mid + 1
        elif instal < target:
            end = mid - 1
    return end

N, C = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])
end = binary_search(C)
print(end)
