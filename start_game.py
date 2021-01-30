import os
import shutil

file_way = os.getcwd()
shutil.rmtree(f"{file_way}/Start_game/model/")
shutil.copytree(f"{file_way}/photo/game_castle/model_castle", f"{file_way}/Start_game/model")
shutil.copy(f"{file_way}/SQL/Field.db", f"{file_way}/Start_game")
shutil.copy(f"{file_way}/SQL/Field_value.db", f"{file_way}/Start_game")
shutil.copy(f"{file_way}/SQL/Original_game.db", f"{file_way}/Start_game")
