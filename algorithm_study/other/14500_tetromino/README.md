## 테트로미노
### 20240210

1. 노가다성이 있는 문제

    그래도 제대로 풀었다고 생각했는데

    틀렸다고 해서 당황했다

2. 행렬을 제대로 회전했다고 생각했는데

    new_arr = list(map(*arr))

    이 방식은 행렬을 회전시키는 것이 아니라
    
    전치 행렬을 만드는 것이었다

    new_arr = list(map(*arr[::-1]))

    이렇게 적어야 제대로 회전된다

    맞았다 처음 맞은 골드 문제 기쁘다!