print("随机抽取[版本号：1.0] 内部版本号[1.0.build-77.9]")
print("作者：GitHub_huonanwholovecomputer © 不保留任何权利。")
print("")
# 随机函数
import random
# 时间函数
import time
# 打字函数
import sys
# 检测键盘按键事件（跨平台）
import keyboard
# 系统时间函数
import datetime
# 日志模块
import logging
# 检测错误的模块
import sys
# 与操作系统进行交互的模块
import os
# 尝试以下代码
try:
    # 配置日志记录
    logging.basicConfig(filename='错误日志.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # 将标准错误输出重定向到日志文件
    sys.stderr = open('错误日志.log', 'a')
    # 英语课专用随机抽取名单
    students_English_list = ["白宇杰","陈俊昌","陈玉","崔欣悦","崔知轩","窦可冉","高怡浩","韩怡悦","郝浩然","郝晔妮","贺佳美","胡峰","霍楠","霍俞达","雷航","雷淼","雷旭阳","李芊雨","李媛媛","李泽翔","刘杰","刘奕含","刘于楠","马赫","马佳雪","马玲丹","马润杰","马谢楠","马跃","米庆","苗夏雨","任璠","王浩森","王浩宇","王慧娟","王美丹","王森","王文涛","王欣瑜","王玙贴","杨慧仪","袁博","张靖雨","张坤","张翔荣","张宇航","张雨萌","朱佳乐"]
    # 常规随机抽取名单
    students_common_list = ["白宇杰","陈俊昌","陈玉","崔欣悦","崔知轩","窦可冉","冯宇乐","高怡浩","韩怡悦","郝浩然","郝晔妮","贺佳美","胡峰","霍楠","霍俞达","雷航","雷淼","雷文杰","雷旭阳","李芊雨","李媛媛","李泽翔","刘杰","刘奕含","刘于楠","马赫","马佳雪","马玲丹","马润杰","马谢楠","马跃","米庆","苗夏雨","任璠","王浩森","王浩宇","王慧娟","王美丹","王森","王文涛","王欣瑜","王玙贴","杨慧仪","袁博","张靖雨","张坤","张文杰","张翔荣","张宇航","张雨萌","朱佳乐"]
    # 学生名单的选择
    global students_list
    global file_name
    def random_delay(min_delay, max_delay):
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
    true = True
    while true:
        print("---------------------------------------------")
        print("请选择学生名单：")
        print("")
        print("【1】 英语课专用（无日语学生）")
        print("")
        print("【2】 常规（全体学生）")
        print("---------------------------------------------")
        key = keyboard.read_key()
        if key == "1":
            students_list = students_English_list
            file_name = "英语_记录.txt"
            s = "已选择【1】，进入：英语课专用的随机抽取(无日语学生)"
            for char in s:
                print(char, end="")
                sys.stdout.flush()
                time.sleep(0.01)
            break
        elif key == "2":
            students_list = students_common_list
            file_name = "常规_记录.txt"
            s = "已选择【2】，进入：常规随机抽取(全体学生)"
            for char in s:
                print(char, end="")
                sys.stdout.flush()
                time.sleep(0.01)
            break
        else:
            print("无效选择！")
            time.sleep(0.5)
    time.sleep(0.25)
    print("")
    print("")
    print("若需要检查特定的学生是否存在与学生名单中或整个名单的完整性，请输入“jc”或者“JC”或者“检查”")
    #抽取部分
    true = True
    while true:
        global recorded_students
        students = students_list
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                recorded_students = set(line.split()[0] for line in file)
            students = [student for student in students if student not in recorded_students]
            if not students:
                print("")
                print("名单中的学生已空，已初始化学生名单并清空[file_name]")
                students = students_list
                with open(file_name, 'r+', encoding='utf-8') as file:
                    file.truncate()
                    recorded_students = set(line.split()[0] for line in file)
        except FileNotFoundError:
            print(f"文件 {file_name} 未找到。")
        except Exception as e:
            print(f"读取文件时出错: {e}")
        print("---------------------------------------------")
        A = input("请输入需要抽取的学生个数：")
        if A.isdigit():
            selection_students = []
            cycle_count = 0
            number_of_shuffles = 0
            A = int(A)
            if A > len(students):
                print("")
                print("提示：需要抽取的学生个数超过学生总数！")
                time.sleep(0.1)
                print("")
                print("请重新抽取..")
                time.sleep(0.2)
            else:
                if A <= 6:
                    time.sleep(0.1)
                    print("")
                    print("输入学生个数小于等于6，运行了if A <= 6")
                    random.shuffle(students)
                    time.sleep(0.1)
                    print("打乱了1次学生列表")
                    while cycle_count < A:
                        cycle_count += 1
                        selection_student = random.choice(students)
                        if selection_student in selection_students:
                            A += 1
                        else:
                            selection_students.append(selection_student)
                            now = datetime.datetime.now()
                            with open(file_name, 'a', encoding='utf-8') as file:
                                file.write(selection_student + ' ' + now.strftime('%Y-%m-%d %H:%M:%S') + '\n')
                else:
                    time.sleep(0.1)
                    print("")
                    print("输入学生个数大于6，运行了else")
                    while cycle_count < A:
                        random.shuffle(students)
                        cycle_count += 1
                        if cycle_count % 5 == 0:
                            number_of_shuffles += 1
                            random.shuffle(students)
                            time.sleep(0.1)
                            print("打乱了",number_of_shuffles,"次学生列表")
                        selection_student = random.choice(students)
                        if selection_student in selection_students:
                            A += 1
                        else:
                            selection_students.append(selection_student)
                            now = datetime.datetime.now()
                            with open(file_name, 'a', encoding='utf-8') as file:
                                file.write(selection_student + ' ' + now.strftime('%Y-%m-%d %H:%M:%S') + '\n')
                time.sleep(0.1)
                print("")
                print("最终的抽取结果：【",selection_students,"】")
        elif A in ["C", "c", "clean", "Clean"]:
            students = students_list
            with open(file_name, 'r+', encoding='utf-8') as file:
                file.truncate()
            print("")
            print("已清空",file_name,"中的内容！")
        elif A in ["记录", "jl"]:
            if recorded_students:
                print("")
                print("已经记录的学生",recorded_students)
                time.sleep(0.1)
                print("")
                print("共记录",(len(recorded_students)),"名学生")
                time.sleep(0.1)
                print("")
                print("还有",len(students_list),"-",len(recorded_students),"=",len(students_list)-len(recorded_students),"名学生未被抽取")
                time.sleep(0.25)
                print("")
                print("本次抽取默认会跳过已经记录的学生，输入“C”或“c”可清除[file_name]中的学生抽取记录")
            if not recorded_students:
                time.sleep(0.25)
                print("")
                print("[file_name]中没有学生的抽取记录，本次抽取将不会去除任何学生")
        elif A in ["JC", "jc", "检查","jiancha"]:
            print("")
            print("您已进入名单检查程序！")
            time.sleep(1)
            true = True
            while true:
                print("---------------------------------------------")
                time.sleep(0.1)
                print("请选择检查模式：")
                print("")
                time.sleep(0.1)
                print("【1】 检查单个学生是否存在于随机抽取名单中")
                print("")
                time.sleep(0.1)
                print("【2】 检查整个随机抽取名单是否正常")
                print("")
                time.sleep(0.1)
                print("【3】 退出检查程序")
                time.sleep(0.1)
                print("---------------------------------------------")
                key = keyboard.read_key()
                if key == "1":
                    print("已进入模式【1】 检查单个学生是否存在于随机抽取名单中")
                    time.sleep(0.25)
                    print("")
                    print("Tip: 输入“quit”或“q”或“tuichu”或“退出”可退出模式【1】")
                    time.sleep(1)
                    true = True
                    while true:
                        print("")
                        check_student = input("请输入需要检查的学生：")
                        time.sleep(0.5)
                        if check_student in students_list:
                            print("")
                            print("✓ 恭喜！学生：“"f"{check_student}”存在于学生列表中！")
                            time.sleep(0.5)
                        elif check_student in ["quit", "q", "tuichu", "退出"]:
                            print("")
                            print("已退出模式【1】")
                            break
                        else:
                            print("")
                            print("× 警告！学生：“"f"{check_student}”不存在于学生列表中！")
                            time.sleep(0.5)
                elif key == "2":
                    # 英语名单检查部分
                    print("已进入模式【2】 检查整个随机抽取名单是否正常")
                    time.sleep(0.25)
                    print("")
                    print("准备检查英语课专用的随机抽取名单",end="")
                    s =  "......"
                    for char in s:
                        print(char, end="")
                        sys.stdout.flush()
                        time.sleep(0.1)
                    print("")
                    print("")
                    time.sleep(1)
                    check_students_English_list = ["白宇杰","陈俊昌","陈玉","崔欣悦","崔知轩","窦可冉","高怡浩","韩怡悦","郝浩然","郝晔妮","贺佳美","胡峰","霍楠","霍俞达","雷航","雷淼","雷旭阳","李芊雨","李媛媛","李泽翔","刘杰","刘奕含","刘于楠","马赫","马佳雪","马玲丹","马润杰","马谢楠","马跃","米庆","苗夏雨","任璠","王浩森","王浩宇","王慧娟","王美丹","王森","王文涛","王欣瑜","王玙贴","杨慧仪","袁博","张靖雨","张坤","张翔荣","张宇航","张雨萌","朱佳乐"]
                    def find_duplicates(list_name, input_list):
                        seen = set()
                        duplicates = set()
                        for item in input_list:
                            if item in seen:
                                duplicates.add(item)
                            else:
                                seen.add(item)
                        if duplicates:
                            print(f"× {list_name}中有重复的学生：['{', '.join(map(str, duplicates))}']")
                            print("")
                        else:
                            print(f"✓  {list_name}中没有重复的学生")
                            print("")
                    find_duplicates("[英语课专用随机抽取名单]", students_English_list)
                    random_delay(0.1, 1)
                    find_duplicates("[英语课专用随机抽取核对名单]", check_students_English_list)
                    random_delay(0.1, 1)
                    missing_students = [student for student in check_students_English_list if student not in students_English_list]
                    extra_students = [student for student in students_English_list if student not in check_students_English_list]
                    random_delay(0.1, 1)
                    print("[英语课专用的随机抽取名单]          总人数：",len(students_English_list))
                    random_delay(0.1, 1)
                    print("")
                    print("[英语课专用的随机抽取核对名单]      总人数：",len(check_students_English_list))
                    random_delay(0.1, 1)
                    if not missing_students and not extra_students:
                        print("")
                        print("✓  [英语课专用的随机抽取名单]与[英语课专用的随机抽取核对名单]一致")
                    if missing_students:
                        print("")
                        print("× 警告！[英语课专用的随机抽取名单]与[英语课专用的随机抽取核对名单]不一致！")
                        print("")
                        print("[英语课专用的核对名单]中缺失学生：",missing_students)
                    if extra_students:
                        print("")
                        print("× 警告！[英语课专用的随机抽取名单]与[英语课专用的随机抽取核对名单]不一致！")
                        print("")
                        print("[英语课专用的随机抽取名单]中多余学生：",extra_students)
                    if len(students_English_list) == len(check_students_English_list) == 48:
                        random_delay(0.1, 1)
                        print("")
                        print("✓  [英语课专用的随机抽取名单]与[英语课专用的随机抽取核对名单]的人数均符合预期！")
                    else:
                        random_delay(0.1, 1)
                        print("")
                        print("× 警告[英语课专用的随机抽取名单]与[英语课专用的随机抽取核对名单]的人数至少一个不符合预期！")
                        time.sleep(1)
                        print("")
                        print("请检查英语课随机抽取名单是否完整！")
                        time.sleep(1)
                    # 过渡
                    s =  "---------------------------------------------"
                    for char in s:
                        print(char, end="")
                        sys.stdout.flush()
                        time.sleep(0.01)
                    # 常规名单检查部分
                    print("")
                    print("准备检查常规随机抽取名单",end="")
                    s =  "......"
                    for char in s:
                        print(char, end="")
                        sys.stdout.flush()
                        time.sleep(0.1)
                    time.sleep(1)
                    check_students_common_list = ["白宇杰","陈俊昌","陈玉","崔欣悦","崔知轩","窦可冉","冯宇乐","高怡浩","韩怡悦","郝浩然","郝晔妮","贺佳美","胡峰","霍楠","霍俞达","雷航","雷淼","雷文杰","雷旭阳","李芊雨","李媛媛","李泽翔","刘杰","刘奕含","刘于楠","马赫","马佳雪","马玲丹","马润杰","马谢楠","马跃","米庆","苗夏雨","任璠","王浩森","王浩宇","王慧娟","王美丹","王森","王文涛","王欣瑜","王玙贴","杨慧仪","袁博","张靖雨","张坤","张文杰","张翔荣","张宇航","张雨萌","朱佳乐"]
                    missing_students = [student for student in check_students_common_list if student not in students_common_list]
                    extra_students = [student for student in students_common_list if student not in check_students_common_list]
                    random_delay(0.1, 1)
                    print("")
                    print("")
                    find_duplicates("[常规随机抽取名单]", students_common_list)
                    random_delay(0.1, 1)
                    find_duplicates("[常规随机抽取核对名单]", check_students_common_list)
                    random_delay(0.1, 1)
                    print("[常规随机抽取名单]          总人数：",len(students_common_list))
                    random_delay(0.1, 1)
                    print("")
                    print("[常规随机抽取核对名单]      总人数：",len(check_students_common_list))
                    random_delay(0.1, 1)
                    if not missing_students and not extra_students:
                        print("")
                        print("✓ [常规随机抽取名单]与[常规随机抽取核对名单]一致！")
                    if missing_students:
                        print("")
                        print("× 警告！[常规随机抽取名单]与[常规随机抽取核对名单]不一致！")
                        print("")
                        print("[常规随机抽取核对名单]中缺失学生：",missing_students)
                    if extra_students:
                        print("")
                        print("× 警告！[常规随机抽取名单]与[常规随机抽取核对名单]不一致！")
                        print("")
                        print("[常规随机抽取名单]中多余学生：",extra_students)
                    if len(students_common_list) == len(check_students_common_list) == 51:
                        random_delay(0.1, 1)
                        print("")
                        print("✓ [常规随机抽取名单]与[常规抽取核对名单]的人数均符合预期！")
                    else:
                        random_delay(0.1, 1)
                        print("")
                        print("× 警告！[常规随机抽取名单]与[常规抽取核对名单]的人数至少一个不符合预期！")
                        random_delay(0.1, 1)
                        print("")
                        print("请检查学生名单是否完整！")
                        random_delay(0.1, 1)
                    print("")
                    time.sleep(1)
                    print("检查完毕！已退出检查程序。")
                    time.sleep(1)
                    break
                elif key in ["3","Q","q"]:
                    print("已退出检查程序。")
                    break
                else:
                    print("无效选择！")
                    time.sleep(0.5)
        elif A in ["？", "?", "帮助","bangzhu", "bz", "BZ", "help", "Help"]:
            print("")
            print("帮助：")
            time.sleep(0.25)
            print("有效命令：")
            time.sleep(0.1)
            print("if A.isdigit():")
            time.sleep(0.1)
            print("elif A in [“C”, “c”, “clean”, “Clean”]")
            time.sleep(0.1)
            print("elif A in [“记录”, “jl”]:")
            time.sleep(0.1)
            print("elif A in [“JC”, “jc”, “检查”, “jiancha”]:")
            time.sleep(0.1)
            print("elif A in [“？”, “?”, “帮助”, “bangzhu”, “bz”, “BZ”, “help”, “Help”]:")
            time.sleep(0.1)
            print("else:")
            time.sleep(0.1)
        else:
            print("无效命令！")
# 如果出现错误
except Exception as e:
    # 捕获错误并记录到日志中
    logging.exception("发生了一个错误: %s", e)
