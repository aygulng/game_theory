import copy

def initBaseTable(a, b, c, baseTable):
    for i in range(1, len(c) + 1 + len(a)):
        baseTable[0].append('x' + str(i))
    baseTable[0].append('b')

    for i in range(1, len(a) + 1):
        baseTable.append(['x' + str(i + len(a) + 1)])
    baseTable.append(['c'])
    # базис
    for i in range(1, len(a) + 1):
        baseTable[i] += copy.deepcopy(a[i - 1])
        for j in range(len(a)):
            value = 1 if i == j + 1 else 0
            baseTable[i].append(value)
        baseTable[i].append(b[i - 1])

    for i in range(len(c)):
        c[i] = -c[i]

    baseTable[len(a) + 1] += copy.deepcopy(c)

    for _ in range(len(a) + 1):
        baseTable[len(a) + 1].append(0)

# Выполняется проверка полученного базисного плана на оптимальность по условию:
# если при каком-либо (допустимое базисное решение) в таблице все коэффициенты строки с не отрицательны,
# то данное дбр оптимально, следовательно конец решения
def isOptimalPlan(baseTable):   # проверка положительных оценок
    indexStr = baseTable[len(baseTable) - 1]

    for i in range(1, len(indexStr)):
        if ( indexStr[i] < 0):
            return False
    return True

# Переход к новому базисному плану.
# Для этого из числа небазисных переменных с отрицательными значениями в последней строке ( -cj < 0)
# выбирается переменная, вводимая в базис,
# это переменная которой соответствует наибольшая по модулю отрицательная оценка:
def findColumn(baseTable):
    indexStr = baseTable[len(baseTable) - 1]
    maxVal = float('inf')
    columnIndex = -1

    for i in range(1, len(indexStr)):
        if (indexStr[i] < maxVal):
            maxVal = indexStr[i]
            columnIndex = i

    return columnIndex

# Строка таблицы, в которой получено наименьшее отношение элемента столбца «b»
# к соответствующему положительному элементу ведущего столбца
def findString(column, baseTable):
    strIndex = -1
    minVal = float('inf')
    bIndex = len(baseTable[0]) - 1

    for i in range(1, len(baseTable) - 1):
        if baseTable[i][column] > 0:
            value = baseTable[i][bIndex] / baseTable[i][column]
            if value < minVal:
                minVal = value
                strIndex = i

    return strIndex


def recalcsTable(string, column, baseTable):
    elem = baseTable[string][column]
    stringCount = len(baseTable)
    columnCount = len(baseTable[0])
    newTable = copy.deepcopy(baseTable)

    for i in range(1, columnCount):
        newTable[string][i] = (newTable[string][i] / elem)

    for i in range(1, stringCount):
        if i != string:
            for j in range(1, columnCount):
                newTable[i][j] = (baseTable[i][j] - (baseTable[string][j] * baseTable[i][column]) / elem)
            newTable[i][column] = 0

    newTable[string][0] = baseTable[0][column]
    return newTable


def method(baseTable):
    while isOptimalPlan(baseTable) is False:
        column = findColumn(baseTable)
        string = findString(column, baseTable)
        baseTable = recalcsTable(string, column, baseTable)

    return baseTable


def printResult(baseTable):
    result = []
    result1 = []
    for i in range(len(baseTable[0]) - len(baseTable)):
        baseVar = False
        for j in range(len(baseTable) - 2):
            if baseTable[j + 1][0] == ('x' + str(i + 1)):
                baseVar = True
                break
        value = baseTable[j + 1][len(baseTable[0]) - 1] if baseVar else 0
        result.append(value)

    value = baseTable[len(baseTable)-1][len(baseTable[0]) - 2]
    value1 = baseTable[len(baseTable)-1][len(baseTable[0]) - 3]
    val = baseTable[len(baseTable)-1][len(baseTable[0])-1]
    result1.append(value1)
    result1.append(value)
    print((val)) #средний выигрыш

    print('q* = '+str(result))
    print('p* = '+str(result1))

    for i in range(0,len(result)):
        result[i]=result[i]*(1/val)
    for i in range(0,len(result1)):
        result1[i]=result1[i]*(1/val)
    print('y* = '+str(result))
    print('x* = '+str(result1))

def printTable(baseTable):
    for i in range(len(baseTable)):
        for j in range(len(baseTable[i])):
            print('{0:6} |'.format(baseTable[i][j]), end=' ')
        print()


a = [[2, 4, 0], [1, 0, 4]]
b = [1, 1]
c = [1, 1, 1]
baseTable = [['базис']]

initBaseTable(a, b, c, baseTable)

printTable(baseTable)
print('----------------------------------------------')

baseTable = method(baseTable)
printTable(baseTable)

print('\nРезультат')
printResult(baseTable)