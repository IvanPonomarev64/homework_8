import os

os.chdir(r'D:\Нетология\Homework_8\myfolder') 

def merging_files():
    list_files_txt =[]
    my_dict = {}
    for files in os.listdir("D:\Нетология\Homework_8\myfolder"): 
        if files.endswith(".txt"):
            list_files_txt.append(files)
            for i in list_files_txt[::-1]:
                with open(i, encoding='utf-8') as files:
                    list_strings = files.readlines()
                    my_dict[i] = (len(list_strings), list_strings)
    sort_dict ={}               
    list_for_sort = list(my_dict.items())
    list_for_sort.sort(key=lambda i: i[1])
    for i in list_for_sort:
        sort_dict[i[0]] = i[1]

    with open("file4.txt", "w", encoding='utf-8') as fail:
        for key, value in sort_dict.items():
            fail.write(f'{key}\n{value[0]}\n{"".join(value[1])}\n')

merging_files()        




  

        