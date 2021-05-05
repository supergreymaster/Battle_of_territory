import sqlite3

for i in range(int(input("Сколько таблиц будет: "))):
    con = sqlite3.connect("SQL/Field.db")

    cur = con.cursor()
    count = int(input("Какого размера будет поле введите одно число: "))
    request = list()
    request2 = list()
    request2_0 = list()
    for i in range(1, count + 1):
        request2.append(f"[{i}]")
        request2_0.append("0")
        request.append(f"[{i}] INT")
    tmp = ", ".join(request)
    print(tmp)

    res = f"{count}x{count}"
    cur.execute(f"""CREATE TABLE pole_{count} (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        {tmp});""")

    con.commit()

    tmp = ", ".join(request2)
    tmp1 = ", ".join(request2_0)
    for i in range(count):
        cur.execute(f"""INSERT INTO pole_{count}({tmp}) VALUES({tmp1})""")
        con.commit()
