def solution(cap, n, deliveries, pickups):
    answer = 0
    while True in deliveries or True in pickups:
        dil, col, dil_cnt, col_cnt = 0, 0, 0, 0
        
        for i in range(n-1, -1, -1):
            if deliveries[i] and dil_cnt != cap:
                if not dil:
                    dil = i+1
                if dil_cnt + deliveries[i] <= cap:
                    dil_cnt += deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= cap - dil_cnt
                    dil_cnt = cap
                if dil_cnt == cap or i == 0:
                    next_dil = i+1
            if pickups[i] and col_cnt != cap:   
                if not col:
                    col = i+1
                if col_cnt + pickups[i] <= cap:
                    col_cnt += pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= cap - col_cnt
                    col_cnt = cap
                if col_cnt == cap or i == 0:
                    next_col = i+1
            if (dil_cnt == cap and col_cnt == cap) or i == 0:
                answer += max(dil, col)*2
                if dil_cnt == cap and col_cnt == cap:
                    n = max(next_dil, next_col)
                else:
                    if dil_cnt == cap:
                        n = next_dil
                    elif col_cnt == cap:
                        n = next_col
                    
                break
    return answer