A = list(range(1,13))
numbers = int(input())
for number in range(numbers):
    N, K = list(map(int, input().split()))

    count = 0
    for i in range(1<<len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(A[j])

        subset_sum = sum(subset)
        if subset_sum == K and len(subset) == N:
            count += 1

    print("#{} {}".format(number+1, count))