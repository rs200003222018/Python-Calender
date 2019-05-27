def to_year_str(year):
    if year == 1:
        return "元"
    return str(year)


ERA = [(1868, "明治"), (1912, "大正"), (1926, "昭和"), (1989, "平成"), (2019, "令和")]

while True:
    year = input("年4桁入力")
    if year == "0000":
        break
    try:
        y = int(year)
        if y < 1900 or y > 2050:
            continue
        for e in reversed(ERA):
            if y >= e[0]:
                print(e[1] + to_year_str(y - e[0] + 1) + "年")
                break
    except:
        continue
