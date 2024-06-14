# 随机抽取 v2.2

### 更新要点：

1.输入密码时隐藏密码

2.桌面的错误日志文件仅在需要时才创建

# 随机抽取 v2.1
### 更新要点：
1.修复了一些BUG

2.更新了图标

# 随机抽取 v2.0
## 更新要点：

1.支持自定义名单，用户可以通过桌面的[请在这里输入学生名单.txt]输入学生名单，之后程序会读取这个txt文本文档，将名单外置在指定的目录。 

2.名单加密储存：使用Fernet加密技术，将学生名单数据加密后，储存到指定目录。 

3.可以随时更改学生名单，更改时，需要输入密码进行身份验证，然后，选择指定的学生名单，程序会对其进行解密并转存到桌面，用户对其进行更改后，程序将应用更改到加密的名单。 

4.当然，密码也可以随时更改！ 

更多BUG...啊呸,,更多内容，等你探索！


有效命令如下：
```
1.输入数字,抽取一定数目的学生
2.输入“清空记录、清空、qingkong、QINGKONG、qk、QK、C、c、clean、Clean”清空学生记录
3.输入“添加记录、添加、tianjia、TIANJIA、tj、TJ、tjjl、TJJL”以手动添加学生的抽取记录
4.输入“记录、jilu、JILU、jl、JL、recorded”查看已经记录的学生
5.输入“修改密码、xgmm、password”以修改密码
6.输入“修改学生名单、xgxsmd、XGXSMD、xg、XG、list”以修改学生名单
```
