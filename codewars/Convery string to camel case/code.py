def to_camel_case(text):
    first = []
    delete = []
    for i in text:
        first.append(str(i))
    if len(text) == 0:
        return ''
    else:
        for i in range(len(first)):
            if first[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                delete.append(i)
        for j in range(len(delete)):
            delete[j] = delete[j] - j
        for j in delete:
            del first[j]
        for i in delete:
            first[i] = first[i].upper()

    return ''.join(first)