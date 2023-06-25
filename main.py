import csv
import funcs

if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

    contacts_list = funcs.names_formatting(contacts_list)
    contacts_list = funcs.nums_formatting(contacts_list)
    contacts_list = funcs.merge_duplicates(contacts_list)

    with open("phonebook.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=",")
        w.writerows(contacts_list)