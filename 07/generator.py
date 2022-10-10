# здесь работал с файлом не через контектсный менеджер, чтобы не было повторения кода
# те была бы одна ветка в случае переданного пути файла, вторая в случае файлового объекта
def generator(file, words):
    if isinstance(file, str):
        file = open(file, 'r', encoding = 'utf-8')
    for line in file:
        line = line.strip()
        line_preprocessed = line.lower().split()
        for word in words:
            if word in line_preprocessed:
                yield line
    file.close()
