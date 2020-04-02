numbers = int(input())

for number in range(numbers):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = pizza[:N] #처음부터 N개까지 화덕에 넣기(큐!!!!)
    oven_index = list(range(N)) # 이러면 들어간 피자 1~N개의 인덱스가 저장됨
    next_pizza_index=N

    result = 0 # 첫번째부터 순서대로 빼서 몇번피잔지 알아낼거야
    while True:
        for i in range(N):
            temp_chesse = oven[i]//2 # 오븐 입구에서 딱봤을 때 치즈가 녹은 양(한바퀴를 돌았다고 하고 시작)
            if temp_chesse == 0: # 본론부터! 치즈가 다 녹았으면 빼야지
                if next_pizza_index < M: # 안익은 피자 넣어야하는데 익은피자가 피자갯수 보다 작으면
                    oven[i] = pizza[next_pizza_index] # 큐에다가 새로운 안익은 피짜 넣어줘
                    result = oven_index[i]+1 # 오븐에 넣은 피자중에 익은 친구빼서 인덱스+1(몇번째피자(0은 피자 없어))을 result에 넣어줘
                    oven_index[i] = next_pizza_index # 이제 익어서 뺀 친구 자리에 시로운 안익은 친구를 넣어주는데 이때 헷갈리지 않도록 인덱스 써주기
                    next_pizza_index += 1 # 이제 새로운 피자는 넣었으니 다시 새로운 친구를 넣기 위해서 +1해주기
                else:
                    oven[i] = 0 #피자M개를 다 넣었으면 oven[i]에는 아무것도 안들어감(피자없어=0)
                    if oven_index[i] != -1: # 군데 비어있는 오븐칸중에 피자가 있는 칸걸리면
                        result = oven_index[i]+1#(이때 뺀피자가 result)
                    oven_index[i] = -1 # 초과된 피자(M~)는 -1의 값 부여
            else: #치즈가 덜 녹았으면
                oven[i] = temp_chesse #그대로 치즈만 절반 준다.
        if sum(oven) == 0: # 모든 오븐칸이 비었다면?
            break
    print('#{} {}'.format(number+1, result))

