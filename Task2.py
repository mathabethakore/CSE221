f_in = open("Text\Input\Input2.txt", "r")
f_out = open("Text\Output\Output2.txt", "w")
read = f_in.readlines()
x=[]
for i in read:
    x+=i.strip().split("\n") 

#assigning the array from input
arr = x[1].split(" ")
def bubbleSort(arr): 
    flag = True
    
    for i in range(len(arr)): 
        for j in range(len(arr)-i-1): 
         if int(arr[j]) > int(arr[j+1]): 
            flag = False
            arr[j], arr[j+1] = arr[j+1], arr[j]
         if flag == True:
            break #otherwise the sorting algorithm continues as it is
          
    for i in arr:
        f_out.write(f'{i} ')
bubbleSort(arr)
f_out.close()
f_in.close()




