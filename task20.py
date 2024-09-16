

def step(state):
    first_heap = state[0]    
    second_heap = state[1]
    history = state[2]
    next_step1 = [first_heap + 1, second_heap, history+'0']
    next_step2 = [first_heap * 2, second_heap, history+'1']
    next_step3 = [first_heap, second_heap + 1, history+'2']
    next_step4 = [first_heap, second_heap * 2, history+'3']
    return [next_step1, next_step2, next_step3, next_step4]

def win(state):
    first_heap = state[0]    
    second_heap = state[1]
    result = (first_heap + second_heap >= 77)
    return result

def check_state(initial_state):
    
    # первый ход делает Петя
    petay_steps = step(initial_state)

    for s in petay_steps:
        if win(s):
            return None
        
    # второй ход делает Ваня
    
    vanya_steps = []
    for s in petay_steps:
        vs = step(s)
        vanya_steps.extend(vs)
        
    for s in vanya_steps:
        if win(s):
            return None
        
    # третий ход опять Петя
    petay_steps2 = []
    for s in vanya_steps:
        there_is_a_win = False
        for ps in step(s):
            if win(ps):
                there_is_a_win = True
                break
        if not there_is_a_win:
            return None
        
    return 1
    
    
for S in range(1, 70):
    initial_state = [7, S, '']
    result = check_state(initial_state)
    if result is not None:
        print(S)
        

        
        