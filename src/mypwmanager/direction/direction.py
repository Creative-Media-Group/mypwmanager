import locale


def text_direction(lang=locale.getlocale()[0].split("_")[0]):
    rtl_list = [
        "ar",
        "fa",
        "ur",
        "ps",
        "sd",
        "ckb",
        "prs",
        "bal",
        "ug",
        "he",
        "he",
        "yi",
        "lad",
        "syc",
        "dv",
        "nqo",
        "fuf",
    ]
    if lang in rtl_list:
        return "rtl"


if __name__ == "__main__":
    text_direction()
