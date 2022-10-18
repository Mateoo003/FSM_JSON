from datatest import input_test, output_test
from read import archive
import time

parameters_FSM = archive["parameters"][0]
inputs = archive["data_test"]["input"]
outputs = archive["data_test"]["output"]

def FSM_3M(state,input):
    if parameters_FSM["status_"+ str(state)]:
        for i in parameters_FSM["status_"+ str(state)]:
            if i["input"] == str(input):
                state = i["next_status"]
                output = i["output"]
    return state,output

outputs = ""
state = "0"

# for input in inputs[::-1]:
#     state, output = FSM_3M(int(state), int(input))
#     outputs += str(output)
 
count = 0

for i in inputs[::-1]: 
    print("Estado actual: "+state+". Entrada: "+i,end=". ")
    state,output=FSM_3M(state,i)
    output_test(output, count)
    print("Estado siguiente: "+state+". Salida: "+output)
    outputs += str(output)
    time.sleep(0.2)
    if len(inputs)-1 == count:
        if state == "0":
            output = "00"
            outputs += "00"
            count += 1
            for w in output:
                print("Estado actual: "+state+". Salida: "+ w)
                output_test(w, count)
                count += 1
                time.sleep(0.2)
        elif state == "1":
            output = "10"
            outputs += "10"
            count += 1
            for w in output:
                print("Estado actual: "+state+". Salida: "+ w)
                output_test(w, count)
                count += 1
                time.sleep(0.2)
        elif state == "2":
            output = "01"
            outputs += "01"
            count += 1
            for w in output:
                print("Estado actual: "+state+". Salida: "+ w)
                output_test(w, count)
                count += 1
                time.sleep(0.2)
    count += 1

# print('input: ', inputs, ', outputs: ', outputs[::-1])