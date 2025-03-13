import re
import string

def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'(?<=[.!?])\s+', text.strip())[0]
            return first_sentence
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")
    return None

def sort_words(sentence):
    phrases = re.findall(r"'([^']+)'", sentence)  # Знаходимо фрази у лапках
    remaining_text = re.sub(r"'([^']+)'", "", sentence)  # Видаляємо фрази з тексту
    words = re.findall(r'\b[\wА-Яа-яЄєІіЇїҐґ]+\b', remaining_text)  # Виділяємо окремі слова
    
    words.extend(phrases)  # Додаємо фрази до списку слів
    words.sort()  # Використовуємо стандартне сортування Python
    return words

def main():
    filename = "text.txt"
    sentence = read_first_sentence(filename)
    
    if sentence:
        print("Перше речення:", sentence)
        sorted_words = sort_words(sentence)
        print("Відсортовані слова:", sorted_words)
        print("Кількість слів:", len(sorted_words))
    else:
        print("Не вдалося зчитати речення з файлу.")

if __name__ == "__main__":
    main()
