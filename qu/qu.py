words_list=input("enter words").split()
words_tuple=tuple(words_list)
with open('qu01.txt','w') as data_file:
    data_file.write(f'list:{words_list}\n')
    data_file.write(f'tuple:{words_tuple}')
print('data written successfully')
with open('qu01.txt','r') as data_file:
    line_list=data_file.readline()
    line_tuple=data_file.readline()
    print(line_list)
    print(line_tuple)



