from read import archive

parameters_FSM = archive["parameters"][0]
inputs = archive["data_test"]["input"]

def FSM_3M(state,input):
    if parameters_FSM["status_"+ str(state)]:
        for i in parameters_FSM["status_"+ str(state)]:
            if i["input"] == str(input):
                state = i["next_status"]
                output = i["output"]
    return state,output

outputs = ""
state = "0"

for input in inputs[::-1]:
    state, output = FSM_3M(int(state), int(input))
    outputs += str(output)

if state == "0":
    outputs += "00"
elif state == "1":
    outputs += "10"
elif state == "2":
    outputs += "01"

print('input: ', inputs, ', outputs: ', outputs[::-1])