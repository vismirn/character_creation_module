from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return
    return (f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return
    return (f'{char_name} нанёс урон противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return
    return (f'{char_name} нанёс урон противнику равный {5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} применил «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил «Защита {10 + 30}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
        print('Потренируйся управлять своими навыками.')
        text_vved = 'Введи одну из команд: attack — чтобы атаковать противника'
        text_chtoby = 'defence — чтобы блокировать атаку противника или'
        text_spec = 'special — чтобы использовать свою суперсилу.'
        print(f'{text_vved}'+{text_chtoby}+{text_spec})
        print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        text_vvedi_nazv = 'Введи название персонажа, за которого хочешь'
        text_igrat = 'играть: Воитель — warrior, Маг — mage, Лекарь — healer: '
        char_class = input(f'{text_vvedi_nazv}+{text_igrat}')
        if char_class == 'warrior':
            text_voit = 'Воитель — дерзкий воин ближнего боя. Сильный, '
            text_vynos_i_otv = 'выносливый и отважный.'
            print(f'{text_voit}+{text_vynos_i_otv}')
        if char_class == 'mage':
            text_mag = 'Маг — находчивый воин дальнего боя. '
            text_oblad = 'Обладает высоким интеллектом.'
            print(f'{text_mag}+{text_oblad}')
        if char_class == 'healer':
            text_lek = 'Лекарь — могущественный заклинатель. '
            text_cher = 'Черпает силы из природы, веры и духов.'
            print(f'{text_lek}+{text_cher}')
        text_nazhmi = 'Нажми (Y), чтобы подтвердить выбор, или любую другую'
        text_knop = ' кнопку, чтобы выбрать другого персонажа '
        approve_choice = input(f'{text_nazhmi}+{text_knop}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
