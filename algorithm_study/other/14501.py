N = int(input())
Time = []
Pay = []
Pay_list = []
for _ in range(N):
    T, P = map(int, input().split())
    Time.append(T)
    Pay.append(P)
def Make_pay(i_, s_):
    if i_ + Time[i_] > N:
        Pay_list.append(s_)
    else:
        s_ += Pay[i_]
        i_ += Time[i_]
        if i_ == N:
            Pay_list.append(s_)
        else:

            for _ in range(i_, N):

                return Make_pay(i_, s_)

for i in range(N):

    Sum_pay = 0
    Make_pay(i, Sum_pay)
    
print(max(Pay_list))