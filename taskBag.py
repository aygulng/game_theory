def knapSack(A, a, c, n):

    W = [[0 for x in range(A + 1)] for x in range(n + 1)]

    # проходим по всем вещам
    for i in range(n + 1):

        for w in range(A + 1):
            # нулевую строку и столбец заполняем нулями
            if i == 0 or w == 0:
                W[i][w] = 0
            elif a[i - 1] <= w:
                # если предмет влезает в рюкзак,рассчитаем цену очередного предмета
                # + максимальную цену для максимально возможный для рюкзака вес − вес предмета
                W[i][w] = max(W[i - 1][w], c[i - 1] + W[i - 1][w - a[i - 1]])
            else:
                # если предмет не влезает в рюкзак, записываем предыдущий максимум
                W[i][w] = W[i - 1][w]

            print(W[i][w], end='  ')
        print()

    print("наибольшая суммарная полезность = ", W[n][A])
    # while(n != 0):
    #     if(W[n][A] != W[n - 1][A]):
    #         print("\tпредмет " + str(n) + " c весом = " +  str(c[n - 1]) + " и полезностью = " +str(a[n - 1]))
    #         A = A - a[n - 1]
    #     n=n-1

    while(n != 0):
        if(W[n][A] != W[n - 1][A]):
            print("x" + str(n) + " = " + str(1))
            A = A - a[n - 1]
        else: print("x" + str(n) + " = " + str(0))
        n=n-1

# Метод динамического программирования для задачи о ранце
c = [6, 2, 2, 2, 5] # вес
a = [4, 1, 3, 1, 6] # полезность
A = 7   # емкость (рюкзак) заданной грузоподъемности
n = len(a) #кол-во предметов
print('-----------------')
(knapSack(A, a, c, n))
