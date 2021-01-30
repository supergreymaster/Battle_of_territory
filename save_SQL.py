import os
import shutil

# с помощью этой программы можно легко сохранять изменения в файлах

os.chdir("SQL")
tmp = os.getcwd()
test = os.listdir(tmp)
for item in test:
    if item == "SQL_save":
        continue
    shutil.copy(f"{os.getcwd()}/{item}", f"{os.getcwd()}/SQL_save")
