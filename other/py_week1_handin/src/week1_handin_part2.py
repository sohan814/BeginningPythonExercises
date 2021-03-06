'''
Created on Jan 4, 2012

@author: pfl
'''

def read_from_file( input_file_name = "output.dat"):
    input_signal = []
    
    file_handle = open( input_file_name, 'r')
    
    for this_line in file_handle.readlines():
        try:
            input_signal.append( (float(this_line.split()[0]), float(this_line.split()[1])) )
        except (ValueError,IndexError):
            pass
    
    file_handle.close()
    return input_signal

def ex_2_1(input_file_name = "output.dat"):
    return len( read_from_file(input_file_name))

def ex_2_2(input_file_name = "output.dat"):
    maxVal = 0.0
    minVal = 9e9
    for this_value in read_from_file(input_file_name):
        if maxVal < this_value[1]:
            maxVal = this_value[1]
        if minVal > this_value[1]:
            minVal = this_value[1]
    return (minVal,maxVal)

def ex_2_3_simple(input_file_name = "output.dat"):
    input_signal = read_from_file(input_file_name)
    
    
    while len(input_signal):
        old_value = input_signal.pop(0)
        new_value = 0
        while new_value = input_signal.pop(0):
            yield 1
    
    return 0
    

print (ex_2_1())
print (ex_2_2("output_sinus.dat"))
print (ex_2_3_simple("output_sinus.dat"))