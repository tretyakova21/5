# Задача 1
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
new_list = [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]
print("1. Новый список:", new_list)

# Задача 2
print("\n2. Таблица умножения от 1 до 10:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")

# Задача 3
with open('исходный_файл.txt', 'r') as source_file, open('новый_файл.txt', 'w') as new_file:
    for i, line in enumerate(source_file, 1):
        if i != 5:
            new_file.write(line)

# Задача 4
with open('файл.txt', 'r') as file:
    for i, line in enumerate(file, 1):
        if i == 4:
            print("\n4. Строка номер 4:", line.strip())
            break

# Задача 5
number = int(input("\n5. Введите число для вычисления суммы от 1 до заданного числа: "))
sum_result = sum(range(1, number + 1))
print("Сумма чисел от 1 до", number, ":", sum_result)

# Задача 6
my_list = [1, 2, 3, 4, 5]
print("\n6. Список в обратном порядке:")
for item in reversed(my_list):
    print(item)

# Задача 7
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start_range = int(input("\n7. Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

prime_numbers = [num for num in range(start_range, end_range + 1) if is_prime(num)]

print("Простые числа в диапазоне:", prime_numbers)
