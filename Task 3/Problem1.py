
from itertools import product

def solve(text, k, d):
    best = {}

    for pattern in [''.join(p) for p in product('ACGT', repeat=k)]:
        count = 0
        for i in range(len(text) - k + 1):
            mismatches = sum(a != b for a, b in zip(text[i:i+k], pattern))
            if mismatches <= d:
                count += 1
        best[pattern] = count

    max_count = max(best.values())      
    print(' '.join(p for p, c in best.items() if c == max_count))

solve("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
