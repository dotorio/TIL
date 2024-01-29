import math
day, night, tree = map(int, input().split())
days = 1 + math.ceil((tree - day) / (day - night))
print(days)