def boyer_moore(pattern, target):
    # lps = {key: value for idx in range(len(pattern))} # 스킵 가능한 범위 기록
    lps = {pattern[idx]: len(pattern)-1 - idx for idx in range(len(pattern))} # 스킵 가능한 범위 기록
    pattern_index = len(pattern)
    target_index = 0

    while target_index <= len(target) - pattern_index:
        for p_idx in range(pattern_index -1, -1, -1):
            if target[target_index + p_idx] != pattern[p_idx]:
                # target_index += lps[target[target_index + p_idx]]
                target_index += lps.get(target[target_index + p_idx], len(pattern))
                break # 틀렸으니까 p_idx 다시 len(pattern) - 1 되도록 조사종료
        else:
            return True
    return False