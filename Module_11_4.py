import inspect
from pprint import pprint

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def get_population(self):
        return self.population

    def __str__(self):
        return f"В городе {self.name} кол-во населения равно: {self.population}"

# Создание объекта класса City
city = City("Москва", 12615882)


# Вывод информации о городе
print(city)

population = city.get_population()
def introspection_info(city):
    info = {}
    info['obj_1'] = type('name')
    info['type_c'] = type(city)
    info['type_f'] = type(population)
    info['type_f_i'] = type(introspection_info)
    info['methods'] = dir(city)
    info['attributes_1'] = hasattr(city,'name')
    info['attributes_2'] = getattr(city,'population')
    setattr(city, 'population', 12615900)  # Установка нового значения для атрибута population
    print(f"Население города {city.name} увеличилось и составляет: {city.population}")
    module = inspect.getmodule(city)
    info['module'] = module.__name__

    return info
city_info = introspection_info(city)
pprint(city_info)
