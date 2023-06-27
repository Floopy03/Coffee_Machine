from count_time import countdown


class Coffee_Machine:
    def __init__(self, name, types_coffee, ingredients):
        self.name = name
        self.types_coffee = types_coffee
        self.ingredients = ingredients


    def available_coffee(self):
        print(f'Кофемашина {self.name} может приготоваить для Вас:')
        for num, each in enumerate(self.types_coffee, 1):
            print(f'  {num}. {each.name} ')



    def pick_coffee(self):
        self.available_coffee()

        num_choice = input('\nВыберите номер кофе из списка: ')
        choice = self.types_coffee[int(num_choice)-1]                   # задали переменную для выбраного кофе по индексу                                   
        
        
        ingredient_error = False                    # задаем флаг для проверки срабатывания break

        for each in self.ingredients:                   # для каждого элемента в словаре ингридиентов
            if each in choice.ingredients:                  # проверка необходимых ингридиентов для выбраного кофе
                
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


    

class Coffee:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


latte = Coffee('Latte', ingredients = {'Water' : 1, 'Coffee' : 1, 'Milk' : 1})
cappuccino = Coffee('Cappuccino', ingredients = {'Water' : 1, 'Coffee' : 2, 'Milk' : 1})
americano = Coffee('Americano', ingredients = {'Water' : 1, 'Coffee' : 1})
espresso = Coffee('Espresso', ingredients = {'Water' : 1, 'Coffee' : 1})
irish = Coffee('Irish Coffee', ingredients = {'Water' : 1, 'Coffee' : 1, 'Whiskey' : 1})


philips = Coffee_Machine('Philips', [latte, cappuccino, americano, espresso, irish], 
                         ingredients = {'Water' : 10, 'Coffee' : 1, 'Milk' : 7, 'Whiskey' : 4})   

