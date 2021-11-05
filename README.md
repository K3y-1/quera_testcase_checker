# quera_testcase_checker
A python script to run any executable and pass test cases </br>
to it's stdin and compare stdout with correct output.

### proper way to use:
there should be two directories "in" and "out" in the same directory where main.py is located. </br>
"in" directory should contain testcase input files named input[number].text, </br>
"out" directory should contain testcase output files named output[number].text.

to run the script enter this command in commandline: </br>
`python main.py [executable path]`

for example: </br>
`python main.py ./a.out`
