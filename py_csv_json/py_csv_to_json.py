import csv
import json


def main():
    f = open('students.csv', 'r')
    reader = csv.DictReader(f)
    rows = list(reader)
    v = open('students.json', 'w')
    json.dump(rows, v)


if __name__ == '__main__':
    main()
