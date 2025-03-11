import string
import re

# Функція для сортування слів (спочатку українські, потім англійські)
def sort_words(words):
    ukr_words = sorted([word for word in words if re.match(r'^[А-Яа-яЇїІіЄєҐґ]+$', word)], key=str.lower)
    eng_words = sorted([word for word in words if re.match(r'^[A-Za-z]+$', word)], key=str.lower)
    return ukr_words + eng_words

# Читання першого речення з файлу
def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'[.!?]', text, maxsplit=1)[0]
            return first_sentence
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

# Основний код
filename = "input.txt"
first_sentence = read_first_sentence(filename)

if first_sentence:
    print("Перше речення:", first_sentence)
    
    # Видаляємо пунктуацію та отримуємо список слів
    words = first_sentence.translate(str.maketrans('', '', string.punctuation)).split()
    sorted_words = sort_words(words)
    
    print("Відсортовані слова:", sorted_words)
    print("Кількість слів:", len(sorted_words))
