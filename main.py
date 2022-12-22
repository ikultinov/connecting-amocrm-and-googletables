
import json
import gspread
import schedule

count = 1


def connecting_amocrm_go_tables():
    """
    Получение логов в виде JSON из AmoCRM и запись их в Google
    Tables.
    """
    gc = gspread.service_account(filename='onyx-glazing-372105-5a331e66f343'
                                          '.json')
    sh = gc.open_by_key('1rE4cAYwwPI-HipJPuq5GIhmeAseIK3BI_MleWBm-hCw')
    worksheet = sh.sheet1

    with open('log_cluster_1.json', 'r', encoding="utf-8") as file:
        log = str(json.load(file))

    global count
    worksheet.update(f'A{count}', log)
    count += 1
    return count


def main():
    """
    Запуск  функции connecting_amocrm_go_tables() в ежедневно в определенное
    время.
    """

    schedule.every().day.at('06:51').do(connecting_amocrm_go_tables)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
