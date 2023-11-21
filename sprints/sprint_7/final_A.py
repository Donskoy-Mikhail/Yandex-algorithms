"""
94991277

-- ПРИНЦИП РАБОТЫ --

Мы создаем двумерный массив dp, где dp[i][j]
представляет минимальное расстояние между подстроками s1[:i] и s2[:j].
Затем мы инициализируем первую строку и первый столбец (расстояние от пустой строки к каждой подстроке),
 а затем заполняем остальные ячейки массива, используя формулу для расчета расстояния Левенштейна.

 -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

Мы создаем двумерный массив dp, где dp[i][j]
будет представлять минимальное расстояние между подстроками s1[:i] и s2[:j].
Мы определяем размеры массива m и n как длины строк s1 и s2,
и затем создаем массив dp размером (m+1) x (n+1) и инициализируем его нулями.
Далее инициализируем первую строку и первый столбец массива dp.
Первая строка представляет расстояние от пустой строки s1[:i] к подстроке s2[:j],
а первый столбец - расстояние от подстроки s1[:i] к пустой строке s2[:j].
Эти исходные значения задаются от 0 до длин строк s1 и s2.

Потом мы заполняем остальные ячейки массива dp с помощью вложенных циклов.
Мы вычисляем расстояние Левенштейна для каждой пары символов из строк s1 и s2.
Если символы в текущих позициях совпадают (s1[i-1] == s2[j-1]),
 cost устанавливается в 0, иначе в 1.
Затем мы вычисляем три возможных пути для заполнения ячейки dp[i][j]:

dp[i-1][j] + 1 - расстояние от s1[:i-1] к s2[:j], учитывая операцию удаления.
dp[i][j-1] + 1 - расстояние от s1[:i] к s2[:j-1], учитывая операцию вставки.
dp[i-1][j-1] + cost - расстояние от s1[:i-1] к s2[:j-1], учитывая операцию замены (с учетом cost).
Затем мы выбираем минимальное из этих трех значений и устанавливаем его как значение dp[i][j].

В конце мы возвращаем значение dp[m][n]

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Временная сложность алгоритма Левенштейна,
реализованного при помощи динамического программирования,
 O(m * n), где m и n - длины строк s1 и s2

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственная сложность алгоритма также составляет O(m * n),
 так как мы используем двумерный массив dp

"""


def levenshtein_distance(s1, s2):

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Удаление
                dp[i][j - 1] + 1,  # Вставка
                dp[i - 1][j - 1] + cost  # Замена
            )

    return dp[m][n]


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    distance = levenshtein_distance(s1, s2)
    print(distance)