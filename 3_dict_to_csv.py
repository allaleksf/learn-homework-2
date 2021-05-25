"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    first_mem ={"name":"Ivan","age":"18","job":"bank","position":"manager"}
    sec_mem = {"name":"Peter","age":"28","job":"FMCG","position":"director"}
    thi_mem = {"name":"Serg","age":"38","job":"GOV","position":"head of"}
    fou_mem = {"name":"Alex","age":"100","job":"IP","position":"self emploed"}

    CV_list = []
    CV_list.append(first_mem)
    CV_list.append(sec_mem)
    CV_list.append(thi_mem)
    CV_list.append(fou_mem)


    import json

    with open("/Users/filatov1-av/Downloads/list1.txt", "w", encoding="utf-8") as file:
        json.dump(CV_list, file)

    import csv

    with open("/Users/filatov1-av/Downloads/list2.csv", "w", encoding="utf-8", newline='') as f2:
        fields = ['name', 'age', 'job', 'position']
        writer = csv.DictWriter(f2, fields, delimiter=';')
        writer.writeheader()
        for user in CV_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
