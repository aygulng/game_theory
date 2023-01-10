
# Для вычислений используется вспомогательная функция факториала:
def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

# Для вычисления вклада игрока необходима следующая функция,
# которая бы сравнивала коалицию с этим игроком и коалицию без этого игрока
def player_profit(coalition, player):
    with_player = function.get(coalition)
    without_player = function.get(coalition.replace(str(player), ''), 0)
    return with_player - without_player

# Для определения количества различных вариантов порядка включения игрока в полную коалицию,
# в которой i-ый игрок расположен на k-ом месте нужна следующая функция:
def number_of_inclusions(n, coalition):

    k = len(coalition) # k – номер, каким i-ый игрок был включен в коалицию
    fact_nk = fac(n - k)
    fact_k1 = fac(k - 1)
    fact_n = fac(n)
    return (fact_nk * fact_k1) / fact_n
# Учитывается количество перестановок игроков,
# вступивших в коалицию до i-ого игрока (которые стоят на (k-1) первых местах),
# и количество перестановок игроков,
# которые вступили в коалицию после i-ого игрока (которые стоят на (n-k) последних местах).

function = {
    '1': 20,
    '2': 30,
    '3': 0,
    '12': 80,
    '13': 50,
    '23': 65,
    '123': 100
}

n = 3   # общее количество игроков в игре
vector = []
for i in range(n):
    value = 0
    player = i + 1

    for k in function.keys():
        if str(player) in k:
            value += number_of_inclusions(n, k) * player_profit(k, player)
    vector.append(value)

print("Вектор Шепли: " + str(vector))