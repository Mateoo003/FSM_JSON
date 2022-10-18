from read import archive

input_data_test = archive["data_test"]["input"]
output_data_test = archive["data_test"]["output"]
# print(archive["data_test"]["input"])

input_cont = 0
output_cont = 0

def input_test(bits):
    global input_cont
    for i in bits[::-1]:
        print(i)
        assert i == str(i), f'The input requiered is {i} in {input_cont}'
        input_cont+=1
        if len(input_data_test) <= input_cont:
            raise Exception(f'No more test data')
    return input_data_test

def output_test(bits):
    global output_cont
    for i in bits[::-1]:
        print(i)
        assert i == str(i), f'The input requiered is {i} in {output_cont}'
        output_cont+=1
        if len(output_data_test) <= output_cont:
            raise Exception(f'No more test data')
    return output_data_test