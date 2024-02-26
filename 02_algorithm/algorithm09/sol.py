import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, T = map(int, input().split())
    cards = list(range(1, N+1))
    for _ in range(T):
        cards = cards[int(N*0.63)+1:] + cards[:int(N*0.63)+1]
        a, b = 0, (N+1)//2
        new_cards = []
        for turn in range(N):
            if turn % 2 == 0:
                new_cards.append(cards[a])
                a += 1
            else:
                new_cards.append(cards[b])
                b += 1
        cards = new_cards
    print(f'#{tc} {" ".join(map(str, cards))}')
