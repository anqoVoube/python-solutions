import string
def alphabet_position(text):
    text = text.replace(" ", '')
    output = []
    a = string.ascii_lowercase
    for i in text:
        if a.find(i.lower()) == -1:
            continue
        else:
            output.append(str(a.find(i.lower()) + 1))
    return " ".join(output)