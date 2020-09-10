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


#[5]闭包的概念
def outter():
    name = "jason"
    def inner():
        new_name = name+".new"
        print(new_name)
    return inner
#print("此时调用outter函数，返回的是inner函数的内存地址：\n", outter())
inner = outter()
#inner()


#[6]传入N个数，以字典形式返回最大值与最小值
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

# [9] 编写装饰器，为多个函数添加认证功能，登录一次，后续函数无需输入用户名和密码
file_name = r"J:\renzhongshu\自玩脚本\user_file.txt"
temp_filename = r"J:\renzhongshu\自玩脚本\temp_user_file.txt"


def set_login_status(status):
    f_status = open(file_name, "r+")
    temp_status = open(temp_filename, "w+")
    for k in f_status:
        print("来自set_login_status:", k)
        if "login" in k:
            login_info = k.split(":")
            print(login_info)
            new_status = k.replace(login_info[1], status+"\n")
            # print("new_status:", new_status)
            temp_status.write(new_status)
        else:
            temp_status.write(k)

    f_status.close()
    temp_status.close()
    os.replace(temp_filename, file_name)


def login(func):
    f = open(file_name, "r+")
    name_list = []
    password_list = []
    login_status = []
    for i in f:
        if "username" in i:
            name_list = i.split(":")
            new_i = name_list[1].strip()
            name_list[1] = new_i
        elif "password" in i:
            password_list = i.split(":")
        elif "login" in i:
            login_status = i.split(":")
            new_j = login_status[1].strip()
            login_status[1] = new_j
            print("login_status:", login_status)
        else:
            print("No Matches!")
    # print(name_list)
    # print(password_list)
    # print(login_status)
    # print(name_list, password_list)
    f.close()

    def check_user_info(*args, **kwargs):
        if login_status[1] == "True":
            print("已经登录！")
            func(*args, **kwargs)
        elif login_status[1] == "False":
            print("未曾登录！")
            input_name = input("请输入用户名")
            input_password = input("请输入密码")
            print("ori_login_status[1]", login_status[1])
            if input_name == name_list[1] and input_password == password_list[1]:
                print("登录成功！")
                login_status[1] = "True"
                print("login_status[1]:", login_status[1])
                set_login_status(login_status[1])
                print("login_status[1] again:", login_status[1])
                func(*args, **kwargs)
            else:
                print("请重新输入！")
        else:
            print(login_status[1])
            sys.exit("gaga_men")
    return check_user_info


@login
def shot_game():
    print("===射击游戏===")


@login
def racing_game():
    print("===赛车游戏===")


racing_game()
shot_game()
