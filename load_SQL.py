import os
import shutil

# с помощью этой программы можно легко загружать за резервированяе файлы

os.chdir("SQL/SQL_save")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
print(os.getcwd())
for item in test:
    if item == "SQL_save":
        continue
    print(item)
    shutil.copy(f"{os.getcwd()}/SQL_save/{item}", f"{os.getcwd()}")
