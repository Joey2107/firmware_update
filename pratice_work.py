#[1] 动态传参，计算所有参数的和
def func_add(*args, **kwargs):
    temp_args = 0
    temp_kwargs = 0
    for i in args:
        i = temp_args + i
        temp_args = i
        print("i:", i)
    for j in kwargs.values():
        j = temp_kwargs + j
        temp_kwargs = j
        print("j:", j)
    print("args和kwargs之和：", i + j)
# func_add(1, 2, 3, 4, 5, num_1=99, num_2=100)


#[2] 传入文件名和要修改的内容，执行函数完成批量修改
import os
def modify_content(filename, target_str, sub_str):
    new_filename = filename + ".new"
    f = open(filename, "r")
    new_f = open(new_filename, "w")
    for i in f:
        if target_str in i:
            new_i = i.replace(target_str, target_str + sub_str)
            new_f.write(new_i)
        else:
            new_f.write(i)
    f.close()
    new_f.close()
    os.replace(new_filename, filename)
# modify_content("event_check.log", "Selected", " Wrong!")


#[3]检查输入内容是否存在空内容，输入内容数据类型为字符、list、dict
#测试数据:
{" name": "jason", "age": 20}
[1, 2, 3, "name"]
"桂林山水甲天下"
def check_content():
    blank_space = " "
    user_cont = input("Please input what you want to say:")
    if "[" in user_cont or "{" in user_cont:
        new_cont = eval(user_cont)
    #print(new_cont)
    #print(type(new_cont))
        if type(new_cont) is list:
            for i in new_cont:
                if blank_space in str(i):
                    print("There is blank space.")
                else:
                    print("There is no blank space.")
        else:
            for j in new_cont.keys():
                if blank_space in str(new_cont[j]):
                    #避免元素存在数字（非可迭代对象）
                    print("There is blank space.")
                else:
                    print("There is no blank space.")
    else:
        if blank_space in user_cont:
            print("There is blank space.")
        else:
            print("There is no blank space.")

#check_content()


#[4] 检查传入字典的每一个value的长度（字符、list、dict），并将新内容传给调用函数
dict_name = {"jason": None, "class": None, "age": None, "hobby": None}
def check_dictvalue(*args):
    for i in args:
        #print(i)
        if len(str(i)) > 2:
            temp_j = ""
            temp_k = ""
            j_list = []
            for j in i:
                j_list.append(j)
            j_list = j_list[0:4]
            for k in j_list:
                k = temp_k +k
                temp_k = k
            for l in dict_name.keys():
                if dict_name[l] is None:
                    dict_name[l] = k
                    #print(k)
                    print(dict_name[l])
                    break
        else:
            for j in dict_name.keys():
                if dict_name[j] is None:
                    dict_name[j] = i
                    print(j)
                    print(dict_name[j])
                    break
                else:
                    pass
    print(dict_name)

#check_dictvalue("male", "junior", 20)


#闭包的概念
def outter():
    name = "jason"
    def inner():
        new_name = name+".new"
        print(new_name)
    return inner
#print("此时调用outter函数，返回的是inner函数的内存地址：\n", outter())
inner = outter()
#inner()


#传入N个数，以字典形式返回最大值与最小值
#1, 2, 3, 4, 5, 6, 7
def compare_num():
    data = []
    user_input = input("Please input numbers:")
    for i in user_input:
        data.append(i)
    min_num = 0
    min_val = data[min_num]
    temp_mid = min_val
    cond = True
    while cond:
        if min_num < len(data):
            if temp_mid < data[min_num]:
                temp_mid= data[min_num]
                print(current_min)
                print(data[min_num])
            else:
                current_max = min_val
                print(current_max)
            min_num += 1
        else:
            cond = False

compare_num()