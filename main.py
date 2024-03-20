def binary(rows: int) -> list:
    bin = []
    if rows <= 1:
        bin = [[0], [1]]
        return bin
    min_binary = binary(rows - 1)
    for i in range(len(min_binary)):
        row = [0]
        row.extend(min_binary[i])
        bin.append(row)
    for i in range(len(min_binary)):
        row = [1]
        row.extend(min_binary[i])
        bin.append(row)
    return bin


def build_code(file) -> list:
    rows = len(file)
    words = binary(rows)
    code_words = []
    for i in range(len(words)):
        word = words[i]
        code_word = []
        for j in range(len(file[0])):
            bit = 0
            for k in range(len(word)):
                bit ^= word[k] * file[k][j]
            code_word.append(bit)
        code_words.append(code_word)
    return code_words


def main(file_name) -> None:
    file = open(file_name + '.txt', 'r').read().split('\n')
    header = file[0].split(' ')
    file = file[1:]
    n = int(header[0])
    m = int(header[1])
    for i in range(n):
        file[i] = file[i].split(' ')
        file[i] = [int(x) for x in file[i]]
    print(file)
    print("Размерность кода: ", n)
    print("Количество кодовых слов: ", pow(2, n))

    code_words = build_code(file)

    count = m + 1
    for code in range(len(code_words)):
        for i in range(code + 1, len(code_words)):
            cou = 0
            for j in range(len(code_words[i])):
                if code_words[code][j] != code_words[i][j]:
                    cou += 1
            if cou < count:
                count = cou

    print("Минимальное кодовое расстояние: ", count)


if __name__ == '__main__':
    main('test')
    main('test1')
    main('test2')
    main('test3')
    main('test4')
