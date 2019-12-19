def unique(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True