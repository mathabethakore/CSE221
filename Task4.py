#Input/Output
f_in = open("Text\Input\Input4.txt", "r")
f_out = open("Text\Output\Output4.txt", "w")
#Reading full text file
read = f_in.readlines()

num_trains = (read[0]).strip("\n")
#debug print(num_trains)
schedule=[]

#creating a list of the schedule
for i in read[1::]:
    schedule.append(i.strip("\n"))

#using recursive function 
def sorter(arr, count = 0):
    if count == (int(num_trains)-1):
        return(schedule)
    #sort by name
    if arr[count].split()[0] > arr[count+1].split()[0]:
        arr[count], arr[count+1] = arr[count+1], arr[count]
        return(sorter(arr, count = 0))
    #sort by time if name is same
    elif arr[count].split()[0] == arr[count+1].split()[0]:
        if arr[count].split()[-1] > arr[count+1].split()[-1]:
            arr[count], arr[count+1] = arr[count+1], arr[count]
            return(sorter(arr, count = 0))
        else:
            return(sorter(arr, count+1))
    else:
        return(sorter(arr, count+1))

sorter(schedule)


#writing to text file
for i in schedule:
    f_out.write(f'{i}\n')
f_out.close()
f_in.close()

