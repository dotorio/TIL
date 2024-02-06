def KMP(pattern, target):
    def make_lps():
        # 내 앞에 나와 동일한 패턴이 몇번 나왔는지 세어주는 리스트
        lps = [0] * len(pattern)
        for idx in range(1, len(pattern)): # 0번 인덱스는 앞에 중복되는 값 없음
            if pattern[lps[idx-1]] == pattern[idx]:
                lps[idx] = lps[idx-1] + 1
        lps.insert(0, -1)
        return lps
    

    lps = make_lps()

    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):
        # print(lps[pattern_index])
        # print(target_index, target[target_index], pattern_index, pattern[pattern_index])
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        # 일치하면 => 사실상 항상
        target_index += 1
        pattern_index += 1

        # 패턴의 끝까지 index가 증가했다
        # -> target과 pattern이 일치하지 않는 부분 없어
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False