import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 150)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

engine.say("I can speak!")      # запись фразы в очередь
engine.say("Я могу говорить!")  # запись фразы в очередь

# очистка очереди и воспроизведение текста
engine.runAndWait()