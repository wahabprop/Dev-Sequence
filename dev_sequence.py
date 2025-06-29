def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_valid(n, last):
    return digit_sum(n) == 6 and (last is None or digit_sum(n - last) == 9)

def a(n_terms):
    seq = []
    k, last = 0, None
    while len(seq) < n_terms:
        val = 9 * k + 6
        if is_valid(val, last):
            seq.append(val)
            last = val
        k += 1
    return seq
