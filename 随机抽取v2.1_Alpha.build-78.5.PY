# 导入需要的模块
import random
import time
import sys
import msvcrt
import logging
import os
import glob
from cryptography.fernet import Fernet

# 打印作者信息
print("随机抽取[版本号：2.1_Alpha] 内部版本号[2.0_Alpha.build-78.5]")
print("作者：© GitHub_huonanwholovecomputer 不保留任何权利。")
print("")

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_file_path = os.path.join(desktop_path, "随机抽取_错误日志.log")
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
sys.stderr = open(log_file_path, "a")

# true变量赋值True
true = True

# 全局变量
global all_students_list_names, all_students_lists
global matching_files

# 程序的最最最外层循环，用于将程序保持黑框框运行
while true:
    #尝试
    try:
        # def 选择名单，select_list()
        def select_list():
            while true:
                print("——————————————————————————————\n请选择需要操作的学生名单：")
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
                        recorded_students_file_num = key_str
                        recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)# 定义记录文件的位置，调用函数define_recorded_students_file(recorded_students_file_num)
                        print(f"选择了【{key_str}】{all_list_name}")
                        time.sleep(0.5)
                        return select_matching_file_path,recorded_students_file_path
                    else:
                        print("选择无效")
                        time.sleep(0.5)
                else:
                    print("输入无效")
                    time.sleep(0.5)

        # def 检测名单文件名是否按照顺序排列，并在必要时进行矫正，check_list_num()
        def check_list_num():
            # 提取数字部分并排序
            file_numbers = sorted([int(os.path.splitext(os.path.basename(f))[0].split('_')[1]) for f in matching_files])
            # 检查并矫正文件名
            expected_num = 1
            for file_number in file_numbers:
                expected_filename = os.path.join(program_data_storage_directory, f"list_{expected_num}.dll")
                current_filename = os.path.join(program_data_storage_directory, f"list_{file_number}.dll")
                # 如果当前文件名不符合预期，则重命名
                if current_filename != expected_filename:
                    os.rename(current_filename, expected_filename)
                    print("\n检测到名单文件数字顺序错误。")
                    time.sleep(0.1)
                    print(f"\n已将\n\n{current_filename}\n\n重命名为：\n\n{expected_filename}\n")
                    time.sleep(0.25)
                expected_num += 1

        def check_Fernet_key():
            if not os.path.exists(Fernet_key_path):
                print("\n咦？奇怪，[Fernet_key]文件怎么突然在本次程序运行的时候不见了?")
                time.sleep(1)
                with open(Fernet_key_path, "wb") as Fernet_key_file:
                    Fernet_key_file.write(Fernet_key)
                print("\n还好还好，本程序成功地重新创建了[Fernet_key]文件，并成功写入了本次程序在运行时读取到程序缓存的[Fernet_key]数据")
                time.sleep(1)
            else:
                with open(Fernet_key_path, "rb") as Fernet_key_file:
                    check_Fernet_key = Fernet_key_file.read()
                    if check_Fernet_key != Fernet_key:
                        print("\n什么？！[Fernet_key]居然在本次程序运行的时候被篡改了，这怎么行。")
                        with open(Fernet_key_path, "wb") as Fernet_key_file:
                            Fernet_key_file.write(Fernet_key)
                        time.sleep(0.75)
                        print("\n已修复[Fernet_key]文件。")
                        time.sleep(1)
        # def 解密数据
        def decrypt_data(data_path):
            with open(data_path, "rb") as data_file:
                encrypted_data = data_file.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            decrypted_data = decrypted_data.decode()
            decrypted_data = decrypted_data.split("\n")
            return decrypted_data

        # def 转换 utf-8 编码
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

        # def 创建学生名单create_list(num)
        def create_list(num):
            break_flag = False
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
                        time.sleep(0.1)
                    elif char in ["。"]:
                        time.sleep(0.2)
                    else:
                        time.sleep(0.02)
                print("")
                print("————————————————————————————————————————")
                time.sleep(1)
                while true:
                    print("请输入 Y 开始读取学生名单文件：")
                    key = msvcrt.getch()
                    if key in [b"y", b"Y"]:
                        print("")
                        print(f"尝试读取文件：[{desktop_input_file_path}]")
                        with open(desktop_input_file_path, "r" ,encoding="utf-8") as file:
                            lines = file.readlines()
                        lines = [line.strip() for line in lines if line.strip()]
                        list_name = lines[0]
                        students = lines[1:]
                        print("\n✓  读取成功！")
                        print(f"\n学生名单名称：[{list_name}]")
                        print(f"\n学生姓名：{students}")
                        if list_name and students:
                            print("\n学生名单名称和学生姓名不为空，将尝试加密学生名单并写入程序储存目录。")
                            time.sleep(0.5)
                        else:
                            print(f"\n您貌似并没有在[{desktop_input_file_path}]输入学生列表名字或者学生名单")
                            time.sleep(1)
                            print("\n无法储存到本程序的数据目录。")
                            time.sleep(0.5)
                            print("\n请重试...")
                        check_and_create_password()# 调用函数check_and_create_password():
                        print("\n加密数据部分：")
                        time.sleep(0.25)
                        data = "\n".join(lines)
                        time.sleep(0.5)
                        print("\n加密学生列表...")
                        encrypted_data = fernet.encrypt(data.encode())
                        time.sleep(0.5)
                        print(f"\n尝试保存加密后的数据到文件[{list_path}]")
                        with open(list_path, "wb") as file:
                            file.write(encrypted_data)
                        time.sleep(0.5)
                        print(f"\n成功将学生名单：[{list_name}]加密并写入本程序的储存目录！")
                        time.sleep(1)
                        print("\n————————————————————————————————————————\n需要再创建一个学生名单以实现更多场景的学生名单切换吗？如果需要请按下 Y (即“yes”)")
                        time.sleep(1)
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
                        print("\n其他按键无效！输入 Y ，告诉我你已经准备好了学生名单\n")
                        time.sleep(1.5)
                if break_flag: 
                    break

        # def 定义函数check_and_create_password():
        def check_and_create_password():
            if not os.path.exists(password_path):
                print("\n未检测到密码！")
                time.sleep(0.5)
                print("\n密码用于后续在您在本程序中，对学生名单的添加、修改、删除等操作。")
                time.sleep(0.5)
                while true:
                    password = input("\n为您的学生名单设置一个密码: ")
                    time.sleep(0.1)
                    verify_password = input("\n请再次确认您的密码: ")
                    time.sleep(0.25)
                    if password != verify_password:
                        print("\n两次输入的密码不一致！")
                    else:
                        print("\n两次输入的密码一致。")
                        time.sleep(0.25)
                        print("\n使用Fernet密钥加密密码...")
                        time.sleep(0.25)
                        encrypted_password = fernet.encrypt(password.encode())
                        print(f"\n保存加密后的密码到文件{password_path}")
                        time.sleep(0.25)
                        with open(password_path, "wb") as password_file:
                            password_file.write(encrypted_password)
                        print("\n加密后的密码已成功保存！")
                        time.sleep(0.25)
                        print("\n密码设置成功！")
                        time.sleep(0.25)
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
                        break

        # def 定义函数write_recorded_students
        def write_recorded_students(selection_students):
            if os.path.exists(recorded_students_file_path):
                with open(recorded_students_file_path, "rb") as data_file:
                    encrypted_data = data_file.read()
                decrypted_data = fernet.decrypt(encrypted_data).decode()
            else:
                decrypted_data = ""
            selection_students = selection_students.strip()
            decrypted_data += selection_students + " "
            encrypted_data = fernet.encrypt(decrypted_data.encode())
            with open(recorded_students_file_path, "wb") as data_file:
                data_file.write(encrypted_data)

        # def 定义函数read_recorded_students
        def read_recorded_students():
            if os.path.exists(recorded_students_file_path):
                with open(recorded_students_file_path, "rb") as data_file:
                    encrypted_data = data_file.read()
                decrypted_data = fernet.decrypt(encrypted_data).decode()
                recorded_students = decrypted_data.strip().split(" ")  # 以空格分割学生名字
                return recorded_students
            return []

        # def for获取[matching_files]的相关数据（在必要时更新）（可获得两个更新的数据，并可以直接使用{all_students_list_names, all_students_lists}）
        def for_matching_files_data(matching_files):
            all_students_list_names = []
            all_students_lists = []
            for matching_file in matching_files:
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

        # 主逻辑
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

        # 检查Fernet_key是否存在，这是程序第一次检查Fernet_key
        if not os.path.exists(Fernet_key_path):
            if len(matching_files) != 0:
                print(f"\n× 糟了，Fernet密钥不见了，已保存的学生名单已无法解密。这是您本人的操作？如果是，请尽快恢复文件[{Fernet_key_path}]")
                time.sleep(1)
                print("\n需要本程序删除已保存的学生名单文件吗？（输入Y，删除所有已保存的学生名单文件）")
                key = msvcrt.getch()
                if key in [b"Y",b"y"]:
                    for matching_file in matching_files:
                        os.remove(matching_file)
                else:
                    print("\n好吧，希望您有办法解决[Fernet_key]丢失的问题。当然，在您找回[Fernet_key]文件之前，您将无法使用程序的后续功能。")
                    time.sleep(1)
                    sentence = "\n程序将在1秒后退出..."
                    for char in sentence:
                        print(char, end="")
                        sys.stdout.flush()
                        if char == ".":
                            time.sleep(0.2)
                        else:
                            time.sleep(0.05)
                    time.sleep(0.75)
                    os._exit(0)
            else:                
                print("\n未检测到加密密钥！将为您创建一个加密密钥，用于加密密码和学生列表。")
                time.sleep(1)
                print("\n加密技术：Fernet对称加密技术")
                time.sleep(0.5)
                sentence = "\nFernet是一个对称加密技术，位于Python的cryptography模块中，它可以方便地进行文本的加密和解密，并为密码学初学者提供简单的接口。 Fernet使用高级加密标准（AES）算法来编码和解码消息。 AES是一种高度安全、被广泛使用和流行的密码学算法。 Fernet的密文是URL安全的，这意味着我们可以通过万维网发送密文，使数据传输更加方便。 Fernet使用随机数生成器生成一个高度安全的字母数字密钥。 它是一个32字节长的密钥，对于暴力破解攻击具有很高的抵抗力。 它还支持密钥轮换，即能够生成新的密钥并替换旧的密钥。 Fernet支持时间戳和数据的序列化，以便与密钥一起附加。"
                for char in sentence:
                    print(char, end="")
                    sys.stdout.flush()
                    if char in ["，","、"]:
                        time.sleep(0.05)
                    elif char in ["。"]:
                        time.sleep(0.08)
                    else:
                        time.sleep(0.01)
                time.sleep(1)
                # 生成一个加密密钥（整个程序中唯一的一个加密密钥）
                print("\n\n生成一个加密密钥...这将是是本程序中唯一一个Fernet密钥")
                time.sleep(0.5)
                Fernet_key = Fernet.generate_key()
                fernet = Fernet(Fernet_key)
                print("\n尝试将Fernet密钥写入文件...")
                time.sleep(0.25)
                with open(Fernet_key_path, "wb") as Fernet_key_file:
                    Fernet_key_file.write(Fernet_key)
                print(f"\n成功将Fernet密钥写入文件[{Fernet_key_path}]")
                time.sleep(1)

        else:
            # 获取Fernet_key和fernet两个变量（本次程序运行只读取一次Fernet_key以及创建一次fernet）
            with open(Fernet_key_path, "rb") as key_file:
                Fernet_key = key_file.read()
            fernet = Fernet(Fernet_key)

        # 检查名单是否为空，若为空，则调用函数create_list(num)
        if len(matching_files) == 0:
            time.sleep(1)
            print("————————————————————————————————————————\n程序没有识别到指定位置的加密学生名单，将为您导向学生名单创建程序...")
            time.sleep(0.5)
            print("\n本程序的数据储存目录：", program_data_storage_directory)
            time.sleep(1)
            num = 1
            create_list(num)# 调用函数create_list(num)
            matching_files = glob.glob(list_pattern)

        # 检查密码是否存在，不存在则创建
        check_and_create_password()

        # 获取password变量（本次程序运行只读取一次password）
        with open(password_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        password = decrypted_data.decode()
        # 调用函数for_matching_files_data(matching_files)
        all_students_list_names, all_students_lists = for_matching_files_data(matching_files)
        
        print(f"找到的学生名单个数：{len(matching_files)}个")
        if len(matching_files) == 1:
            time.sleep(0.25)
            print(f"\n由于您的学生名单只有1个，程序已默认选择该学生名单。")
            time.sleep(0.25)
            print(f"\n学生名单名称：[{all_students_list_names[0]}]")
            time.sleep(0.25)
            print(f"\n学生：{all_students_lists[0]}")
            students_list = all_students_lists[0]
            recorded_students_file_num = 1
            recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)  # 调用函数define_recorded_students_file(recorded_students_file_num)
        else:
            time.sleep(0.25)
            print("——————————————————————————————\n请选择需要使用的学生名单（通过数字按键选择学生名单）")
            list_num = 1
            for all_list_name in all_students_list_names:
                print(f"\n【{list_num}】{all_list_name}")
                list_num += 1
            print("——————————————————————————————")
            while true:
                key = msvcrt.getch()
                key_str = conversion_utf_8_coding(key)# 调用函数conversion_utf_8_coding(key)
                if key_str.isdigit():
                    key_str = int(key_str)
                    if 1 <= key_str <= len(all_students_list_names):
                        print(f"选择了学生名单【{key_str}】{all_students_list_names[key_str - 1]}")
                        students_list = all_students_lists[key_str - 1]
                        recorded_students_file_num = key_str
                        recorded_students_file_path = define_recorded_students_file(recorded_students_file_num)  # 调用函数define_recorded_students_file(recorded_students_file_num)
                        time.sleep(0.5)
                        break
                    else:
                        print("输入的数字超出范围，请输入一个有效的数字键。")
                else:
                    print("输入无效，请输入一个数字键。")
                time.sleep(1)
        while true:
            check_Fernet_key()# 检查Fernet_key，调用函数check_Fernet_key()
            students = students_list
            if os.path.exists(recorded_students_file_path):
                recorded_students = read_recorded_students()# 调用函数read_recorded_students()
                students = [student for student in students if student not in recorded_students]
                if len(students) == 0:
                    print("\n名单中的学生已空，已初始化学生名单并清空抽取记录。")
                    students = students_list
                    recorded_students = []
                    os.remove(recorded_students_file_path)
            A = input("————————————————————————————————————————\n请输入需要抽取的学生个数或命令：")
            # 抽取
            if A.isdigit():
                A = int(A)
                if A > len(students):
                    print("\n提示：需要抽取的学生个数超过学生总数！")
                    time.sleep(0.1)
                    print("\n请重新抽取..")
                    time.sleep(0.2)
                else:
                    selection_students = []
                    cycle_count = 0
                    random.shuffle(students)
                    while cycle_count < A:
                        cycle_count += 1
                        if cycle_count % 3 == 0:
                            random.shuffle(students)
                        selection_student = random.choice(students)
                        selection_students.append(selection_student)
                        write_recorded_students(selection_student)# 写入记录的学生,调用函数write_recorded_students(selection_students)
                        recorded_students = read_recorded_students()# 调用函数read_recorded_students()
                        students = [student for student in students if student not in recorded_students]
                    time.sleep(0.1)
                    print(f"\n最终的抽取结果：【{selection_students}】")
                    print(f"\n记录的学生：【{recorded_students}】")
                    time.sleep(0.5)
                    
            elif A in ["清空记录", "清空", "qingkong", "QINGKONG", "qk", "QK", "C", "c", "clean", "Clean"]:
                students = students_list
                if os.path.exists(recorded_students_file_path):
                    os.remove(recorded_students_file_path)
                    print(f"\n已清空记录！")
                else:
                    print("\n记录为空，不需要删除。")
                time.sleep(0.5)
            elif A in ["添加记录", "添加", "tianjia", "TIANJIA", "tj", "TJ", "tjjl", "TJJL"]:
                recorded_students = read_recorded_students()  # 调用函数read_recorded_students()
                with open(password_path, "rb") as encrypted_file:
                    encrypted_data = encrypted_file.read()
                password_data = fernet.decrypt(encrypted_data)
                password = password_data.decode()
                check_password = input("\n请输入密码以核实您的身份：")
                if check_password == password:
                    print("√ 密码正确！")
                    time.sleep(0.75)
                    add_recorded_students = input("\n添加一个或多个学生到记录中，以排除抽取...\nTip:若需要输入多个学生，则需要使用“、”分割开\n\n请输入需要添加的学生名字：")
                    add_recorded_students_list = [student.strip() for student in add_recorded_students.split("、")]
                    all_students_valid = True
                    add_students = []
                    for student in add_recorded_students_list:
                        if student in add_students:
                            print(f"\n嗯？您貌似重复输入了[{student}]这个学生？请不要输入重复的学生。")
                            all_students_valid = False
                            break
                        add_students.append(student)
                        if student not in students_list:
                            print(f"\n嗯？您输入的[{student}]貌似不在您的学生名单中啊。")
                            all_students_valid = False
                            break
                        if student in recorded_students:
                            print(f"\n嗯？[{student}]这个学生貌似已经被记录了。")
                            all_students_valid = False
                            break
                    if all_students_valid:
                        # 将学生列表转换为一个字符串，每个学生用空格分隔
                        students_str = " ".join(add_recorded_students_list)
                        write_recorded_students(students_str)# 写入记录的学生, 调用函数write_recorded_students(selection_students)
                        recorded_students = read_recorded_students()# 调用函数read_recorded_students()
                        print("\n记录添加成功！")
                        time.sleep(1)
                else:
                    print("× 密码错误。")
            elif A in ["记录", "jilu", "JILU", "jl", "JL", "recorded"]:
                recorded_students = read_recorded_students()# 调用函数read_recorded_students()
                if recorded_students:
                    print("\n已经记录的学生：",recorded_students)
                    time.sleep(0.1)
                    print("\n共记录",(len(recorded_students)),"名学生")
                    time.sleep(0.1)
                    print("\n还有",len(students_list),"-",len(recorded_students),"=",len(students_list)-len(recorded_students),"名学生未被抽取")
                    time.sleep(0.25)
                    print("\n本次抽取默认会跳过这些已经记录的学生，输入“C”或“c”可清空学生抽取记录")
                if not recorded_students:
                    time.sleep(0.25)
                    print("\n没有学生的抽取记录，本次抽取将不会去除任何学生")
            elif A in ["修改密码","xgmm", "password"]:
                print("\n这是修改密码部分...")
                time.sleep(0.5)
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
                        if new_password != verify_new_password:
                            print("\n× 两次输入的密码不一致！")
                        else:
                            encrypted_new_password = fernet.encrypt(new_password.encode())
                            with open(password_path, "wb") as password_file:
                                password_file.write(encrypted_new_password)
                            print("\n√ 密码修改成功！")
                        break
                else:
                    print("× 密码错误")
            # 修改学生名单
            elif A in ["修改学生名单", "xgxsmd", "XGXSMD", "xg", "XG", "list"]:
                with open(password_path, "rb") as encrypted_file:
                    encrypted_data = encrypted_file.read()
                password_data = fernet.decrypt(encrypted_data)
                password = password_data.decode()
                error_count = 0
                while true:
                    break_flag = False
                    check_password = input("\n请输入密码以核实您的身份：")
                    if check_password == password:
                        print("√ 密码正确！")
                        while true:
                            check_list_num()# 调用函数check_list_num()
                            # 显示修改学生名单菜单
                            print("\n菜单\n——————————————————————————————")
                            print("【1】修改或导出学生名单内容\n\n【2】删除学生名单\n\n【3】添加新的学生名单\n\n【4】退出")
                            print("——————————————————————————————")
                            key = msvcrt.getch()
                            key_str = conversion_utf_8_coding(key)# 调用函数conversion_utf_8_coding(key)
                            if key_str.isdigit():
                                key_str = int(key_str)
                                if key_str == 1:
                                    if len(matching_files) != 0:
                                        print("选择了【1】修改学生名单内容")
                                        time.sleep(0.5)
                                        select_matching_file_path = select_list()[0]# 调用函数select_list()
                                        decrypted_data = decrypt_data(select_matching_file_path)# 调用函数decrypt_data()解密数据
                                        txt_name = decrypted_data[0] + ".txt"
                                        txt_path = os.path.join(desktop_path, txt_name)
                                        with open(txt_path, 'w', encoding='utf-8') as file:
                                            for data in decrypted_data:
                                                file.write(data + "\n")
                                        print(f"\n已将学生名单解密并写到桌面文本文档[{txt_path}]，您可以在这个文本文档中修改名单内容，稍后，本程序将读取这个文本文档，并将更新应用于[{select_matching_file_path}]")
                                        while true:
                                            print("\n请输入 Y 开始读取学生名单文件，其他任意键取消读取：")
                                            key = msvcrt.getch()
                                            if key in [b"y", b"Y"]:
                                                print("")
                                                print(f"尝试读取文件：[{txt_path}]")
                                                with open(txt_path, "r" ,encoding="utf-8") as file:
                                                    lines = file.readlines()
                                                lines = [line.strip() for line in lines if line.strip()]
                                                data = "\n".join(lines)
                                                list_name = lines[0]
                                                students = lines[1:]
                                                print("\n√ 读取成功！")
                                                print("\n学生名单名称：",list_name)
                                                print("\n学生姓名：",students)
                                                if list_name and students:
                                                    print("\n学生名单名称和学生姓名不为空，将尝试加密学生名单并写入程序储存目录。")
                                                    time.sleep(1)
                                                    print("\n加密数据部分：")
                                                    time.sleep(0.5)
                                                    print("\n加密学生列表...")
                                                    time.sleep(0.25)
                                                    encrypted_data = fernet.encrypt(data.encode())
                                                    print(f"\n尝试保存加密后的数据到文件[{select_matching_file_path}]")
                                                    with open(select_matching_file_path, "wb") as file:
                                                        file.write(encrypted_data)
                                                    time.sleep(0.25)
                                                    print(f"\n成功将学生名单：[{list_name}]加密并写入本程序的储存目录！")
                                                    time.sleep(0.75)
                                                    print(f"\n将删除桌面的[{txt_path}]，然后退出学生名单修改程序...")
                                                    os.remove(txt_path)
                                                    time.sleep(1)
                                                    break
                                                else:
                                                    print(f"\n您貌似并没有在[{txt_path}]输入学生列表名字或者学生名单")
                                                    time.sleep(1)
                                                    print("\n所以我们无法应用更改到对应的学生名单。")
                                                    time.sleep(0.5)
                                                    print("\n请重试...")
                                                    time.sleep(0.5)
                                            else:
                                                print(f"\n好的，已取消应用更改，您可以从桌面查看或备份您的学生名单[{decrypted_data[0]}]。")
                                                time.sleep(1)
                                                break
                                    else:
                                        print("\n哎呀，没有名单可以修改或导出呢。")
                                        time.sleep(1)
                                elif key_str == 2:
                                    print("选择了【2】删除学生名单")
                                    if len(matching_files) != 0:
                                        select_matching_file_path, recorded_students_file_path = select_list()# 调用函数select_list()
                                        os.remove(select_matching_file_path)
                                        time.sleep(0.25)
                                        print(f"\n成功删除了文件[{select_matching_file_path}]")
                                        if os.path.exists(recorded_students_file_path):
                                            os.remove(recorded_students_file_path)
                                            print(f"\n成功删除了记录文件[{recorded_students_file_path}]")
                                        check_list_num()# 调用函数check_list_num()
                                        matching_files = glob.glob(list_pattern)
                                        all_students_list_names, all_students_lists = for_matching_files_data(matching_files)# 刷新matching_files数据
                                    else:
                                        print("\n哎呀，没有名单可以删除呢。")
                                    time.sleep(1)
                                elif key_str == 3:
                                    print("选择了【3】添加学生名单")
                                    num = len(matching_files) + 1
                                    create_list(num)# 调用函数create_list(num)
                                    matching_files = glob.glob(list_pattern)
                                    all_students_list_names, all_students_lists = for_matching_files_data(matching_files)# 刷新matching_files数据
                                elif key_str == 4:
                                    print("退出...")
                                    time.sleep(0.5)
                                    break_flag = True
                                    break
                                else:
                                    print("超出范围，请重新选择")
                                    time.sleep(0.5)
                            else:
                                print("输入无效，请输入数字按键")
                                time.sleep(0.5)
                    else:
                        print("× 密码错误")
                        error_count += 1
                        if error_count %5 == 0:
                            time.sleep(0.5)
                            print(f"\n您已经输错{error_count}次密码了...")
                        time.sleep(0.25)
                    if break_flag: 
                        break
            else:
                print("输入无效，有效命令如下：")
                time.sleep(0.75)
                print("1.输入数字,抽取一定数目的学生\n2.输入“清空记录、清空、qingkong、QINGKONG、qk、QK、C、c、clean、Clean”清空学生记录\n3.输入“添加记录、添加、tianjia、TIANJIA、tj、TJ、tjjl、TJJL”以手动添加学生的抽取记录\n4.输入“记录、jilu、JILU、jl、JL、recorded”查看已经记录的学生\n5.输入“修改密码、xgmm、password”以修改密码\n6.输入“修改学生名单、xgxsmd、XGXSMD、xg、XG、list”以修改学生名单")
    except BaseException as e:
        logging.exception(f"发生了一个错误: %s{e}\n")
        sentence = f"\n**************************************************\n\n× 程序出现异常，这是错误信息：\n\n{e}\n\n若要查看详细信息，请前往桌面错误日志\n**************************************************\n\n"
        for char in sentence:
            print(char, end="")
            sys.stdout.flush()
            if char in ["，", "：", "。"]:
                time.sleep(0.5)
            elif char in ["*"]:
                time.sleep(0.005)
            else:
                time.sleep(0.01)
        time.sleep(2)
