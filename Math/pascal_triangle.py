def pascal_triangle(n: int) -> list[int]:
    if n < 0:
        raise Exception("n must be an integer larger than one")

    yield [1]

    row = [1]

    for _ in range(n):
        temp = [1]
        for i in range(len(row)-1):
            temp.append(row[i] + row[i+1])
        temp.append(1)
        row = temp

        yield row


if __name__ == "__main__":
    for i, row in enumerate(pascal_triangle(24)):
        print(i, " ".join(map(lambda x: str(x).center(8), row)).center(256))
