# Find Maximum Score of substring with next alphabet

def max_score_with_one_change(data: str) -> int:
    def compute_score(s):
        score = len(s)  # 1 point per character
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i+1])) <= 1:
                score += 1
        return score

    max_score = compute_score(data)

    for i in range(len(data)):
        original_char = data[i]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c == original_char:
                continue
            new_data = data[:i] + c + data[i+1:]
            score = compute_score(new_data)
            max_score = max(max_score, score)

    return max_score

print(max_score_with_one_change("abez"))