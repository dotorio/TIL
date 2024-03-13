def f(buy, i, j):
    for k in range(10, 50, 10):
        if k >= users[i][0]:
            buy[i] += emoticon[j]*(1-k*0.01)
            if j == len_emoticon-1:
                if i == len_users-1:
                    join, bene = 0, 0
                    for l in range(len_users):
                        if buy[l] >= users[l][1]:
                            join += 1
                        else:
                            bene += buy[l]
                    answer.append([join, bene])
                    return
                else:
                    f(buy, i+1, 0)
            else:
                f(buy, i, j+1)
        else:
            if j == len_emoticon-1:
                if i == len_users-1:
                    join, bene = 0, 0
                    for l in range(len_users):
                        if buy[l] >= users[l][1]:
                            join += 1
                        else:
                            bene += buy[l]
                    answer.append([join, int(bene)])
                    return
                else:
                    f(buy, i+1, 0)
            else:
                f(buy, i, j+1)


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticon = [1300, 1500, 1600, 4900]
answer = []
len_users, len_emoticon = len(users), len(emoticon)
buy = [0]*(len_users)
f(buy, 0, 0)
answer.sort()
print(answer[-1])