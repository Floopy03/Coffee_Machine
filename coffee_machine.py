from count_time import countdown


class Coffee_Machine:
    def __init__(self, name, types_drink, ingredients):
        self.name = name
        self.types_drink = types_drink
        self.ingredients = ingredients


    def available_drinks(self):
        for num, i in enumerate(self.types_drink, 1):                   
            print(f'{num}. {i[0].__class__.__name__}')                  # обращаясь к каждому первому элементу списка, выводим название его класса 
        choice_drink = input('Выберите напиток : ')

        print(f'Кофемашина {self.name} может приготоваить для Вас:')

        for num, each in enumerate(self.types_drink[int(choice_drink)-1], 1):                   # перебираем список по выбраному индексу (choice_drink)
            print(f'  {num}. {each.name} ')

        return self.types_drink[int(choice_drink)-1]                    # Возвращаем значение выбраного списка, что бы использовать его в некс функции



    def pick_drink(self):
        drink = self.available_drinks()                 # Вызываем функцию (available_drinks) и сразу сохраняем в переменную ее return


        num_choice = input('\nВыберите номер напитка из списка: ')
        choice = drink[int(num_choice)-1]                   # задали переменную для выбраного напитка по индексу                                   
        print(choice.name)
        
        ingredient_error = False                    # задаем флаг для проверки срабатывания break

        for each in self.ingredients:                   # для каждого элемента в словаре ингридиентов
            if each in choice.ingredients:                  # проверка необходимых ингридиентов для выбраного напитка
                
                if self.ingredients[each] >= choice.ingredients[each]:                  # проверка наличия необходимого ингридиента в автомате
                    self.ingredients[each] -= choice.ingredients[each]                  # вычитаем использованные ингридиенты
                    # print(f'Использую : {each}({choice.ingredients[each]})')

    
                else:
                    print(f'\nВ автомате недостаточно {each}.\nПриготовление остановлено.')

                    ingredient_error = True                 # изменяем значение флага т.к. break сработает
                    break


        if not ingredient_error:                    # если флаг False (break не сработал), выполняем следующий код         
            print(f'\nГотовлю --> {choice.name}.\n')
            countdown()      
            print(f'\nВаш {choice.name} готов, можете забрать стаканчик.')    


class Drink:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    

class Coffee(Drink):
    list_coffee = []


class Tea(Drink):
    list_tea = []


Coffee.list_coffee.append(Coffee('Latte', ingredients = {'Water' : 1, 'Coffee' : 1, 'Milk' : 1}))
Coffee.list_coffee.append(Coffee('Cappuccino', ingredients = {'Water' : 1, 'Coffee' : 2, 'Milk' : 1}))
Coffee.list_coffee.append(Coffee('Americano', ingredients = {'Water' : 1, 'Coffee' : 1}))
Coffee.list_coffee.append(Coffee('Espresso', ingredients = {'Water' : 1, 'Coffee' : 1}))
Coffee.list_coffee.append(Coffee('Irish Coffee', ingredients = {'Water' : 1, 'Coffee' : 1, 'Whiskey' : 1}))


Tea.list_tea.append(Tea('Black Tea', ingredients = {'Water' : 1, 'Tea leaves' : 1}))
Tea.list_tea.append(Tea('Green Tea', ingredients = {'Water' : 1, 'Tea leaves' : 1}))
Tea.list_tea.append(Tea('Herbal Tea', ingredients = {'Water' : 1, 'Tea leaves' : 2}))


philips = Coffee_Machine('Philips', [Coffee.list_coffee, Tea.list_tea], 
                         ingredients = {'Water' : 10, 'Coffee' : 4, 'Milk' : 7, 'Whiskey' : 4, 'Tea leaves' : 5})   




philips.pick_drink()