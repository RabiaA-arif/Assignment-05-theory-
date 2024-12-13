matrices_list1 =[[1,4,9,],[3,4,7],[5,2,8]]


matrices_list2 =[[7,3,9],[8,12,6],[5,66,22]]


result_matricess =[[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(matrices_list1)):
    for j in range(len(matrices_list1[0])):
        result_matricess[i][j] = matrices_list1[i][j] + matrices_list2[i][j]
        print(result_matricess)
        
        
print("hello rabia")