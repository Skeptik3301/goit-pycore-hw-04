import sys
from pathlib import Path
from colorama import Fore, Style, init
init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
   
    try:
     
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        print(indent + Fore.RED + "[Доступ заборонено]" + Style.RESET_ALL)
        return

    for item in items:
        if item.is_dir():
            print(f"{indent}{Fore.CYAN}📂 {item.name}{Style.RESET_ALL}")
            print_directory_structure(item, indent + "   ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main():
    
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: потрібно вказати шлях до директорії!" + Style.RESET_ALL)
        print("Приклад: python hw03.py D:\\my_folder")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не існує!" + Style.RESET_ALL)
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: '{dir_path}' не є директорією!" + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.YELLOW + f"\nСтруктура директорії: {dir_path}\n" + Style.RESET_ALL)
    print_directory_structure(dir_path)


if __name__ == "__main__":
    main()
