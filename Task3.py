#Input/Output
f_in = open("Text\Input\Input3.txt", "r")
f_out = open("Text\Output\Output3.txt", "w")
#Reading full text file
read = f_in.readlines()

num_students = int(read[0].strip())
ids = read[1].strip().split()
marks = read[2].strip().split()

#joining marks and id of corresponding values
marksheet = []
for i in range((num_students)):
    x = [ids[i],marks[i]]
    marksheet.append(x)

#function to sort by marks and id 
def selection_sort(arr):
    for i in range(num_students):
        max_index = i
        for j in range(i + 1, num_students):
            # Compare marks
            if marksheet[j][1] > marksheet[max_index][1]:
                max_index = j
            # If marks are equal, compare IDs
            elif marksheet[j][1] == marksheet[max_index][1] and marksheet[j][0] < marksheet[max_index][0]:
                max_index = j
        # Swap the found minimum element with the first element
        marksheet[i], marksheet[max_index] = marksheet[max_index], marksheet[i]

# Call the selection sort function
selection_sort(marksheet)
#writing to text file
                   
for i in marksheet:
      f_out.write(f'ID: {i[0]} Mark: {i[1]} \n')
f_out.close()