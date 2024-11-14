from collections import Counter
import re

def get_frequency(text:str)->list[tuple[str, int]]:
    lowered_text:str = text.lower()
    words: list[str]= re.findall(r'\b\w+\b',lowered_text)
    words_count: Counter = Counter(words)
    return words_count.most_common()

def main():
    text:str=input('enter your text:').strip()
    word_frequecies : list[tuple[str,int]]= get_frequency(text)

    for word, count in word_frequecies:
        print(f'{word}: {count}')
    
if __name__ == "__main__":
    main()