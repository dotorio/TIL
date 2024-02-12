fibo = []
fibo.append(0)
fibo.append(1)
for _ in range(15*10**5-2):
    fibo.append((fibo[-2]+fibo[-1])%10**6)
print(fibo[int(input())%(15*10**5)])