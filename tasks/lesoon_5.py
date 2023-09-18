def multiplication_table(n):
    for i in range(n+1):
        row = []
        for j in range(n+1):
            row.append(str(i*j))
        print(" ".join(row))
