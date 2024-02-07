N, M = map(int, input().split())
wiki = {}
for i in range(1, N+1):
    wiki[i] = input()
    
def get_key(val):
    for key, value in wiki.items():
        if val == value:
            return key
        
for i in range(M):
    Q = input()
    if Q in wiki.values():
        print(get_key(Q))
    else:
        print(wiki[int(Q)])
