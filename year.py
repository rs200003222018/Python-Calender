# 元号用
meiji = 1900
taisho = 1912
shouwa = 1926
heisei = 1989
reiwa = 2019
reiwa_end = 2050

# 明治和暦変換用
meiji_offset = 33

while True:
    year = input("何か入力してください: ")
    if int(year) < meiji or int(year) > reiwa_end:
        print("範囲外です")
        continue
    else:
        break

year_offset = int(year) + 1

# 1900～1911 明治33年～明治44年
if int(year) < taisho:
    m_seireki = (int(year) + int(meiji_offset)) - int(meiji)
    print("明治" + str(m_seireki) + "年です！")

# 1912～1925 → 大正1年～大正14年
elif int(year) < shouwa:
    t_seireki = int(year_offset) - int(taisho)
    # 大正元年の場合
    if t_seireki == 1:
        print("大正元年です！")
    # 大正2年～大正14年
    else:
        print("大正" + str(t_seireki) + "年です！")

# 1926～1988 → 昭和1年～昭和63年
elif int(year) < heisei:
    s_seireki = int(year_offset) - int(shouwa)
    # 昭和元年の場合
    if s_seireki == 1:
        print("昭和元年です！")
    # 昭和2年～昭和63年
    else:
        print("昭和" + str(s_seireki) + "年です！")

# 1989～2018 → 平成1年～平成30年
elif int(year) < reiwa:
    h_seireki = int(year_offset) - int(heisei)
    # 平成元年の場合
    if h_seireki == 1:
        print("平成元年です！")
    else:
        print("平成" + str(h_seireki) + "年です！")

# 2019～2050 → 令和1年～令和32年
elif int(year) <= reiwa_end:
    r_seireki = int(year_offset) - int(reiwa)
    # 令和元年の場合
    if r_seireki == 1:
        print("令和元年です！")
    else:
        print("令和" + str(r_seireki) + "年です！")
