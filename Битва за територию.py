import pygame
import sys
import os
import shutil
import sqlite3

# COLOR_TEXT = (2, 105, 180)
COLOR_TEXT = (250, 250, 0)
COLOR_TEXT_1 = (216, 183, 132)
COLOR_PLAYER_1 = (0, 0, 255)
COLOR_PLAYER_2 = (255, 0, 0)
COLOR_PLAYER_3 = (128, 0, 128)
COLOR_PLAYER_4 = (0, 255, 0)
CONST_MAINWORK = list()
dictionary_for_optimization = {}
CRUTCH_list = list()


class PushButton:  # Выпоняет функцию кнопки
    def __init__(self, scr):  # её характеристики
        self.image1_or_text0 = False
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.border = False
        self.size_border = 1
        self.enabler = True
        self.color_border = (0, 0, 0)
        self.text = ""
        self.background = False
        self.color_background = (255, 255, 255)
        self.show1_or_hide0 = True
        self.font = Font()
        self.click = ''
        self.target = False
        self.image_way = 'False'

    def show(self):  # следующие функции будут отвечать за изменение характеристик
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def setTarget(self, target):
        self.target = target

    def getFont(self):
        return self.font

    def changeFont(self, font):
        self.font = font

    def setColor(self, color):
        self.color = color

    def setImage(self, image):
        self.image_way = image
        self.image1_or_text0 = True
        self.image = pygame.image.load(image)
        if self.image.get_size() == (self.wight, self.height):
            pass
        else:
            self.image = pygame.transform.scale(self.image, (self.wight, self.height))

    def setEnabler(self, enabler):
        self.enabler = enabler

    def setText(self, text):
        self.image1_or_text0 = False
        self.text = text

    def setBorder(self, border):
        self.border = border

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def setClick(self, click):
        self.click = click

    def clicked(self):  # активирует поставленную функцию при нажатии
        self.click()

    def render(self):  # отрисовывает кнопку
        if not self.show1_or_hide0:
            return
        if self.image1_or_text0:
            self.draw.blit(self.image, (self.x, self.y))
        elif self.background:
            pygame.draw.rect(self.draw, self.color_background,
                             (self.x, self.y, self.wight, self.height))
        elif not self.image1_or_text0:
            text = self.font.getFont().render(self.text, 1, self.color)
            self.draw.blit(text, (self.x, self.y))
        if self.border:
            pygame.draw.rect(self.draw, self.color_border,
                             (self.x, self.y, self.wight, self.height), width=self.size_border)


class Game_pushbutton(PushButton):  # игровая кнопка в которую добавленны новые функции
    def __init__(self, scr):
        super().__init__(scr)


        self.coor = (0, 0)
        self.side = 0
        self.value = 0
        self.start = Start_game()

    def setCoor(self, coor):
        self.coor = (coor[0], coor[1])

    def setImage(self, image):
        self.image_way = image
        self.image1_or_text0 = True
        if self.image_way in dictionary_for_optimization:
            self.image = dictionary_for_optimization[self.image_way]
            return
        self.image = pygame.image.load(image)
        if self.image.get_size() == (self.wight, self.height):
            pass
        else:
            self.image = pygame.transform.scale(self.image, (self.wight, self.height))
            dictionary_for_optimization[self.image_way] = self.image

    def setSide(self, side):
        self.side = side

    def plusValue(self):
        dictt = {0: (-1, -1), 1: (-1, 1), 2: (1, -1), 3: (1, 1)}
        self.value += 1
        # if self.value == 4:
        #     self.value = 0
        #
        #     self.side = 0

    def clicked(self):  # изменены действия при нажатии, это увеличение значения так же при начале изменнения стороны
        st_game_true = self.start.request_sql_original_game("start_game")
        resolut = self.start.request_sql_original_game("resolution_screen")
        side = int(self.start.request_sql_original_game("step_player"))
        if st_game_true == "False":
            if self.side == 0:
                self.side = side
            else:
                return
        elif self.side == 0 or self.side != side:
            return
        self.plusValue()
        self.start.change_field(f"pole_{resolut}", self.coor, self.side)
        self.start.change_field_value(f"pole_{resolut}", self.coor, self.value)
        self.click()


class Label:  # Написанно в пояс. зап.
    def __init__(self, scr):
        self.image1_or_text0 = False
        self.show1_or_hide0 = True
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.text = ""
        self.font = Font()
        self.background = False
        self.background_color = (0, 0, 0)
        self.max_len_text = 10000

    def show(self):
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def setColor(self, color):
        self.color = color

    def setBackground(self, background):
        self.background = background

    def setBackgroundColor(self, color):
        self.background_color = color

    def setMaxLen(self, max_len):
        self.max_len_text = max_len

    def setImage(self, image):
        self.image1_or_text0 = True
        self.image = pygame.image.load(image)
        if self.image.get_size() == (self.wight, self.height):
            pass
        else:
            self.image = pygame.transform.scale(self.image, (self.wight, self.height))

    def setText(self, text):
        self.image1_or_text0 = False
        self.text = text

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def render(self):
        if not self.show1_or_hide0:
            return
        if self.background:
            pygame.draw.rect(self.draw, self.background_color,
                             (self.x, self.y, self.wight, self.height))
        if self.image1_or_text0:
            self.draw.blit(self.image, (self.x, self.y))
        elif self.text:
            if len(self.text) > self.max_len_text:
                self.text = self.text[:self.max_len_text]
            text = self.font.getFont().render(self.text, 1, self.color)
            self.draw.blit(text, (self.x, self.y))


class Lineedit:  # Написанно в пояс. зап.
    def __init__(self, scr):
        self.image1_or_text0 = False
        self.image = ''
        self.draw = scr
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.wight = 0
        self.height = 0
        self.border = False
        self.size_border = 1
        self.enabler = True
        self.color_border = (0, 0, 0)
        self.text = ""
        self.background = False
        self.color_background = (255, 255, 255)
        self.show1_or_hide0 = True
        self.font = Font()
        self.click = ''
        self.target = False
        self.max_len = 10000

    def show(self):
        self.show1_or_hide0 = True

    def hide(self):
        self.show1_or_hide0 = False

    def getFont(self):
        return self.font

    def setTarget(self, target):
        self.target = target

    def changeFont(self, font):
        self.font = font

    def setColor(self, color):
        self.color = color

    def setEnabler(self, enabler):
        self.enabler = enabler

    def setText(self, text):
        self.text = text

    def setBorder(self, border):
        self.border = border

    def setMaxlen(self, max_len):
        self.max_len = max_len

    def setGeometry(self, x, y, wight, height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height

    def clicked(self):
        self.target = True

    def render(self):
        if self.background:
            pygame.draw.rect(self.draw, self.color_background,
                             (self.x, self.y, self.wight, self.height))
        text = self.font.getFont().render(self.text, 1, self.color)
        self.draw.blit(text, (self.x, self.y))
        if self.border:
            pygame.draw.rect(self.draw, self.color_border,
                             (self.x, self.y, self.wight, self.height), width=self.size_border)


class Font:  # Написанно в пояс. зап.
    def __init__(self):
        self.size = 16
        self.family = None

    def setPointSize(self, size):
        self.size = size

    def setFamily(self, family):
        self.family = family

    def getFont(self):
        return pygame.font.Font(self.family, self.size)


class Hover(PushButton):  # Написанно в пояс. зап.
    def __init__(self, other):
        self.image1_or_text0 = other.image1_or_text0
        self.image = other.image
        self.draw = other.draw
        self.color = other.color
        self.x = other.x
        self.y = other.y
        self.wight = other.wight
        self.height = other.height
        self.border = other.border
        self.size_border = other.size_border
        self.enabler = other.enabler
        self.color_border = other.color_border
        self.text = other.text
        self.background = other.background
        self.color_background = other.color_background
        self.show1_or_hide0 = other.show1_or_hide0
        self.font = other.font


# Второстепенные функции для вытаскивания информации из баз данных
# Написанно в пояс. зап.
class Language:
    def __init__(self):
        # подключает к базам данных
        self.sql_setting = sqlite3.connect("SQL/Setting_game.db")
        self.sql_language = sqlite3.connect("SQL/Language_game.db")
        self.sql_setting_game_original = sqlite3.connect("SQL/Original_game.db")

    def request_sql_setting(self, request):
        cur = self.sql_setting.cursor()

        result = cur.execute(f"""SELECT value 
                                 FROM setting 
                                 WHERE name == '{request}'""").fetchall()[0][0]
        if not result:
            print("Пустой запрос 1")
        return result

    def request_sql_language(self, request):
        cur = self.sql_setting.cursor()

        result = cur.execute(f"""SELECT value 
                                 FROM setting 
                                 WHERE name == 'language'""").fetchall()[0][0]

        cur = self.sql_language.cursor()

        result = cur.execute(f"""SELECT value 
                                 FROM language 
                                 WHERE name == '{request}{result}'""").fetchall()[0][0]
        if not result:
            print("Пустой запрос 2")
        return result

    def request_sql_original_game(self, request):
        cur = self.sql_setting_game_original.cursor()

        result = cur.execute(f"""SELECT value 
                                 FROM setting 
                                 WHERE name == '{request}'""").fetchall()[0][0]
        if not result:
            print("Пустой запрос 3")
        return result

    def change_sql_setting(self, name, value):
        cur = self.sql_setting.cursor()

        cur.execute(f"""UPDATE setting SET value == '{value}' 
                                        WHERE name == '{name}'""")
        self.sql_setting.commit()


class Change_sql_original_game:
    def __init__(self):
        self.sql_setting_game_original = sqlite3.connect("SQL/Original_game.db")

    def change_col_player(self, col_player):
        cur = self.sql_setting_game_original.cursor()
        cur.execute(f"""UPDATE setting SET value == '{col_player}' 
                        WHERE name == 'num_play'""")
        self.sql_setting_game_original.commit()

    def change_resolution_screen(self, res):
        cur = self.sql_setting_game_original.cursor()
        cur.execute(f"""UPDATE setting SET value == '{res}' 
                                WHERE name == 'resolution_screen'""")
        self.sql_setting_game_original.commit()

    def change_name_player(self, number, value):
        cur = self.sql_setting_game_original.cursor()
        cur.execute(f"""UPDATE setting SET value == '{value}' 
                                        WHERE name == 'name_player_{number}'""")
        self.sql_setting_game_original.commit()


class Start_game:
    def __init__(self):
        self.field = sqlite3.connect("Start_game/Field.db")
        self.field_value = sqlite3.connect("Start_game/Field_value.db")
        self.original_game = sqlite3.connect("Start_game/Original_game.db")

    def request_sql_original_game(self, request):
        cur = self.original_game.cursor()

        result = cur.execute(f"""SELECT value 
                                 FROM setting 
                                 WHERE name == '{request}'""").fetchall()[0][0]
        if not result:
            print("Пустой запрос START GAME 1")
        return result

    def request_field(self, view, pos):
        cur = self.field.cursor()

        result = cur.execute(f"""SELECT [{pos[0]}] FROM {view} WHERE id == {pos[1]}""").fetchall()
        if not result:
            print("Пустой запрос START GAME 2")
        return result[0][0]

    def request_all_field(self, view):
        cur = self.field.cursor()

        result = cur.execute(f"""SELECT * FROM {view}""").fetchall()
        if not result:
            print("Пустой запрос START GAME 3")
        return result

    def request_all_field_value(self, view):
        cur = self.field_value.cursor()

        result = cur.execute(f"""SELECT * FROM {view}""").fetchall()
        if not result:
            print("Пустой запрос START GAME 3")
        return result

    def request_field_value(self, view, pos):
        cur = self.field_value.cursor()

        result = cur.execute(f"""SELECT [{pos[0]}] FROM {view} WHERE id == {pos[1]}""").fetchall()
        if not result:
            print("Пустой запрос START GAME 3")
        return result[0][0]

    def change_field(self, view, pos, value):
        cur = self.field.cursor()

        cur.execute(f"""UPDATE {view} SET [{pos[0]}] = '{value}' 
                        WHERE id == {pos[1]}""")
        self.field.commit()

    def change_field_value(self, view, pos, value):
        cur = self.field_value.cursor()

        cur.execute(f"""UPDATE {view} SET [{pos[0]}] = '{value}' 
                        WHERE id == {pos[1]}""")
        self.field_value.commit()

    def change_original(self, name, value):
        cur = self.original_game.cursor()

        cur.execute(f"""UPDATE setting SET value = '{value}' 
                                WHERE name == '{name}'""")
        self.original_game.commit()


# начались классы страниц
class Title_1:  # это один из главных классов на который будет равнятся главная страница
    def __init__(self, work):
        self.list_render = list()  # в эти списки добовляются, то с чем будет взаидействовать главный класс
        self.list_hover = list()
        self.list_clik = list()
        self.list_line_edit = list()

        self.main_work = work

        self.main_text_start = ""

        self.start_game = Start_game()  # Активирует классы которые отвечают за базы данных
        self.language = Language()
        self.sql_original_game = Change_sql_original_game()

        self.SetBackground()  # составляет порядок примущества виджетов
        self.create_label()
        self.create_pushbutton()
        self.dop_screen()

    def create_pushbutton(self):  # создание кнопок
        self.title_1_button_start = PushButton(screen)
        self.title_1_button_start.setColor((244, 60, 0))
        self.title_1_button_start.setGeometry(300, 730, 150, 50)
        self.title_1_button_start.setText(self.change_main_text_start())
        self.title_1_button_start.font.setPointSize(96)
        self.title_1_button_start.setClick(self.main_work.transition_1_2)

        self.list_clik.append(self.title_1_button_start)
        self.list_render.append(self.title_1_button_start)

        self.title_1_hover_start = Hover(self.title_1_button_start)
        self.title_1_hover_start.setColor(COLOR_TEXT_1)

        self.list_hover.append(self.title_1_hover_start)

    def create_lineedit(self):  # создание строки ввода текста
        pass

    def create_label(self):  # создание виджетов
        pass

    def SetBackground(self):  # создани фона
        self.title_1_image = Label(screen)
        self.title_1_image.setGeometry(0, 0, 800, 800)
        self.title_1_image.setImage("photo/image_button/main_background.png")
        self.list_render.append(self.title_1_image)

    def dop_screen(self):  # создание дополнительного всплывающего окна
        pass

    def return_render(self):  # следующие 4 функции сделанны для связи с главной функции
        return self.list_render

    def return_lineedit(self):
        return self.list_line_edit

    def return_hover(self):
        return self.list_hover

    def return_clik(self):
        return self.list_clik

    def change_main_text_start(self):  # Хз зачем :) вроде для создания текста старт
        language = Language()
        # Вытаскивает значение из базы данных языка и отправляет в певрую страницу
        self.main_text_start = language.request_sql_language("main_text_start_button_")
        return self.main_text_start  # так и есть


class Main_page(Title_1):  # главная страница здесь происходит изменения настроек
    def create_label(self):
        self.main_page_original = Label(screen)
        self.main_page_original.setGeometry(330, 200, 100, 50)
        self.main_page_original.font.setPointSize(48)
        self.main_page_original.setColor(COLOR_TEXT)

        self.main_page_original.setText(self.language.request_sql_language("main_page_text_original_"))
        self.list_render.append(self.main_page_original)

    def create_pushbutton(self):
        self.main_page_but_original = PushButton(screen)
        self.main_page_but_original.setGeometry(200, 250, 400, 400)
        self.main_page_but_original.setImage("photo/image_button/original_game.png")
        self.main_page_but_original.setClick(self.main_work.transition_2_prep)

        self.main_page_but_originalhover = Hover(self.main_page_but_original)
        self.main_page_but_originalhover.setImage("photo/image_button/original_game_hover.png")

        self.list_hover.append(self.main_page_but_originalhover)
        self.list_clik.append(self.main_page_but_original)
        self.list_render.append(self.main_page_but_original)

        self.main_page_language_change = PushButton(screen)
        self.main_page_language_change.setGeometry(100, 660, 200, 100)
        self.main_page_language_change.setImage("photo/image_button/name_language_" +
                                                self.language.request_sql_setting("language") + ".png")
        self.main_page_language_change.setClick(self.change_language)
        self.list_render.append(self.main_page_language_change)
        self.list_clik.append(self.main_page_language_change)


        self.main_page_language_hover = Hover(self.main_page_language_change)
        self.main_page_language_hover.setImage("photo/image_button/name_language_hover_" +
                                                self.language.request_sql_setting("language") + ".png")
        self.list_hover.append(self.main_page_language_hover)


        self.resolution_but = PushButton(screen)
        self.resolution_but.setGeometry(350, 690, 100, 75)
        self.resolution_but.setText(self.language.request_sql_setting("resolution_screen"))
        self.resolution_but.setColor(COLOR_TEXT)
        self.resolution_but.font.setPointSize(130)
        self.resolution_but.setBorder(True)
        self.resolution_but.color_border = COLOR_TEXT
        self.resolution_but.setClick(self.change_resolution)
        self.list_render.append(self.resolution_but)
        self.list_clik.append(self.resolution_but)

        self.resolution_hover = Hover(self.resolution_but)
        self.resolution_hover.color_border = (255, 255, 255)
        self.list_hover.append(self.resolution_hover)

        self.resolution = Label(screen)
        self.resolution.setGeometry(330, 660, 100, 75)
        self.resolution.setText(self.language.request_sql_language("resolution_"))
        self.resolution.font.setPointSize(24)
        self.resolution.setColor(COLOR_TEXT)
        self.list_render.append(self.resolution)


        self.col_pleyer_but = PushButton(screen)
        self.col_pleyer_but.setGeometry(560, 690, 50, 75)
        self.col_pleyer_but.setText(self.language.request_sql_setting("number_player"))
        self.col_pleyer_but.setColor(COLOR_TEXT)
        self.col_pleyer_but.font.setPointSize(130)
        self.col_pleyer_but.setClick(self.change_col_player)
        self.col_pleyer_but.setBorder(True)
        self.col_pleyer_but.color_border = COLOR_TEXT
        self.list_render.append(self.col_pleyer_but)
        self.list_clik.append(self.col_pleyer_but)

        self.col_pleyer_hover = Hover(self.col_pleyer_but)
        self.col_pleyer_hover.color_border = (255, 255, 255)
        self.list_hover.append(self.col_pleyer_hover)


        self.col_pleyer = Label(screen)
        self.col_pleyer.setGeometry(500, 660, 50, 75)
        self.col_pleyer.setText(self.language.request_sql_language("col_player_"))
        self.col_pleyer.setColor(COLOR_TEXT)
        self.col_pleyer.font.setPointSize(24)
        self.list_render.append(self.col_pleyer)

    def SetBackground(self):
        self.main_page_background = Label(screen)
        self.main_page_background.setGeometry(0, 0, 800, 800)
        self.main_page_background.setImage("photo/open_background/" + self.language.request_sql_setting("Background"))
        self.list_render.append(self.main_page_background)

    def change_language(self):  # изменения языков
        tmp = self.language.request_sql_setting("language")
        if tmp == "rus":
            self.language.change_sql_setting("language", "eng")
        elif tmp == "eng":
            self.language.change_sql_setting("language", "rus")
        self.update_page()

    def change_resolution(self):  # изменения размеров поля
        tmp = self.language.request_sql_setting("resolution_screen")
        if tmp == "10":
            self.language.change_sql_setting("resolution_screen", "15")
        elif tmp == "5":
            self.language.change_sql_setting("resolution_screen", "8")
        elif tmp == "8":
            self.language.change_sql_setting("resolution_screen", "10")
        elif tmp == "15":
            self.language.change_sql_setting("resolution_screen", "25")
        elif tmp == "25":
            self.language.change_sql_setting("resolution_screen", "50")
        elif tmp == "50":
            self.language.change_sql_setting("resolution_screen", "5")
        self.update_page()

    def change_col_player(self):  # изменения количества игроков
        tmp = self.language.request_sql_setting("number_player")
        if tmp == "4":
            self.language.change_sql_setting("number_player", "2")
        elif tmp == "3":
            self.language.change_sql_setting("number_player", "4")
        elif tmp == "2":
            self.language.change_sql_setting("number_player", "3")
        self.update_page()

    def update_page(self):  # для обновления поля
        self.main_work.transition_1_2()


class Prep_original_game(Main_page):  # вспывающее окно
    def dop_screen(self):
        self.list_clik = list()
        self.list_hover = list()
        self.prep_background = Label(screen)
        self.prep_background.setGeometry(200, 200, 400, 400)
        self.prep_background.setImage("photo/image_button/debt_window.png")
        self.list_render.append(self.prep_background)

        self.prep_inf_text = Label(screen)
        self.prep_inf_text.setGeometry(250, 250, 100, 100)
        self.prep_inf_text.setText(self.language.request_sql_language("inf_dop_scr_main_page_"))
        self.prep_inf_text.font.setPointSize(30)
        self.prep_inf_text.setColor(COLOR_TEXT)

        self.list_render.append(self.prep_inf_text)

        self.load_sql_game()

        self.list_prep_line = list()

        for i in range(1, int(self.language.request_sql_original_game("num_play")) + 1):
            self.prep_text_player = Label(screen)
            self.prep_text_player.setText(self.language.request_sql_language("dop_scr_main_page_player_") + str(i))
            self.prep_text_player.setGeometry(230, 255 + i * 50, 150, 50)
            self.prep_text_player.font.setPointSize(40)
            self.prep_text_player.setColor(COLOR_TEXT)

            self.list_render.append(self.prep_text_player)

            self.prep_line = Lineedit(screen)
            self.prep_line.setGeometry(350, 250 + i * 50, 200, 40)
            self.prep_line.setBorder(True)
            self.prep_line.color_border = COLOR_TEXT
            self.prep_line.setMaxlen(10)
            self.prep_line.setColor(COLOR_TEXT)
            self.prep_line.font.setPointSize(40)

            self.list_prep_line.append(self.prep_line)

            self.list_render.append(self.prep_line)
            self.list_clik.append(self.prep_line)
            self.list_line_edit.append(self.prep_line)

        self.prep_but_ok = PushButton(screen)
        self.prep_but_ok.setGeometry(350, 550, 50, 50)
        self.prep_but_ok.setColor(COLOR_TEXT)
        self.prep_but_ok.setText("Ok")
        self.prep_but_ok.font.setPointSize(40)
        self.prep_but_ok.setClick(self.check_right_name)

        self.list_clik.append(self.prep_but_ok)
        self.list_render.append(self.prep_but_ok)

        self.prep_but_out = PushButton(screen)
        self.prep_but_out.setGeometry(575, 200, 25, 25)
        self.prep_but_out.setImage("photo/image_button/exit_brown.png")
        self.prep_but_out.setClick(self.main_work.transition_1_2)

        self.list_render.append(self.prep_but_out)
        self.list_clik.append(self.prep_but_out)

        self.prep_but_ok_hover = Hover(self.prep_but_ok)
        self.prep_but_ok_hover.setColor(COLOR_TEXT_1)

        self.list_hover.append(self.prep_but_ok_hover)

        self.prep_lower_comp = Label(screen)
        self.prep_lower_comp.setGeometry(230, 520, 50, 50)
        self.prep_lower_comp.setText(self.language.request_sql_language("prep_mode_"))
        self.prep_lower_comp.setColor(COLOR_TEXT)
        self.prep_lower_comp.font.setPointSize(26)
        self.list_render.append(self.prep_lower_comp)

        self.prep_lower_comp_but = PushButton(screen)
        self.prep_lower_comp_but.setGeometry(490, 515, 25, 25)
        self.prep_lower_comp_but.setText(self.language.request_sql_language("prep_mode_" +
                                         self.language.request_sql_setting("mode_game") + "_"))
        self.prep_lower_comp_but.setClick(self.change_lower)
        self.prep_lower_comp_but.setColor(COLOR_TEXT)
        self.prep_lower_comp_but.font.setPointSize(40)
        self.list_render.append(self.prep_lower_comp_but)
        self.list_clik.append(self.prep_lower_comp_but)

        self.prep_lower_comp_hover = Hover(self.prep_lower_comp_but)
        self.prep_lower_comp_hover.setColor(COLOR_TEXT_1)

        self.list_hover.append(self.prep_lower_comp_hover)

    def load_sql_game(self):  # вытаскивает из настроек в настройки игры
        self.sql_original_game.change_resolution_screen(self.language.request_sql_setting("resolution_screen"))
        self.sql_original_game.change_col_player(self.language.request_sql_setting("number_player"))

    def check_right_name(self):  # Проверка првильности именн если именна будут одинаковыми, то он сбросит всё
        for i in range(len(self.list_prep_line)):
            tmp = 0
            for j in range(len(self.list_prep_line)):
                if self.list_prep_line[i].text == self.list_prep_line[j].text:
                    tmp += 1
            if tmp != 1:
                self.dop_screen()
                return
        for i in range(1, len(self.list_prep_line) + 1):
            self.sql_original_game.change_name_player(i, self.list_prep_line[i - 1].text)
        self.transfer_SQL_and_photo()
        self.main_work.transition_prep_original()

    def transfer_SQL_and_photo(self):  # Активирует изменяемые настройки в игре
        file_way = os.getcwd()
        shutil.rmtree(f"{file_way}/Start_game/model/")
        if self.language.request_sql_setting("mode_game") == "false":
            shutil.copytree(f"{file_way}/photo/game_castle/model_castle", f"{file_way}/Start_game/model")
        else:
            shutil.copytree(f"{file_way}/photo/game_castle/model_1", f"{file_way}/Start_game/model")
        shutil.copy(f"{file_way}/SQL/Field.db", f"{file_way}/Start_game")
        shutil.copy(f"{file_way}/SQL/Field_value.db", f"{file_way}/Start_game")
        shutil.copy(f"{file_way}/SQL/Original_game.db", f"{file_way}/Start_game")

    def change_lower(self):  # Настройки слабого или сильного компьютера
        if self.language.request_sql_setting("mode_game") == "false":
            self.language.change_sql_setting("mode_game", "true")
        elif self.language.request_sql_setting("mode_game") == "true":
            self.language.change_sql_setting("mode_game", "false")
        self.prep_lower_comp_but.setText(self.language.request_sql_language("prep_mode_" +
                                        self.language.request_sql_setting("mode_game") + "_"))

        self.prep_lower_comp_hover.setText(self.language.request_sql_language("prep_mode_" +
                                        self.language.request_sql_setting("mode_game") + "_"))


class Original_game:  # игровой класс
    def __init__(self, work):
        global dictionary_for_optimization
        dictionary_for_optimization = {}
        self.loop = Game_loop(work, self)

        self.main_work = work
        self.sg = Start_game()
        self.view = self.sg.request_sql_original_game("resolution_screen")
        self.step_player = int(self.sg.request_sql_original_game("step_player"))
        self.step = int(self.sg.request_sql_original_game("step"))
        self.num_player = int(self.sg.request_sql_original_game("num_play"))

        self.list_render = list()
        self.list_clik = list()

    def return_render(self):
        return self.loop.list_render

    def return_lineedit(self):
        return self.loop.list_line_edit

    def return_hover(self):
        return self.loop.list_hover

    def return_clik(self):
        return self.loop.list_clik

    def change_step(self):  # увеличивает ход
        self.step += 1
        self.sg.change_original("step", self.step)

    def change_step_player(self):  # сменяет ход игроков
        if self.sg.request_sql_original_game("start_game") == "True":
            count = 0
            win = list()
            for i in range(1, int(self.sg.request_sql_original_game("num_play")) + 1):
                count_player = int(self.sg.request_sql_original_game(f"count_player_{i}"))
                if count_player == 0:
                    count += 1
                else:
                    win.append(i)
            if len(win) == 1:
                self.win_game()
                return
            warning = False

            self.step_player += 1
            if self.step_player > self.num_player:
                self.step_player = 1
                warning = True
            while self.step_player not in win:
                self.step_player += 1
                if self.step_player > self.num_player:
                    self.step_player = 1
                    warning = True
            if warning:
                self.change_step()
        else:
            self.step_player += 1
            if self.step_player > self.num_player:
                self.step_player = 1
                self.change_step()
        self.sg.change_original("step_player", self.step_player)

    def click_button(self):  # обрабатывает нажатие кнопки
        if self.sg.request_sql_original_game("game_win") == "0":
            pass
        else:
            for i in CRUTCH_list:
                i.hide()
                del CRUTCH_list[0]
            self.main_work.transition_1_2()
            return
        self.rep = Reproduction(self.main_work, self)
        self.rep.check_value()

        self.change_value_player()
        self.change_step_player()
        self.sg.change_original("step_player", self.step_player)
        if self.step == 1:
            self.sg.change_original("start_game", "True")
        self.loop = Game_loop(self.main_work, self)

    def change_value_player(self):  # изменяет базы данных содержащих поле
        dictq = {}
        col_cell = int(self.sg.request_sql_original_game("resolution_screen"))
        list_pole = self.sg.request_all_field(f"pole_{col_cell}")
        list_pole_value = self.sg.request_all_field_value(f"pole_{col_cell}")
        for i in range(len(list_pole)):
            for j in range(1, len(list_pole[i])):
                tmp = int(list_pole[i][j])
                if tmp not in dictq:
                    dictq[tmp] = 0
                dictq[tmp] += int(list_pole_value[i][j])
        for i in range(1, int(self.sg.request_sql_original_game("num_play")) + 1):
            if i in dictq:
                tmp = dictq[i]
            else:
                tmp = 0
            self.sg.change_original(f"count_player_{i}", tmp)

    def win_game(self):  # обрабатывает победу игрока
        print("win")
        self.sg.change_original("game_win", self.sg.request_sql_original_game("step_player"))
        self.win_label = Label(screen)
        language = Language()
        self.win_label.setText(language.request_sql_language("win_game_") + " " +
                               self.sg.request_sql_original_game("step_player"))
        self.win_label.setGeometry(400, 150, 100, 100)
        self.win_label.font.setPointSize(36)
        self.win_label.setColor(COLOR_TEXT)
        CRUTCH_list.append(self.win_label)

    def cheat_game(self, text):
        print("Использование читов")
        list_text = text.split(".")
        if len(list_text) != 4:
            print("Нужно 4 числа")
            return
        try:
            if int(list_text[0]) <= 0 or int(list_text[0]) > int(self.view):
                print("Некорректная кордината x")
                return
            if int(list_text[1]) <= 0 or int(list_text[1]) > int(self.view):
                print("Некорректная кордината y")
                return
            if int(list_text[2]) < 0 or int(list_text[2]) > int(self.view):
                print("Некорректная строна")
                return
            if int(list_text[3]) < 0 or int(list_text[3]) >= 4:
                print("Некорректное значение")
                return
        except ValueError:
            print("Некорректный ввод")
            return

        if int(list_text[0]) == 0 or int(list_text[1]) == 0:
            self.sg.change_field("pole_" + self.view, (int(list_text[0]), int(list_text[1])), 0)
            self.sg.change_field_value("pole_" + self.view, (int(list_text[0]), int(list_text[1])), 0)
            print("ok")
            return

        self.sg.change_field("pole_" + self.view, (int(list_text[0]), int(list_text[1])),
                             list_text[2])
        self.sg.change_field_value("pole_" + self.view, (int(list_text[0]), int(list_text[1])),
                                   list_text[3])

        self.loop = Game_loop(self.main_work, self)
        print("ok")


class Reproduction:  # Этот класс отвечает за атаку соседних клеток
    def __init__(self, work, orig):
        self.start = Start_game()

        self.main_work = work
        self.orig = orig

    def check_value(self):  # Проверка занчения ведь оно не должно превышать 4, если же превышает,
        # то программа запускает атаку соседних клеток
        self.view_number = self.start.request_sql_original_game("resolution_screen")
        self.view = "pole_" + self.view_number
        self.side = self.start.request_sql_original_game("step_player")

        warning = True
        while warning:
            self.list_field = self.start.request_all_field(self.view)
            self.list_field_value = self.start.request_all_field_value(self.view)

            warning = False
            for i in range(len(self.list_field_value)):
                for j in range(1, len(self.list_field_value[i])):
                    if self.list_field_value[i][j] >= 4:
                        tmp = i + 1
                        warning = True
                        self.start.change_field_value(self.view, (j, tmp), 0)
                        self.start.change_field(self.view, (j, tmp), 0)

                        # print("!--------------------")
                        # print(self.list_field_value[i][j], type(self.list_field_value[i][j]))
                        # print(self.list_field)
                        # print(self.list_field_value)
                        # print(j, tmp, type(j), type(tmp))
                        # print(self.view_number)
                        # print("---------------------")

                        if tmp + 1 <= int(self.view_number):
                            tmp1 = self.start.request_field_value(self.view, (j, tmp + 1))
                            self.start.change_field_value(self.view, (j, tmp + 1), min(4, int(tmp1) + 1))
                            self.start.change_field(self.view, (j, tmp + 1), self.side)
                        if tmp - 1 >= 1:
                            tmp1 = self.start.request_field_value(self.view, (j, tmp - 1))
                            self.start.change_field_value(self.view, (j, tmp - 1), min(4, int(tmp1) + 1))
                            self.start.change_field(self.view, (j, tmp - 1), self.side)
                        if j + 1 <= int(self.view_number):
                            tmp1 = self.start.request_field_value(self.view, (j + 1, tmp))
                            self.start.change_field_value(self.view, (j + 1, tmp), min(4, int(tmp1) + 1))
                            self.start.change_field(self.view, (j + 1, tmp), self.side)
                        if j - 1 >= 1:
                            tmp1 = self.start.request_field_value(self.view, (j - 1, tmp))
                            self.start.change_field_value(self.view, (j - 1, tmp), min(4, int(tmp1) + 1))
                            self.start.change_field(self.view, (j - 1, tmp), self.side)


class Game_loop:  # Занимается обновлением поля
    def __init__(self, work, orig):  # Создание поля
        self.orig_game = orig
        self.main_work = work

        self.list_render = list()
        self.list_hover = list()
        self.list_clik = list()
        self.list_line_edit = list()
        self.start_game = Start_game()

        self.list_player_statistics = list()
        self.list_player_statistics.extend(CRUTCH_list)
        self.list_but_game = list()
        self.list_peref = list()

        self.orig_game_bg = Label(screen)
        self.lan = Language()
        self.orig_game_bg.setGeometry(0, 0, 800, 800)
        self.orig_game_bg.setImage("photo/open_background/" + self.lan.request_sql_setting("Background"))
        self.list_render.append(self.orig_game_bg)

        self.orig_game_but_out = PushButton(screen)
        self.orig_game_but_out.setGeometry(0, 0, 50, 50)
        self.orig_game_but_out.setImage("photo/image_button/exit_orange.png")
        self.orig_game_but_out.setClick(self.main_work.transition_1_2)

        self.list_render.append(self.orig_game_but_out)
        self.list_clik.append(self.orig_game_but_out)

        self.cheat_line = Lineedit(screen)
        self.cheat_line.setMaxlen(10)
        self.cheat_line.setGeometry(710, 725, 60, 25)
        self.cheat_line.setColor((255, 255, 255))
        # self.cheat_line.setBorder(True)
        self.cheat_line.font.setPointSize(20)

        self.list_render.append(self.cheat_line)
        self.list_line_edit.append(self.cheat_line)
        self.list_clik.append(self.cheat_line)

        self.cheat_but = PushButton(screen)
        self.cheat_but.setGeometry(750, 760, 50, 40)
        self.cheat_but.setClick(self.cheat)

        self.list_render.append(self.cheat_but)
        self.list_clik.append(self.cheat_but)

        for i in range(1, int(self.start_game.request_sql_original_game("num_play")) + 1):
            self.orig_game_player = Label(screen)
            self.orig_game_player.setGeometry(60 + i * 150, 10, 10, 10)
            self.orig_game_player.setText(self.start_game.request_sql_original_game(f"name_player_{i}"))
            self.orig_game_player.setColor(COLOR_TEXT)
            self.orig_game_player.font.setPointSize(26)

            self.list_peref.append(self.orig_game_player)

            self.orig_game_col_player = Label(screen)
            self.orig_game_col_player.setText(self.start_game.request_sql_original_game(f"count_player_{i}"))
            self.orig_game_col_player.setGeometry(60 + i * 150, 75, 75, 75)
            self.orig_game_col_player.font.setPointSize(40)
            if int(self.start_game.request_sql_original_game(f"step_player")) == i:
                self.orig_game_col_player.setColor((250, 250, 0))
            else:
                self.orig_game_col_player.setColor((255, 255, 255))
            self.orig_game_col_player.setMaxLen(5)


            self.list_player_statistics.append(self.orig_game_col_player)


            self.orig_game_bg_col_player = Label(screen)
            self.orig_game_bg_col_player.setGeometry(50 + i * 150, 40, 100, 100)
            self.orig_game_bg_col_player.setImage(f"photo/image_button/color_player_{i}.png")

            self.list_peref.append(self.orig_game_bg_col_player)


        self.list_render.extend(self.list_peref)
        self.list_render.extend(self.list_player_statistics)

        # игровые кнопки
        col_cell = int(self.start_game.request_sql_original_game("resolution_screen"))
        size_cell = 600 // col_cell
        list_pole = self.start_game.request_all_field(f"pole_{col_cell}")
        list_pole_value = self.start_game.request_all_field_value(f"pole_{col_cell}")
        civi = ''
        for i in range(len(list_pole)):
            for j in range(1, len(list_pole[i])):
                self.cell = Game_pushbutton(screen)
                self.cell.setGeometry(100 + (j - 1) * size_cell, 190 + i * size_cell, size_cell, size_cell)

                self.cell.coor = (j, i + 1)
                self.cell.side = list_pole[i][j]
                self.cell.value = list_pole_value[i][j]

                if self.cell.side == 0:
                    self.cell.setImage(f"Start_game/model/{self.cell.side}.png")
                else:
                    civi = self.start_game.request_sql_original_game(f"color_player_{self.cell.side}")
                    self.cell.setImage(f"Start_game/model/{civi}/{self.cell.value}.png")

                self.cell.setClick(self.orig_game.click_button)

                self.list_but_game.append(self.cell)

                self.list_clik.append(self.cell)
        self.list_render.extend(self.list_but_game)
        CONST_MAINWORK[0].crutch_rendering(self.list_render)

    def update_pole(self):  # обновление поля
        for i in range(1, len(self.list_player_statistics) + 1):
            self.list_player_statistics[i - 1].setText(self.start_game.request_sql_original_game(f"count_player_{i}"))


        col_cell = int(self.start_game.request_sql_original_game("resolution_screen"))
        list_pole = self.start_game.request_all_field(f"pole_{col_cell}")
        list_pole_value = self.start_game.request_all_field_value(f"pole_{col_cell}")
        civi = ''

        for i in self.list_but_game:
            coor = i.coor
            i.name = 0
            # print(i.side, "before side")
            # print(i.value, "before value")
            i.side = list_pole[coor[0] - 1][coor[-1]]
            i.value = list_pole_value[coor[0] - 1][coor[-1]]
            # print(i.side, "after side")
            # print(i.value, "after value")
            if i.side == 0:
                i.setImage(f"Start_game/model/{i.side}.png")
            else:
                civi = self.start_game.request_sql_original_game(f"color_player_{i.side}")
                i.setImage(f"Start_game/model/{civi}/{i.value}.png")

        for i in self.list_but_game:
            print(i.image_way)

        print(list_pole)
        print(list_pole_value)
        print("Ok")

        self.list_render = list()
        self.list_render.extend(self.list_player_statistics)
        self.list_render.extend(self.list_peref)
        self.list_render.extend(self.list_but_game)
        CONST_MAINWORK[0].crutch_rendering(self.list_render)

    def cheat(self):
        self.orig_game.cheat_game(self.cheat_line.text)


# Главная функция здесь все происходит
class Main_work:
    def __init__(self):
        self.page = 'False'
        self.render = list()
        self.hoverr = list()
        self.mouse_pos = (0, 0)
        self.work = ""
        self.orig = Start_game()

    # следующие функции отвечают за переход страниц
    def title1(self, work):
        self.work = work
        self.page = Title_1(self)

        # коректировка работы программы (необращайте внимание)
        # self.transition_1_2()
        # self.transition_prep_original()

    def transition_1_2(self):
        for i in CRUTCH_list:
            i.hide()
            del CRUTCH_list[0]
        self.orig.change_original("game_win", "0")
        self.page = Main_page(self)

    def transition_2_prep(self):
        self.page = Prep_original_game(self)

    def transition_prep_original(self):
        self.page = Original_game(self)

    def SetMousePos(self, pos):
        self.mouse_pos = pos

    # следующие функции отвечают за связь движка с программой
    def del_sumbol(self):
        for i in self.page.return_lineedit():
            if i.target:
                if bool(i.text):
                    i.text = i.text[:-1]

    def GetText(self, text):
        for i in self.page.return_lineedit():
            if i.target:
                if text not in "!@#$%^&*№;:?~`\/" and len(i.text) < i.max_len:
                    i.text = i.text + text

    def hovering(self):
        for i in self.page.return_hover():
            if i.x < self.mouse_pos[0] < i.x + i.wight and i.y < self.mouse_pos[1] < i.y + i.height:
                i.render()

    def rendering(self):
        for i in self.page.return_render():
            # if i.text:
            # print(i.text)
            i.render()

    def crutch_rendering(self, list_value):
        for i in list_value:
            i.render()

    def clike(self, pos):
        for i in self.page.return_clik():
            if i.x < pos[0] < i.x + i.wight and i.y < pos[1] < i.y + i.height:
                i.clicked()
            else:
                i.setTarget(False)


if __name__ == '__main__':  # pygame отвечающий за обработку событий
    pygame.init()
    pygame.display.set_caption('Битва за територию')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    screen.fill((255, 128, 0))

    work = Main_work()
    CONST_MAINWORK.append(work)

    work.title1(work)

    work.rendering()
    work.hovering()
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                work.SetMousePos(event.pos)
                work.rendering()
                work.hovering()
            elif event.type == pygame.KEYDOWN:
                if event.key == 8:
                    work.del_sumbol()
                work.rendering()
                work.hovering()
            elif event.type == pygame.TEXTINPUT:
                work.GetText(event.text)
                work.rendering()
                work.hovering()
            elif event.type == pygame.MOUSEBUTTONUP:
                work.clike(event.pos)
                work.rendering()
                work.hovering()
        pygame.display.flip()
