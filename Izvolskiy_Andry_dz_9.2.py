'''
Task 2
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

'''

class Road:

    def __init__(self,lenght, width):
        self.lenght = lenght
        self.width = width
        self.weight = 25
        self.height = 5

    def weight_of_asphalt(self):
        weight_of_asphalt = self.lenght * self.width * self.weight * self.height / 1000
        print(f'Для покрытия полотна нужно {round(weight_of_asphalt)} массы асфальта')

r = Road(5000, 20)
r.weight_of_asphalt()