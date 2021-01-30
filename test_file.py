import sqlite3

field_value = sqlite3.connect("Start_game/Field_value.db")
pos = (1, 2)
view = "pole_5"

cur = field_value.cursor()

result = cur.execute(f"""SELECT [{pos[0]}] FROM {view} WHERE id == {pos[1]}""").fetchall()
if not result:
    print("Пустой запрос START GAME 3")
print(result[0][0])
