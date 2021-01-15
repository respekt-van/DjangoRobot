class Track:
    bottlefound = False
    humanfound = False

    def findBottle(self):  # поиск бутылки
        if self == 'BOTTLE':
            print('bottle found')
            Track.bottlefound = True
        else:
            print('cant find bottle')
            Track.bottlefound = False

    def findHuman(self):  # поиск человека
        if self == 'PERSON':
            print('human found')
            Track.humanfound = True
        else:
            print('cant find human')
            Track.humanfound = False


class Truck:
    Truck_and_camera_diff = 0  # Хардкод(Камера всегда смотрит в сторону движ. тележки)

    def IsTurnedToTheTarget():
        if Truck.Truck_and_camera_diff != 0:
            print(f'Повернитесь на {Truck.Truck_and_camera_diff}')  # команда дополнительному модулю на поворот камеры
            return False
        else:
            return True

    def Move(cmeters):  # команда двигаться вперед модулю тележки
        print(f'Нужно подвинуться вперед на {int(cmeters) - 35} сантиметров')


class Manipulator:
    busy = False

    def Lock():  # команда манипулятору взять
        if not Manipulator.busy:
            print('Беру обьект')

    def Unlock():  # команда манипулятору отдать
        print('Отдаю обьект')

class Wannamore:   # костыль для повторного запуска
    dontwant = False
