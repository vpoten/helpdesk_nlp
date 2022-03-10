from langdetect import detect


def detect_language(text):
    return detect(text)


if __name__ == "__main__":
    print(detect_language("A user-defined generic class can have ABCs as base classes without a metaclass conflict"))
    print(detect_language("Las tropas aliadas han alcanzado sus ultimos objetivos"))
    # print(detect_language(None))
