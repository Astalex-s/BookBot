import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    punctuation = ',.!:;?'
    end = min(start + page_size, len(text))

    last_punctuation = -1
    for i in range(end - 1, start - 1, -1):
        if text[i] in punctuation:
            if i + 1 < len(text) and text[i + 1] in punctuation:
                continue
            last_punctuation = i
            break
    if last_punctuation == -1:
        return (text[start:end], end - start)
    return (text[start:last_punctuation + 1], last_punctuation + 1 - start)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:

    global book  # Используем существующий словарь book
    PAGE_SIZE = 1050  # Указанный в задании размер страницы

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    start = 0
    page_number = 1

    while start < len(text):
        page_text, page_length = _get_part_text(text, start, PAGE_SIZE)
        # Удаляем начальные пробельные символы и добавляем страницу в словарь
        book[page_number] = page_text.lstrip()
        start += page_length
        page_number += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))