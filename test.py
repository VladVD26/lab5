import re

def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'(?<=[.!?])\s', text)[0]
            print("Перше речення:")
            print(first_sentence)

            words = re.findall(r'\b[а-яїєіїґa-z]+\b', text.lower())

            ukrainian_words = sorted([word for word in words if re.match(r'^[а-яїєіїґ]+$', word)])
            english_words = sorted([word for word in words if re.match(r'^[a-z]+$', word)])

            if ukrainian_words:
                print("\nУкраїнські слова:")
                print(', \n'.join(ukrainian_words))
            if english_words:
                print("\nАнглійські слова:")
                print(', \n'.join(english_words))

            print("\nЗагальна кількість слів:", len(words))
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Помилка: ", str(e))

read_first_sentence('input.txt')

