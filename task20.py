


# эта функция строит состояние из количества камней в кучах a и b, и истории шагов h
def get_state(a, b, h):
    return [a, b, h + ' -> (' +str(a) + ',' + str(b) + ')']

# эта функция возвращает список возможных ходов из состояния state
def player_step(state):
    first_heap = state[0]    
    second_heap = state[1]
    history = state[2]
    next_step1 = get_state(first_heap + 1, second_heap, history)
    next_step2 = get_state(first_heap * 2, second_heap, history)
    next_step3 = get_state(first_heap, second_heap + 1, history)
    next_step4 = get_state(first_heap, second_heap * 2, history)
    return [next_step1, next_step2, next_step3, next_step4]

# функция проверяет, закончилась ли игра состоянием state
def win(state):
    first_heap = state[0]    
    second_heap = state[1]
    result = (first_heap + second_heap >= 77)
    return result

# основная функция - проверяет выполняется ли условие задачи для начального состояния initial_state
def check_state(initial_state):
    
    # первый ход делает Петя
    # находим все возможные ходы Пети
    petay_steps = player_step(initial_state)

    # проверяем, если Петя может выиграть первым ходом, то это противоречит условию задачи и такое начальное сотояние не подходит
    for ps in petay_steps:
        if win(ps):
            print('Есть первый выигрышный ход:', ps[2])
            return False
        
    # проверяем ходы Пети по одному
    for ps in petay_steps:
        # второй ход делает Ваня
        # находим все возможные ходы Вани
        vanya_steps = player_step(ps)

        # проверяем, если Ваня может выиграть, то нам такой ход Пети не подходит, переходим к следующему ходу Пети
        vanya_can_win = False
        example = []
        for vs in vanya_steps:
            if win(vs):
                vanya_can_win = True
                example = vs
                break
        if vanya_can_win:
            print(example[2], 'Ваня может выиграть')
            continue

        # ищем, для любого хода Вани у Пети должен быть выигрышный ход
        win_states = 0
        example = []
        for vs in vanya_steps:
            petay_last_steps = player_step(vs)
            for pls in petay_last_steps:
                if win(pls):
                    win_states += 1
                    example = pls
                    break
        if win_states == len(vanya_steps):
            return True, example[2]
        
        print(ps[2], 'Нет выигрыша для', len(vanya_steps) - win_states, 'ходов Вани')

    return False        
    
solution = ''
for S in range(1, 70):
    print('')
    print('Проверяем S =', S)
    initial_state = [7, S, '(7,' + str(S) + ')']
    result = check_state(initial_state)
    if result:
        solution += 'S = ' + str(S) + ': ' + result[1] + '\n'
        
print('')
if solution:
    print('Выигрышная стратегия существует для следующих S:')
    print(solution)
else:
    print('Выигрышная стратегия не найдена')

        
        