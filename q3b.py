def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a, b = a[2:], b[2:]
    res = ""
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        val_a = int(a[i]) if i >= 0 else 0
        val_b = int(b[j]) if j >= 0 else 0    
        total = val_a + val_b + carry
        res = str(total % 2) + res
        carry = total // 2
        i -= 1
        j -= 1
        idx = 0
    while idx < len(res) - 1 and res[idx] == '0':
        idx += 1   
    return "0b" + res[idx:]
