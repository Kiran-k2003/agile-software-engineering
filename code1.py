grid = [
    [8,2,7,5,3,6,9,4,1], 
    [5,1,6,8,4,9,3,2,7],
    [9,4,3,1,7,2,6,5,8],
    [2,7,1,3,9,4,8,6,5],
    [3,6,5,7,1,8,2,9,4],
    [4,9,8,6,2,5,1,7,3],
    [6,5,2,4,8,3,7,1,9],
    [1,8,9,2,5,7,4,3,6],
    [7,3,4,9,6,1,5,8,2]

]

def check_row(grid,row_no,element):
 for column in range(9):
     print(grid[row_no][column])
     if grid[row_no][column]==element:
        return True
 return False
    
print(check_row(grid,0,8))

def check_column(grid,column_no,element):
 for row in range(9):
     print(grid[row][column_no])
     if grid[row][column_no]==element:
        return True
 return False
    
print(check_column(grid,0,8))

def check_diag(grid):
   for i in range(9):
      print(grid[i][i])

check_diag(grid)


for row in range (3):
   for col in range (3):
      print("row:",row,"col:",col,"elem:",grid[row][col])

'''
 box_row=0
 box_column=3
 for row in range (3):
     for col in range (3):
       print("row:",row+box_row,"col:",col+box_column,"elem:",grid[row+box_row][col+box_column])
'''

def check_box(grid,box_row,box_column,elem): 
 
 for row in range (3):
    for col in range (3):
        print("row:",row+box_row,"col:",col+box_column,"elem:",grid[row+box_row][col+box_column])      
        if grid[row+box_row][col+box_column]==elem:
         return True
    return False

print(check_box(grid,0,3,9))
      

      
def check_one_row_all_elem(grid, row_no):
  for elem in range(1,10):
     if check_row(grid,row_no,elem)==False:
        
            print("hello")
            return False
        
     return True

print(check_one_row_all_elem(grid,1))

def check_one_column_all_elem(grid,column_no):
    for elem in range(1,10):
        if check_column(grid,column_no,elem)==False:
         
            print("hello")
            return False

    return True

print(check_one_column_all_elem(grid,1))


def check_one_box_all_elem(grid,box_row,box_column):
    for elem in range(1,10): 
        if check_box(grid,box_row,box_column,elem)==False:
            print("hello")
            return False
         
    return True  

print(check_one_column_all_elem(grid,1)) 
