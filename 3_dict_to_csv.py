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
    name_dict ={"name":"Ivan","name":"Sergey"}
    age_dict = {"age":"18", "age":"21","age":"30","age":"40" }
    job_dict = {"job":"bank","job":"FMCG","job":"Gov","job":"less"}
    position_dict = {"position":"manager","position":"director","position":"out staff"}

    CV_list = []
    CV_list.append(name_dict)
    CV_list.append(age_dict)
    CV_list.append(job_dict)
    CV_list.append(position_dict)

    print(CV_list)

if __name__ == "__main__":
    main()
