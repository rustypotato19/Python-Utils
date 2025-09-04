def to_upper(s: str) -> str:
    chars = []
    for c in s:
        code = ord(c)
        if 97 <= code <= 122:
            chars.append(chr(code - 32))
        else:
            chars.append(c)
    return "".join(chars)

def to_lower(s: str) -> str:
    chars = []
    for c in s:
        code = ord(c)
        if 65 <= code <= 90:
            chars.append(chr(code + 32))
        else:
            chars.append(c)
    return "".join(chars)

def capitalize_words(s: str) -> str:
    words = s.split()
    result = []
    for w in words:
        w = to_lower(w)
        if w:
            result.append(to_upper(w[0]) + w[1:])
    return " ".join(result)