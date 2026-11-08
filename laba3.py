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

    def calculate_fuel_consumption(self, distance):
        consumption = (distance / 100) * 8
        return consumption
    
    def calculate_max_distance(self):
        return (self.__fuel / 8) * 100
    
    def drive(self, distance):
        consumption = self.calculate_fuel_consumption(distance)
        if consumption > self.__fuel:
            print(f"Недостаточно топлива! Нужно {consumption:.1f} л, есть {self.__fuel} л.")
            return False
        self.__fuel -= consumption
        print(f"Проехали {distance} км. Осталось топлива: {self.__fuel:.1f} л.")
        return True
    
    def refuel(self, liters):
        new_fuel = self.__fuel + liters
        if new_fuel > 100:
            print(f" Бак переполнится! Максимум 100 л.")
            return False
        self.__fuel = new_fuel
        print(f" Заправлено {liters} л. Топливо: {self.__fuel} л.")
        return True
    
    def display_info(self):
        print(f"\n{'='*50}")
        print(f"Автомобиль: {self.brand} {self.model}")
        print(f"   Год: {self.year}")
        print(f"   Цвет: {self.color}")
        print(f"   Скорость: {self.__speed} км/ч")
        print(f"   Топливо: {self.__fuel} л")
        print(f"   Макс. дистанция: {self.calculate_max_distance():.1f} км")
    
    def compare_with(self, other):
        my_distance = self.calculate_max_distance()
        other_distance = other.calculate_max_distance()
        print(f"\n--- Сравнение: {self.brand} vs {other.brand} ---")
        if my_distance > other_distance:
            print(f" Дальше проедет: {self.brand} (разница: {my_distance - other_distance:.1f} км)")
        elif my_distance < other_distance:
            print(f" Дальше проедет: {other.brand} (разница: {other_distance - my_distance:.1f} км)")
        else:
            print(" Автомобили имеют одинаковый запас хода!")

    def apply_tuning(self):
        self.__speed += 20
        print(f" Тюнинг применён! Новая скорость: {self.__speed} км/ч")

        asdasdasdasadad

if __name__ == "__main__":
  
    car1 = Car("Toyota", "Camry", 2020, "Чёрный", speed=0, fuel=80)
    car2 = Car("BMW", "X5", 2022, "Белый", speed=0, fuel=60)
    car3 = Car("Lada", "Vesta", 2023, "Красный", speed=0, fuel=40)
 
    print("Информация об авто")
    car1.display_info()
    car2.display_info()
    car3.display_info()

    print("\n Поездки")
    car1.drive(200)
    car2.drive(150)
    car3.drive(100)

    print("\n Заправка авто")
    car3.refuel(30)
    car3.display_info()
 
    print("\n Результаты сравнения")
    car1.compare_with(car2)
    car2.compare_with(car3)

    print("\n Задача")
    cars = [car1, car2, car3]
    best_car = max(cars, key=lambda c: c.calculate_max_distance())
    print(f"Дальше всех проедет: {best_car.brand} {best_car.model}")
    print(f"   Запас хода: {best_car.calculate_max_distance():.1f} км")
    
    # Проверка инвариантов
    print("\n Проверка Вариантов")
    try:
        car1.speed = -10
    except ValueError as e:
        print(f" Ошибка: {e}")
    
    try:
        car1.fuel = 150
    except ValueError as e:
        print(f" Ошибка: {e}")