from subprocess import Popen, PIPE
import os, re, sys

args = sys.argv

if len(args) == 2:
    EXECUTABLE = args[1]
else:
    print('wrong options.')
    exit(0)

LOG_PERCENTAGE = 100
PRINT_INPUT = False

input_directory_list = os.listdir('./in')
output_directory_list = os.listdir('./out')

if len(input_directory_list) != len(output_directory_list):
    print('there should be same number of input and output files.')
    exit(0)

def get_input_file_number(string):
    return int(re.match(r'input(\d+).txt', string).groups()[0])

input_directory_list.sort(key=get_input_file_number)

def difference(a, b):
    a = a.split('\n')
    b = b.split('\n')

    if a[-1] == '':
        a = a[:-1]
    if b[-1] == '':
        b = b[:-1]

    total_lines = max(len(a), len(b))
    if not total_lines:
        return 100, 0, a, b
    correct_lines = 0
    for i in range(min(len(a), len(b))):
        line1 = a[i].strip()
        line2 = b[i].strip()

        if line1 == line2:
            correct_lines += 1
        else:
            a[i] = '\n>' + line1 + '<\n'
            b[i] = '\n>' + line2 + '<\n'
            
    return int(correct_lines / total_lines * 100), (total_lines - correct_lines), a, b


for i, inp in enumerate(input_directory_list):
    out = inp.replace('input', 'output')
    process = Popen([EXECUTABLE], stdout=PIPE, stdin=PIPE)
    with open('./in/' + inp, 'r') as in_f:
        with open('./out/' + out) as out_f:
            in_text = in_f.read()
            out_text = out_f.read()
            output = process.communicate(input=bytes(in_text, 'utf-8'))[0].decode()
            diff, wrone_lines, output, out_text = difference(output, out_text)
            if(wrone_lines):
                print('#' * 70, end='\n\n')
            print(f'{out} -> {diff}%')

            if diff < LOG_PERCENTAGE:
                output = '\n'.join(output)
                out_text = '\n'.join(out_text)
                print(f'wrong lines: {wrone_lines}')
                PRINT_INPUT and print('>> input:\n\n' + in_text)
                print('\n>>> OUTPUT:\n\n' + output)
                print('\n>>> CORRECT OUTPUT:\n\n' + out_text + '\n\n' + '#' * 70)
            