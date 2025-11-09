def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue
            name, salary = line.split(',')
            total += int(salary)
            count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return (0, 0)
total, average = total_salary("D:/Pyton/goit-pycore-hw-04/developers.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
