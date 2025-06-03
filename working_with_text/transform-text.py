def remove_new_line(text):
    new_text = []
    for line in text.splitlines():
        if line[-1] == '.':
            sentence = line + "\n"
            new_text.append(sentence)
        else:
            new_text.append(line)
    return " ".join(new_text)
