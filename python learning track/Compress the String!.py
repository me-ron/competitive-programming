def compress_string(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(f'({count}, {s[i]})')
        i += 1
    return ' '.join(result)
if __name__ == '__main__':
    s=list(input())
    print(compress_string(s))
