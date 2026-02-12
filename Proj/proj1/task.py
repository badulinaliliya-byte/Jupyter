def calculate_and_save():
    try:
        # Запрашиваем 3 целых числа у пользователя
        print("Введите три целых числа:")
        num1 = int(input("Число 1: "))
        num2 = int(input("Число 2: "))
        num3 = int(input("Число 3: "))

        # Вычисляем сумму и среднее арифметическое
        total_sum = num1 + num2 + num3
        average = total_sum / 3

        # Формируем строку результата
        result_text = (
            f"Введенные числа: {num1}, {num2}, {num3}\n"
            f"Сумма: {total_sum}\n"
            f"Среднее арифметическое: {average:.2f}"
        )

        # Выводим результат в консоль для наглядности
        print("\nРезультат вычислений:")
        print(result_text)

        # Сохраняем результат в файл result.txt в кодировке UTF-8
        with open("result.txt", "w", encoding="utf-8") as file:
            file.write(result_text)
        
        print("\nРезультат успешно сохранен в файл result.txt")

    except ValueError:
        print("Ошибка: Пожалуйста, вводите только целые числа.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Запуск функции
if __name__ == "__main__":
    calculate_and_save()