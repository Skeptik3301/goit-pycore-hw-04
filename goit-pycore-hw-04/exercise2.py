def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:  
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f" Помилка у форматі рядка: {line}")
        return cats

    except FileNotFoundError:
        print(" Помилка: файл не знайдено.")
        return []
    except Exception as e:
        print(f" Невідома помилка: {e}")
        return []

cats_info = get_cats_info("cats.txt")
print(cats_info)
