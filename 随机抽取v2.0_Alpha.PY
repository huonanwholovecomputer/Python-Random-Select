# 导入需要的模块
import random
import time
import sys
import msvcrt
import datetime
import logging
import os
import glob
from cryptography.fernet import Fernet

# 打印作者信息
print("随机抽取[版本号：2.0_Alpha] 内部版本号[2.0_Alpha.build-77.9.17]")
print("作者：GitHub_huonanwholovecomputer © 不保留任何权利。")
print("")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file_path = os.path.join(desktop_path, "错误日志.log")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
sys.stderr = open(log_file_path, "a")

# true变量赋值True
true = True

#尝试
try:
    # 创建程序储存目录
    program_data_storage_directory = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Python_Random_Select")
    os.makedirs(program_data_storage_directory, exist_ok=True)

    # 定义名单的识别模式
    list_pattern = os.path.join(program_data_storage_directory, "list_*.dll")
    matching_files = glob.glob(list_pattern)

    # 定义环境变量、文件路径
    desktop_input_file_name = "请在这里输入学生名单.txt"
    desktop_input_file_path = os.path.join(desktop_path, desktop_input_file_name)
    Fernet_key_name = "Fernet_key.dll"
    Fernet_key_path = os.path.join(program_data_storage_directory, Fernet_key_name)
    password_name = "password.dll"
    password_path = os.path.join(program_data_storage_directory, password_name)
    Fernet_key_name = "Fernet_key.dll"
    Fernet_key_path = os.path.join(program_data_storage_directory, Fernet_key_name)
    def define_recorded_students_file(recorded_students_file_num):
        recorded_students_file_name = f"recorded_students_{recorded_students_file_num}.dll"
        recorded_students_file_path = os.path.join(program_data_storage_directory, recorded_students_file_name)
        return recorded_students_file_path
    recorded_students_file_num = 1
    recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)# 调用函数define_recorded_students_file(recorded_students_file_num)
    txt_name = "默认名字.txt"
    txt_path = os.path.join(desktop_path, txt_name)

    # 定义函数create_list():
    def create_list():
        break_flag = False
        num = 1
        while true:
            list_name = f"list_{num}.dll"
            list_path = os.path.join(program_data_storage_directory, list_name)
            with open(desktop_input_file_path, "w", encoding="utf-8") as file:
                file.write("请在该txt文本文档中输入学生名单，并遵循以下格式：\n\n```txt内容：\n第一行是你的学生名单名称（必须填写，否则第一个学生会被识别为名单名称）\n第二行以及之后的行是学生名单\n```\n>示例填写：\n\n```txt内容：\n某某班的学生名单\n李白\n杜甫\n白居易\n苏轼\n```\n\n请注意，填写学生名单时，请务必清空这些内容。")
            print("————————————————————————————————————————")
            sentence = "请到桌面的[请在这里输入学生名单.txt]文件中输入你的学生名单。输入完毕后，保存更改，本程序稍后会读取该txt文本文档的学生列表，并对学生列表进行加密保存。"
            for char in sentence:
                print(char, end="")
                sys.stdout.flush()
                if char in [",","，","."]:
                    time.sleep(0.05)
                elif char in ["。"]:
                    time.sleep(0.1)
                else:
                    time.sleep(0.01)
            print("")
            print("————————————————————————————————————————")
            time.sleep(1)
            while true:
                print("请输入 Y 开始读取学生名单文件：")
                key = msvcrt.getch()
                if key in [b"y", b"Y"]:
                    print("")
                    print("尝试读取文件：",desktop_input_file_path)
                    with open(desktop_input_file_path, "r" ,encoding="utf-8") as file:
                        lines = file.readlines()
                    lines = [line.strip() for line in lines if line.strip()]
                    list_name = lines[0]
                    students = lines[1:]
                    print("\n✓  读取成功！")
                    print("\n学生名单名称：",list_name)
                    print("\n学生姓名：",students)
                    if list_name and students:
                        print("\n学生名单名称和学生姓名不为空，将尝试加密学生名单并写入程序储存目录。")
                        if not os.path.exists(Fernet_key_path):
                            print("\n未检测到加密密钥！将为您创建一个加密密钥，用于加密密码和学生列表。")
                            time.sleep(1)
                            print("\n加密技术：Fernet对称加密技术")
                            time.sleep(0.5)
                            print("\nFernet是一个对称加密技术，位于Python的cryptography模块中，它可以方便地进行文本的加密和解密，并为密码学初学者提供简单的接口。 Fernet使用高级加密标准（AES）算法来编码和解码消息。 AES是一种高度安全、被广泛使用和流行的密码学算法。 Fernet的密文是URL安全的，这意味着我们可以通过万维网发送密文，使数据传输更加方便。 Fernet使用随机数生成器生成一个高度安全的字母数字密钥。 它是一个32字节长的密钥，对于暴力破解攻击具有很高的抵抗力。 它还支持密钥轮换，即能够生成新的密钥并替换旧的密钥。 Fernet支持时间戳和数据的序列化，以便与密钥一起附加。")
                            time.sleep(1)
                            # 生成一个加密密钥（整个程序中唯一的一个加密密钥）
                            print("生成一个加密密钥...这将是是本程序中唯一一个Fernet密钥")
                            time.sleep(0.5)
                            Fernet_key = Fernet.generate_key()
                            print("\n尝试将Fernet密钥写入文件...")
                            time.sleep(0.25)
                            with open(Fernet_key_path, "wb") as Fernet_key_file:
                                Fernet_key_file.write(Fernet_key)
                            print(f"\n成功将Fernet密钥写入文件{Fernet_key_path}")
                            time.sleep(1)
                    else:
                        print("\n您貌似并没有在[",desktop_input_file_path,"]输入学生列表名字或者学生名单")
                        time.sleep(1)
                        print("\n无法储存到本程序的数据目录。")
                        time.sleep(0.5)
                        print("\n请重试...")
                    check_and_create_password()# 调用函数check_and_create_password():
                    print("\n加密数据部分：")
                    data = "\n".join(lines)
                    print("\n读取Fernet密钥")
                    with open(Fernet_key_path, "rb") as key_file:
                        Fernet_key = key_file.read()
                        print("\n读取成功！")
                    print("\n通过Fernet密钥创建加密格式...")
                    fernet = Fernet(Fernet_key)
                    print("\n加密学生列表...")
                    encrypted_data = fernet.encrypt(data.encode())
                    print(f"尝试保存加密后的数据到文件{list_path}")
                    with open(list_path, "wb") as file:
                        file.write(encrypted_data)
                    print(f"\n成功将学生名单：{list_name}加密并写入本程序的储存目录！")
                    print("\n————————————————————————————————————————\n需要再创建一个学生名单以实现更多场景的学生名单切换吗？如果需要请按下 Y (即“yes”)")
                    print("\n（按 Y 以外的任意按键跳过...(即“no”)）")
                    key = msvcrt.getch()
                    if key in [b"y", b"Y"]:
                        print("\n好的，正在再次为您导向学生名单创建程序...")
                        time.sleep(0.75)
                        num += 1
                        break
                    else:
                        print("\n好的，将删除桌面的[请在这里输入学生名单.txt]，正在退出学生名单创建程序...")
                        os.remove(desktop_input_file_path)
                        time.sleep(0.75)
                        break_flag = True
                        break
                else:
                    print("")
                    print("其他按键无效！输入 Y ，告诉我你已经准备好了学生名单")
                    time.sleep(1.5)
            if break_flag: 
                break
    def check_Fernet_key():
        if not os.path.exists(Fernet_key_path):
            if len(matching_files) > 0:
                for matching_file in matching_files:
                    os.remove(matching_file)
                print(f"× Fernet密钥丢失，已保存的学生名单已无法解密，程序已自动删除已保存的学生名单文件。")
        time.sleep(1)
    # 定义函数create_password():
    def check_and_create_password():
        if not os.path.exists(password_path):
            print("\n未检测到密码！")
            print("\n密码用于后续在您在本程序中，对学生名单的添加、修改、删除等操作。")
            while true:
                password = input("\n为您的学生名单设置一个密码: ")
                verify_password = input("\n请再次确认您的密码: ")
                if password != verify_password:
                    print("\n两次输入的密码不一致！")
                else:
                    print("\n两次输入的密码一致。已退出密码一致性检测循环")
                break
            print("\n使用Fernet密钥加密密码：") 
            print("\n读取Fernet密钥...")
            with open(Fernet_key_path, "rb") as key_file:
                Fernet_key = key_file.read()
            print("\n读取成功")
            print("\n通过Fernet密钥创建加密格式...")
            fernet = Fernet(Fernet_key)
            print("\n加密密码...")
            encrypted_password = fernet.encrypt(password.encode())
            print(f"\n保存加密后的密码到文件{password_path}")
            with open(password_path, "wb") as password_file:
                password_file.write(encrypted_password)
                print("\n加密后的密码已成功保存！")
            print("\n密码设置成功！")
            sentence = "\n日后，若您需要对学生名单进行更改，您需要输入这个密码。当然，您随时可以更改这个密码。"
            for char in sentence:
                print(char, end="")
                sys.stdout.flush()
                if char in ["，"]:
                    time.sleep(0.05)
                elif char in ["。"]:
                    time.sleep(0.1)
                else:
                    time.sleep(0.01)
            print("\n")
    # 定义函数write_recorded_students
    def write_recorded_students(selection_students, now):
        with open(Fernet_key_path, "rb") as key_file:
            Fernet_key = key_file.read()
        fernet = Fernet(Fernet_key)
        if os.path.exists(recorded_students_file_path):
            with open(recorded_students_file_path, "rb") as data_file:
                encrypted_data = data_file.read()
            decrypted_data = fernet.decrypt(encrypted_data).decode()
        else:
            decrypted_data = ""
        selection_students_and_now = " ".join(selection_students) + " - " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
        decrypted_data += selection_students_and_now
        encrypted_data = fernet.encrypt(decrypted_data.encode())
        with open(recorded_students_file_path, "wb") as data_file:
            data_file.write(encrypted_data)
    # 定义函数read_recorded_students
    def read_recorded_students():
        if os.path.exists(recorded_students_file_path):
            with open(Fernet_key_path, "rb") as key_file:
                Fernet_key = key_file.read()
            fernet = Fernet(Fernet_key)
            with open(recorded_students_file_path, "rb") as data_file:
                encrypted_data = data_file.read()
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            recorded_students = []
            for line in decrypted_data.strip().split("\n"):
                students_part = line.split(" - ")[0]
                recorded_students.extend(students_part.split(" "))
            return recorded_students
        return []
    # for获取[matching_files]的相关数据（在必要时更新）（可获得两个更新的数据，并可以直接使用{all_students_list_names, all_students_lists}）
    def for_matching_files_data():
        all_students_list_names = []
        all_students_lists = []
        for matching_file in matching_files:
            with open(Fernet_key_path, "rb") as key_file:
                Fernet_key = key_file.read()
            fernet = Fernet(Fernet_key)
            with open(matching_file, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            data = decrypted_data.decode()
            students_list = data.split("\n")
            students_list = [line.strip() for line in students_list if line.strip()]
            list_name = students_list[0]
            students = students_list[1:]
            all_students_list_names.append(list_name)
            all_students_lists.append(students)
        return all_students_list_names, all_students_lists
    # 选择需要操作的学生名单
    def select_list():
        while True:
            print("\n选择需要操作的学生名单")
            print("——————————————————————————————\n请选择学生名单：")
            list_num = 1
            for all_list_name in all_students_list_names:
                print(f"\n【{list_num}】{all_list_name}")
                list_num += 1
            print("——————————————————————————————")
            key = msvcrt.getch()
            key_str = conversion_utf_8_coding(key)# 调用函数conversion_utf_8_coding(key)
            if key_str.isdigit():
                key_str = int(key_str)
                if 1 <= key_str <= len(all_students_list_names):
                    select_matching_file_path = matching_files[key_str - 1]
                    print(f"\n选择了【{key_str}】{all_list_name}")
                    return select_matching_file_path
                else:
                    print("\n输入无效")
            else:
                print("\n输入无效")
        time.sleep(0.5)
    # 解密数据
    def decrypt_data(data_path):
        with open(Fernet_key_path, "rb") as key_file:
            Fernet_key = key_file.read()
        fernet = Fernet(Fernet_key)
        with open(data_path, "rb") as data_file:
            encrypted_data = data_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_data = decrypted_data.decode()
        decrypted_data = decrypted_data.split("\n")
        return decrypted_data
    # 转换 utf-8 编码
    def conversion_utf_8_coding(key):
        if isinstance(key, bytes):
            key_str = key.decode("utf-8")
        elif not isinstance(key, str):
            # 如果 key 不是字符串类型，则将其转换为 utf-8 编码
            key_str = str(key).decode("utf-8")
        else:
            # 如果 key 是字符串类型，则无需转换
            key_str = key
        return key_str
    # 主逻辑
    check_Fernet_key()# 调用函数check_Fernet_key()
    check_and_create_password()# 调用函数check_and_create_password()
    if len(matching_files) == 0:
        time.sleep(1)
        print("————————————————————————————————————————\n程序没有识别到指定位置的加密学生名单，将为您导向学生名单创建程序...")
        time.sleep(1)
        print("\n本程序的数据储存目录：", program_data_storage_directory)
        create_list()  # 调用函数create_list()
        print("\n再次寻找储存目录中的学生名单...\n")
        time.sleep(0.5)
        matching_files = glob.glob(list_pattern)

    all_students_list_names, all_students_lists = for_matching_files_data()  # 调用函数for_matching_files_data()
    print(f"找到的学生名单个数：{len(matching_files)}个")
    if len(matching_files) == 1:
        time.sleep(0.25)
        print(f"\n由于您的学生名单只有1个，程序已默认选择该学生名单。")
        time.sleep(0.25)
        print(f"\n学生名单名称：{all_students_list_names[0]}")
        time.sleep(0.25)
        print(f"\n学生：{all_students_lists[0]}")
        students_list = all_students_lists[0]
        recorded_students_file_num = 1
        recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)  # 调用函数define_recorded_students_file(recorded_students_file_num)
    else:
        time.sleep(0.25)
        print("——————————————————————————————\n请选择学生名单：")
        list_num = 1
        for all_list_name in all_students_list_names:
            print(f"\n【{list_num}】{all_list_name}")
            list_num += 1
        print("——————————————————————————————")
        while true:
            print("通过数字按键选择学生名单")
            key = msvcrt.getch()
            key_str = conversion_utf_8_coding(key)# 调用函数conversion_utf_8_coding(key)
            if key_str.isdigit():
                key_str = int(key_str)
                if 1 <= key_str <= len(all_students_list_names):
                    print(f"\n选择了学生名单【{key_str}】{all_students_list_names[key_str - 1]}")
                    print(f"\n学生：{all_students_lists[key_str - 1]}")
                    students_list = all_students_lists[key_str - 1]
                    recorded_students_file_num = key_str
                    recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)  # 调用函数define_recorded_students_file(recorded_students_file_num)
                    time.sleep(0.5)
                    break
                else:
                    print("\n输入的数字超出范围，请输入一个有效的数字键。\n")
            else:
                print("\n输入无效，请输入一个数字键。\n")
            time.sleep(1)
    while true:
        students = students_list
        if os.path.exists(recorded_students_file_path):
            recorded_students = read_recorded_students()# 调用函数read_recorded_students()
            students = [student for student in students if student not in recorded_students]
            if len(students) == 0:
                print("\n名单中的学生已空，已初始化学生名单并清空抽取记录。")
                students = students_list
                recorded_students = []
                os.remove(recorded_students_file_path)
        A = input("————————————————————————————————————————\n请输入需要抽取的学生个数：")
        # 抽取
        time.sleep(0.5)
        if A.isdigit():
            A = int(A)
            if A > len(students):
                print("\n提示：需要抽取的学生个数超过学生总数！")
                time.sleep(0.1)
                print("\n请重新抽取..")
                time.sleep(0.2)
            else:
                random.shuffle(students)
                selection_students = random.sample(students, A)
                now = datetime.datetime.now()
                write_recorded_students(selection_students, now)  # 调用函数write_recorded_students(selection_students, now)
                print(f"\n抽取结果：【{selection_students}】")
        elif A in ["C", "c", "clean", "Clean"]:
            students = students_list
            if os.path.exists(recorded_students_file_path):
                os.remove(recorded_students_file_path)
                print(f"\n已清空记录！")
            else:
                print("记录为空。")
        elif A in ["记录", "jl"]:
            recorded_students = read_recorded_students()# 调用函数read_recorded_students()
            if recorded_students:
                print("\n已经记录的学生：",recorded_students)
                time.sleep(0.1)
                print("\n共记录",(len(recorded_students)),"名学生")
                time.sleep(0.1)
                print("\n还有",len(students_list),"-",len(recorded_students),"=",len(students_list)-len(recorded_students),"名学生未被抽取")
                time.sleep(0.25)
                print("\n本次抽取默认会跳过这些已经记录的学生，输入“C”或“c”可清除[file_name]中的学生抽取记录")
            if not recorded_students:
                time.sleep(0.25)
                print("\n没有学生的抽取记录，本次抽取将不会去除任何学生")
        elif A in ["修改密码"]:
            print("\n这是修改密码部分...")
            with open(Fernet_key_path, "rb") as key_file:
                Fernet_key = key_file.read()
            fernet = Fernet(Fernet_key)
            with open(password_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
            password_data = fernet.decrypt(encrypted_data)
            password = password_data.decode()
            check_password = input("\n请输入您之前创建的密码：")
            if check_password == password:
                print("\n√ 密码正确！")
            while true:
                time.sleep(0.5)
                new_password = input("\n请输入一个新密码：")
                verify_new_password = input("\n请再次确定您的新密码：")
                if new_password != verify_password:
                    print("\n× 两次输入的密码不一致！")
                else:
                    encrypted_new_password = fernet.encrypt(new_password.encode())
                    with open(password_path, "wb") as password_file:
                        password_file.write(encrypted_new_password)
                    print("\n√ 密码修改成功！")
                break
            else:
                print("\n× 密码错误")
        # 修改学生名单
        elif A in ["修改学生名单","xg"]:
            while true:
                # 显示修改学生名单菜单
                print("\n菜单\n——————————————————————————————")
                print("【1】修改学生名单内容\n\n【2】删除学生名单\n\n【3】添加学生名单\n\n【4】退出")
                print("——————————————————————————————")
                key = msvcrt.getch()
                key_str = conversion_utf_8_coding(key)# 调用函数conversion_utf_8_coding(key)
                if key_str.isdigit():
                    key_str = int(key_str)
                    if key_str == 1:
                        print("\n选择了【1】修改学生名单内容")
                        select_matching_file_path = select_list()# 调用函数select_list()
                        decrypted_data = decrypt_data(select_matching_file_path)# 调用函数decrypt_data()解密数据
                        txt_name = decrypted_data[0] + ".txt"
                        txt_path = os.path.join(desktop_path, txt_name)
                        with open(txt_path, 'w', encoding='utf-8') as file:
                            for data in decrypted_data:
                                file.write(data + "\n")
                        print(f"\n已将学生名单解密并写到桌面文本文档{txt_path}，您可以在这个文本文档中修改名单内容，稍后，本程序将读取这个文本文档，并将更新应用于{txt_path}")
                        print("\n请输入 Y 开始读取学生名单文件：")
                        key = msvcrt.getch()
                        while true:
                            if key in [b"y", b"Y"]:
                                print("")
                                print(f"尝试读取文件：{txt_path}")
                                with open(txt_path, "r" ,encoding="utf-8") as file:
                                    lines = file.readlines()
                                lines = [line.strip() for line in lines if line.strip()]
                                list_name = lines[0]
                                students = lines[1:]
                                print("\n√ 读取成功！")
                                print("\n学生名单名称：",list_name)
                                print("\n学生姓名：",students)
                                if list_name and students:
                                    print("\n学生名单名称和学生姓名不为空，将尝试加密学生名单并写入程序储存目录。")
                                    print("\n加密数据部分：")
                                    data = "\n".join(lines)
                                    print("\n读取Fernet密钥")
                                    with open(Fernet_key_path, "rb") as key_file:
                                        Fernet_key = key_file.read()
                                        print("\n读取成功！")
                                    print("\n通过Fernet密钥创建加密格式...")
                                    fernet = Fernet(Fernet_key)
                                    print("\n加密学生列表...")
                                    encrypted_data = fernet.encrypt(data.encode())
                                    print(f"尝试保存加密后的数据到文件{select_matching_file_path}")
                                    with open(select_matching_file_path, "wb") as file:
                                        file.write(encrypted_data)
                                    print(f"\n成功将学生名单：{list_name}加密并写入本程序的储存目录！")
                                    print("\n————————————————————————————————————————\n需要再创建一个学生名单以实现更多场景的学生名单切换吗？如果需要请按下 Y (即“yes”)")
                                    print("\n（按 Y 以外的任意按键跳过...(即“no”)）")
                                    key = msvcrt.getch()
                                    if key in [b"y", b"Y"]:
                                        print("\n好的，正在再次为您导向学生名单创建程序...")
                                        time.sleep(0.75)
                                        num += 1
                                        break
                                    else:
                                        print(f"\n好的，将删除桌面的[{txt_path}]，正在退出学生名单创建程序...")
                                        os.remove(txt_path)
                                        time.sleep(0.75)
                                        break_flag = True
                                        break
                                        time.sleep(1)
                                else:
                                    print(f"\n您貌似并没有在[{txt_path}]输入学生列表名字或者学生名单")
                                    time.sleep(1)
                                    print("\n所以我们无法应用更改到对应的学生名单。")
                                    time.sleep(0.5)
                                    print("\n请重试...")
                            else:
                                print("\n其他按键无效！输入 Y ，告诉我你已经准备好了学生名单")
                                time.sleep(1.5)
                    elif key_str == 2:
                        print("\n选择了【2】删除学生名单")
                        matching_file_path = select_list()# 调用函数select_list()
                        print(matching_file_path)
                        os.remove(matching_file_path)
                    elif key_str == 3:
                        print("\n选择了【3】添加学生名单")
                        create_list()# 调用函数create_list()
                    elif key_str == 4:
                        print("\n退出...")
                        time.sleep(0.5)
                        break
                    else:
                        print("\n选择无效")
                        time.sleep(0.5)
                else:
                    print("\n输入无效")
                    time.sleep(0.5)
except Exception as e:
    logging.exception(f"发生了一个错误: %s{e}\n\n")
