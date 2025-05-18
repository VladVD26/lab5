import re

def read_first_sentence(filename):
    """Зчитує перше речення з файлу"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            sentences = re.split(r'(?<=[.!?])\s+', text) 
            return sentences[0] if sentences else ""
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return ""
    except Exception as e:
        print(f"Помилка: {e}")
        return ""

def extract_words(sentence):
    """Видаляє пунктуацію і повертає список слів/фраз"""
    words = re.findall(r'\b[а-яА-ЯіїєґІЇЄҐa-zA-Z]+(?:\s[а-яА-ЯіїєґІЇЄҐa-zA-Z]+)?\b', sentence)
    return words

def custom_sort(words):
    """Сортує спочатку українські слова, потім англійські"""
    ukr_words = sorted(
        [w for w in words if re.match(r'^[а-яА-ЯіїєґІЇЄҐ]', w)], key=lambda w: w.lower()
    )
    eng_words = sorted(
        [w for w in words if re.match(r'^[a-zA-Z]', w)], key=lambda w: w.lower()
    )
    return ukr_words + eng_words

filename = "text.txt"
sentence = read_first_sentence(filename)

if sentence:
    print(f"Перше речення: {sentence}")
    
    words = extract_words(sentence)
    sorted_words = custom_sort(words)
    
    print("Відсортований список:", sorted_words)
    print("Кількість слів:", len(words))
