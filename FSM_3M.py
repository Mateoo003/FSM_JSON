def FSM_3M(state, input):
    if state == 0:
        if input == 0:
            output = 0
            state = 0
        elif input == 1:
            output = 1
            state = 1
    elif state == 1:
        if input == 0:
            output = 1
            state = 0
        elif input == 1:
            output = 0
            state = 2
    elif state == 2:
        if input == 0:
            output = 0
            state =1
        elif input == 1:
            output = 1
            state = 2
    return state, output

outputs = ""
inputs = "101110110"
state = "0"
for input in inputs[::-1]:
    state, output = FSM_3M(int(state), int(input))
    outputs += str(output)

if state == 0:
    outputs += "00"
elif state == 1:
    outputs += "10"
elif state == 2:
    outputs += "01"

print('input: ', inputs, ', outputs: ', outputs[::-1])
