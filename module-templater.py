import os
import shutil
import argparse
import re


template_dir = './template'
template_filename = 'template'
template_const = '$$TEMPLATE$$'
template_screaming_const = '$$TEMPLATE_SCREAMING$$'


def to_camel_case(text):
  s = re.sub(r"(_|-)+", " ", text).title().replace(" ", "")
  return ''.join(s)


def to_screaming_snake_case(text):
  s = re.sub(r"(_|-)+", " ", text).upper().replace(" ", "_")
  return ''.join(s)

# Функция для копирования директории
def copy_and_rename_directory(module_filenames: list[str]):
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
                new_file_contents = new_file_contents.replace(template_const, to_camel_case(module_filename))
                new_file_contents = new_file_contents.replace(template_screaming_const, to_screaming_snake_case(module_filename))
                
                # Перезаписываем файл, если изменения произошли
                if new_file_contents != file_contents:
                    with open(file_path, 'w') as file:
                        file.write(new_file_contents)
                    print(f"Обновлено содержимое файла {file_path}")

# Функция для парсинга параметров командной строки
def parse_arguments():
    parser = argparse.ArgumentParser(description="Копирование и переименование шаблонной директории.")
    parser.add_argument("--filename", "-f", nargs='+', type=str, required=True, help="Имя файлов без суффиксов (module.ts, service.ts).")
   
    args = parser.parse_args()
    
    return args.filename

if __name__ == "__main__":
    filenames = parse_arguments()
    copy_and_rename_directory(filenames)
