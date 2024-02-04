 #File operation 
f_in = open("Text\Input\Input1a.txt", "r")
f_out = open("Text\Output\Output1a.txt", "w")
#read file 
read = f_in.readlines()
x=[]
for i in read:
    x+=i.split()
#If statement and text file writing
for i in x[1::]:
     if int(i)%2 !=0:
        f_out.write(f'{i} is an odd number \n')
     if int(i)%2 ==0:
        f_out.write(f'{i} is an even number \n')
        
f_in.close()
f_out.close()