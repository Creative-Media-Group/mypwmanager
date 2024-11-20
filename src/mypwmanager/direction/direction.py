import locale


def text_direction(lang=locale.getlocale()[0].split("_")[0]):
    print(lang)


if __name__ == "__main__":
    text_direction()
