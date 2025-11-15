text = ('— Я всё очень тщательно проверил, — сказал компьютер, — и со всей определённостью '
        'заявляю, что это и есть ответ. Мне кажется, если уж быть с вами абсолютно честным, '
        'то всё дело в том, что вы сами не знали, в чём вопрос.')

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


print(*_get_part_text(text, 54, 70), sep='\n')