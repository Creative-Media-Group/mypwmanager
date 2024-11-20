import csv


def text_direction(
    lang,
    fp="src/mypwmanager/resources/localisation.csv",
):
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
    with open(file=fp, mode="r", newline="", encoding="utf-8") as file:
        locale_csv = csv.reader(file)
        headings = next(locale_csv)
    if lang in rtl_list and lang in headings:
        return "rtl"
    else:
        return "ltr"


if __name__ == "__main__":
    print(
        text_direction(
            fp="src/mypwmanager/resources/localisation.csv",
        )
    )
