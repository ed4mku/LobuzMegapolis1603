with open("lan2.txt", "r", encoding = "utf-8") as f:
    data = f.readlines()
for stroka in data:
    stroka = str(stroka).split("$")
    print (stroka[1])
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c10 = 0
    c11 = 0
    c12 = 0
    c13 = 0
    c14 = 0
    c15 = 0
    c16 = 0
    c17 = 0
    c18 = 0
    if stroka[1] == "язык программирования":
        c1 += 1
    if stroka[1] == "разметка данных":
        c2 += 1
    if stroka[1] == "нотация":
        c3 += 1
    if stroka[1] == "xml формат":
        c4 += 1
    if stroka[1] == "промежуточное представление кода":
        c5 += 1
    if stroka[1] == "визуальный":
        c6 += 1
    if stroka[1] == "протокол":
        c7 += 1
    if stroka[1] == "шаблон":
        c8 += 1
    if stroka[1] == "разметка текста":
        c9 += 1
    if stroka[1] == "сборка":
        c10 += 1
    if stroka[1] == "язык запросов":
        c11 += 1
    if stroka[1] == "конфигурирование":
        c12 += 1
    if stroka[1] == "isa":
        c13 += 1
    if stroka[1] == "язык грамматики":
        c14 += 1
    if stroka[1] == "язык описания интерфейсов":
        c15 += 1
    if stroka[1] == "байткод":
        c16 += 1
    if stroka[1] == "таблицы стилей":
        c17 += 1
    if stroka[1] == "схема":
        c18 += 1
print(f"{c1} книг содержится в библиотеке по типу язык программирования")
print(f"{c2} книг содержится в библиотеке по типу разметка данных")
print(f"{c3} книг содержится в библиотеке по типу нотация")
print(f"{c4} книг содержится в библиотеке по типу xml формат")
print(f"{c5} книг содержится в библиотеке по типу промежуточное представление кода")
print(f"{c6} книг содержится в библиотеке по типу визуальный")
print(f"{c7} книг содержится в библиотеке по типу протокол")
print(f"{c8} книг содержится в библиотеке по типу шаблон")
print(f"{c9} книг содержится в библиотеке по типу разметка текста")
print(f"{c10} книг содержится в библиотеке по типу сборка")
print(f"{c11} книг содержится в библиотеке по типу язык запросов")
print(f"{c12} книг содержится в библиотеке по типу конфигурирование")
print(f"{c13} книг содержится в библиотеке по типу isa")
print(f"{c14} книг содержится в библиотеке по типу язык грамматики")
print(f"{c15} книг содержится в библиотеке по типу язык описания интерфейсов")
print(f"{c16} книг содержится в библиотеке по типу байткод")
print(f"{c17} книг содержится в библиотеке по типу таблицы стилей")
print(f"{c17}  содержится в библиотеке по типу схема")







