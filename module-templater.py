import os
import shutil
import argparse

template_dir = './template'
template_filename = 'template'
template_const = 'TEMPLATE'

# Функция для копирования директории
def copy_and_rename_directory(module_filenames: list[str], module_consts: list[str]):
    # Копируем шаблон-директорию
    for module_filename in module_filenames:
        target_dir = './' + module_filename 
        shutil.copytree(template_dir, target_dir)
        print(f"Директория скопирована из {template_dir} в {target_dir}")

        for root, _, files in os.walk(target_dir):
            # Переименование файлов на основе словаря замены
            for filename in files:
                new_filename = filename
                new_filename = new_filename.replace(template_filename, module_filename)
                if new_filename != filename:
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, new_filename)
                    os.rename(old_path, new_path)
                    print(f"Файл {old_path} переименован в {new_path}")
            
        for root, _, files in os.walk(target_dir):
            # Проход по содержимому файлов для замены текстов
            for filename in files:
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                
                # Выполняем замену констант внутри файлов
                new_file_contents = file_contents
                new_file_contents = new_file_contents.replace(template_filename, module_filename)
                for module_const in module_consts:
                    new_file_contents = new_file_contents.replace(template_const, module_const)
                
                # Перезаписываем файл, если изменения произошли
                if new_file_contents != file_contents:
                    with open(file_path, 'w') as file:
                        file.write(new_file_contents)
                    print(f"Обновлено содержимое файла {file_path}")

# Функция для парсинга параметров командной строки
def parse_arguments():
    parser = argparse.ArgumentParser(description="Копирование и переименование шаблонной директории.")
    parser.add_argument("--filename", type=str, nargs='+', required=True, help="Имя файлов без префиксов (module.ts, service.ts).")
    parser.add_argument("--const", type=str, nargs='+', required=True, help="Имя констант без суффиксов (Module, Service).")
    
    args = parser.parse_args()
    
    return args.filename, args.const

if __name__ == "__main__":
    filenames, consts = parse_arguments()
    copy_and_rename_directory(filenames, consts)
