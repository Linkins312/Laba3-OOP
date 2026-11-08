class Car:
    
    def __init__(self, brand, model, year, color, speed=0, fuel=50):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.__speed = 0
        self.__fuel = 50
        self.speed = speed
        self.fuel = fuel

    @property
    def speed(self):
        return self.__speed
    
    @property
    def fuel(self):
        return self.__fuel

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError(f"Скорость не может быть отрицательной! Получено: {value}")
        self.__speed = value
    
    @fuel.setter
    def fuel(self, value):
        if value < 0 or value > 100:
            raise ValueError(f"Топливо должно быть от 0 до 100! Получено: {value}")
        self.__fuel = value