def brute_force(pattern, target):
    # 둘다 첫 조사 시작지점 0번에서 시작
    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):
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