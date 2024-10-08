class Vehicle:
    __COLOR_VARIANTS = ['красный', 'синий', 'зеленый', 'черный', 'белый']  # Допустимые цвета

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner  # Владелец транспорта
        self.__model = model  # Модель (защищенный атрибут)
        self.__engine_power = engine_power  # Мощность двигателя (защищенный атрибут)

        # Проверим, допустим ли цвет
        if color in Vehicle.__COLOR_VARIANTS:
            self.__color = color  # Цвет (защищенный атрибут)
        else:
            raise ValueError("Недопустимый цвет. Доступные цвета: " + ", ".join(Vehicle.__COLOR_VARIANTS))

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color in Vehicle.__COLOR_VARIANTS:
            # Обновляем цвет через специальный сервис
            self.__color = new_color
        else:
            raise ValueError("Недопустимый цвет. Доступные цвета: " + ", ".join(Vehicle.__COLOR_VARIANTS))


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)  # Вызов конструктора родительского класса

        # Создаём объект седана
        my_sedan = Sedan (owner="Иван", model="Toyota Camry", engine_power=150, color="красный")

        # Выводим информацию о седане
        my_sedan.print_info()

        # Пробуем изменить цвет
        try:
            my_sedan.set_color("синий")  # Меняем цвет через специальный сервис
            print("\nЦвет изменён.")
        except ValueError as e:
            print(e)

        # Печатаем обновленную информацию
        my_sedan.print_info()

        class Vehicle:
            __COLOR_VARIANTS = ['красный', 'синий', 'зеленый', 'черный', 'белый']  # Допустимые цвета

            def __init__(self, owner, model, engine_power, color):
                self.owner = owner  # Владелец транспорта
                self.__model = model  # Модель (защищенный атрибут)
                self.__engine_power = engine_power  # Мощность двигателя (защищенный атрибут)

                # Проверим, допустим ли цвет
                if color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
                    self.__color = color  # Цвет (защищенный атрибут)
                else:
                    raise ValueError("Недопустимый цвет. Доступные цвета: " + ", ".join(Vehicle.__COLOR_VARIANTS))

            def get_model(self):
                return f"Модель: {self.__model}"

            def get_horsepower(self):
                return f"Мощность двигателя: {self.__engine_power}"

            def get_color(self):
                return f"Цвет: {self.__color}"

            def set_color(self, new_color):
                if new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
                    self.__color = new_color
                else:
                    print(f"Нельзя сменить цвет на {new_color}")

            def print_info(self):
                print(self.get_model())
                print(self.get_horsepower())
                print(self.get_color())
                print(f"Владелец: {self.owner}")

        # Наследуемый класс Sedan
        class Sedan(Vehicle):
            __PASSENGERS_LIMIT = 5  # Ограничение на количество пассажиров

            def __init__(self, owner, model, engine_power, color):
                super().__init__(owner, model, engine_power, color)  # Вызов конструктора родительского класса

            def get_passengers_limit(self):
                return f"Лимит пассажиров: {Sedan.__PASSENGERS_LIMIT}"

            def print_info(self):
                super().print_info()  # Вывод информации из родительского класса
                print(self.get_passengers_limit())

        # Пример использования
        try:
            my_vehicle = Vehicle("Иван", "Тойота", 150, "синий")
            my_vehicle.print_info()
            my_vehicle.set_color("зеленый")
            print(my_vehicle.get_color())
            my_vehicle.set_color("жёлтый")  # Неправильный цвет

            my_sedan = Sedan("Анна", "Хонда", 180, "черный")
            my_sedan.print_info()
        except ValueError as e:
            print(e)