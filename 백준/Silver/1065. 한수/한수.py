N = int(input()) # 값 받기
cnt = 0 # 한수 세기
for i in range(1, N + 1):
    num = list(map(int, str(i))) # 리스트에 1부터 넣은 값까지를 하나씩 넣는다.
    if i < 100: # 100보다 작은 값은 한수이다.
        cnt += 1
    elif num[0] - num[1] == num[1] - num[2]: # 조건이 1000보다 작은 수 이므로 3자리 숫자이므로, 
        # 첫째자리와 둘째자리 비교하고 다음자리를 비교한 값이 같으면 한수이다. => 3자리 이상 4자리 단위는 공식이 달라질 것 같다.
        cnt += 1
print(cnt)