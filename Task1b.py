f_in = open("Text\Input\Input1b.txt", "r")
f_out = open("Text\Output\Output1b.txt", "w")
read = f_in.readlines()
x=[]
for i in read:
    x+=i.strip().split("\n")

#num_operations=int(x[0])

#if condition statements
    
for i in x[1::]:
    calculation = list(i.strip().split(" "))
    if calculation[2] == "+":
        f_out.write(f'The result of {calculation[1]} {calculation[2]} {calculation[3]} is {int(calculation[1])+int(calculation[3])}\n')
    if calculation[2] == "-":
        f_out.write(f'The result of {calculation[1]} {calculation[2]} {calculation[3]} is {int(calculation[1])-int(calculation[3])}\n')
    if calculation[2] == "*":
            f_out.write(f'The result of {calculation[1]} {calculation[2]} {calculation[3]} is {int(calculation[1])*int(calculation[3])}\n')
    if calculation[2] == "/":
            f_out.write(f'The result of {calculation[1]} {calculation[2]} {calculation[3]} is {int(calculation[1])/int(calculation[3])}\n')    

f_in.close()
f_out.close()