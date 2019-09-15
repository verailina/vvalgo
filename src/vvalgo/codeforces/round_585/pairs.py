def solve(array):
    positif_cnt = [0 for _ in range(len(array))]
    negativ_cnt = [0 for _ in range(len(array))]
    count = 0
    signs = [0 for _ in range(len(array))]
    # 0 - pos, 1 - neg
    current_sign = 0
    for i in range(len(array) - 1, -1, -1):
        if array[i] < 0:
            current_sign = (current_sign + 1) % 2
        signs[i] = current_sign
    print(signs)

    for i in range(len(array) - 1, -1, -1):
        if signs[i] == 0:
            count += 1
        positif_cnt[i] = count
    count = 0
    print(positif_cnt)
    for i in range(len(array) - 1, -1, -1):
        if signs[i] == 1:
            count += 1
        negativ_cnt[i] = count
    print(negativ_cnt)

    pos = 0
    neg = 0
    current_sign = 0
    for i in range(len(array) - 1):
        if array[i] < 0:
            current_sign = (current_sign + 1) % 2

        if current_sign == 0:
            pos += positif_cnt[i + 1]
            neg += negativ_cnt[i + 1]
        else:
            pos += negativ_cnt[i + 1]
            neg += positif_cnt[i + 1]
    return neg, pos


if __name__ == "__main__":
    n = int(input())
    array = [int(x) for x in input().split(" ")]
    res = solve(array)
    print(res[0], res[1])
