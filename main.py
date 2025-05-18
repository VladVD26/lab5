import re

def sort_words(words):
    ukrainian_words = []
    english_words = []
    
    for word in words:
        if re.search('[а-яА-ЯїЇіІєЄ]', word):
            ukrainian_words.append(word)
        else:
            english_words.append(word)

    ukrainian_words.sort(key=lambda x: x.lower())
    english_words.sort(key=lambda x: x.lower())
    
    return ukrainian_words + english_words

def process_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            first_sentence = re.split(r'[.!?]', content)[0].strip()
            print("Перше речення:", first_sentence)
            
            words = re.findall(r'\b[а-яА-ЯїЇіІєЄa-zA-Z]+\b', content)
            
            sorted_words = sort_words(words)
            
            print("\nВідсортовані слова:")
            for word in sorted_words:
                print(word)
                
            print("\nКількість слів:", len(words))
            
    except FileNotFoundError:
        print(f"Помилка: файл {filename} не знайдено")
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")

if __name__ == "__main__":
    process_text_file("text.txt")
