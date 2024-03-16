def search(year, data):
    for stroka in data:
        stroka = stroka.split("$")
        if str(stroka[2]) == str(year):
            return stroka




with open("lan2.txt", "r", encoding ="utf-8") as f:
    data = f.readlines()
    a = []
    print(data)
    #for line in data:
        #s = line.split("$")
        #a.append(s)
    year = "x"
    while year != "0000":
        year = input()
        result = search(year, data)
        if result is None:
            print('В этом году не было создано ЯП')
        elif result[3] == "":
            print(f'в {result[2]} был создан {result[0]}')
        else:
            print(f'в {result[2]} был создан {result[0]}, его создатель: {result[3]}')
