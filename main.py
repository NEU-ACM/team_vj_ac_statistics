import csv
import requests
import datetime
import openpyxl
from bs4 import BeautifulSoup


def get_solve(uname):
    get_vj_solve(uname)


def get_vj_solve(uname):
    url = "https://vjudge.net/user/" + uname
    score_file = datetime.date.today().strftime('%Y-%m') + "-Scores.csv"
    cavil = open(score_file, "a")
    writer = csv.writer(cavil)
    try:
        data = [uname]
        res = requests.get(url)
        result = res.text
        soup = BeautifulSoup(result, 'html.parser')
        for i in soup.table.find_all(title=True):
            data.append(str(i.string))
        writer.writerow(data)
    except requests.exceptions:
        print("something error")
    cavil.close()


def pre_file():
    score_file = datetime.date.today().strftime('%Y-%m') + "-Scores.csv"
    cavil = open(score_file, "a")
    writer = csv.writer(cavil)
    writer.writerow(['user', 'day', '7day', '30day', 'all_ac', 'all_attempted'])
    cavil.close()


def read_all_players(filename):
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    col = ws['A']
    users = []
    for i in col:
        users.append(i.value)
    return users


if __name__ == '__main__':
    file = "teams.xlsx"
    pre_file()
    players = read_all_players(file)
    for p in players:
        get_solve(p)
