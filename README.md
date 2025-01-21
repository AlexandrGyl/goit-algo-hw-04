# goit-algo-hw-04 

Алгоритми сортування \
  Сортування злиттям (Merge Sort): \
        Складність: O(nlog⁡n)O(nlogn) \
        Стабільне сортування. 

   Сортування вставками (Insertion Sort): \
        Складність: O(n2)O(n2) у найгіршому випадку, O(n)O(n) у найкращому випадку. \
        Стабільне сортування. 

   Timsort: \
        Складність: O(nlog⁡n)O(nlogn) \
        Гібридний алгоритм, що поєднує сортування злиттям і сортування вставками. \
        Стабільне сортування. 

Для порівняння різних способів сотрування, наведемо результати отримані за допомогою програми, у якій реалізовані види сортування наведені вище.
Як варіант списку значань, використано генератор випадкових чисел.

# Результат 1: # 
Генеруємо випадковий список чисел \
Ведіть початкове число для генерації: 1 \
Ведіть кінцеве число для генерації: 1000 \
Ведіть кількість елементів у списку: 10000 \
Сортування списку вставками із 10000 елементів зайняло 2.6287 секунд. \
Сортування списку злиттям із 10000 елементів зайняло 0.0235 секунд. \
Сортування списку Timsort із 10000 елементів зайняло 0.0013 секунд. 

# Результат 2:# 
Генеруємо випадковий список чисел \
Ведіть початкове число для генерації: 5 \
Ведіть кінцеве число для генерації: 1000 \
Ведіть кількість елементів у списку: 500 \
Сортування списку вставками із 500 елементів зайняло 0.0251 секунд. \
Сортування списку злиттям із 500 елементів зайняло 0.0040 секунд. \
Сортування списку Timsort із 500 елементів зайняло 0.0002 секунд. 

# Результат 3:# 
Генеруємо випадковий список чисел \
Ведіть початкове число для генерації: 1 \
Ведіть кінцеве число для генерації: 10000 \
Ведіть кількість елементів у списку: 20000 \
Сортування списку вставками із 20000 елементів зайняло 9.2952 секунд. \
Сортування списку злиттям із 20000 елементів зайняло 0.0429 секунд. \
Сортування списку Timsort із 20000 елементів зайняло 0.0029 секунд. 

У всіх трьох випадках гібридний алгоритм дає найкращі результати. 
