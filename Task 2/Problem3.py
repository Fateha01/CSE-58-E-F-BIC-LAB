def rev_complt(pattern):
    mapping ={'A':'T','T':'A','C':'G','G':'C'}
    result= ""
    for char in pattern:
        result =mapping[char] + result
    return result
        print(rev_complt("AAAACCCGGT"))
