import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('医院信息管理系统')
        self.window.geometry('600x700')
         # 这里的乘是小x
        # 创建一个图片管理类
        label =tk.Label(self.window,
                        text="医院信息管理系统",
                        justify=tk.LEFT,
                        compound=tk.CENTER,
                        font=("Verdana", 20),
                        fg="black")
        # label=Label(self.window,text="医院信息管理系统", font=("Verdana", 20),image=photo)  # 把图片整合到标签类中
        label.pack(pady=10)  # pady=100 界面的长度
        Button(self.window, text="管理员登陆", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), width=30,
               height=2,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="游客登陆", font=tkFont.Font(size=16), command=lambda: StudentPage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="关于", font=tkFont.Font(size=16), command=lambda: AboutPage(self.window), width=30,
               height=2,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环
# 管理员登陆页面的初始化
class AdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('400x400') # 这里的乘是小x
        label = tk.Label(self.window, text='管理员登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()
        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()
        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()
        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=lambda:Gongnengjiemian(self.window),fg='white', bg='gray', activebackground='black', activeforeground='white').pack(pady=20)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
            StartPage(self.window)  # 显示主窗口 销毁本窗口
#功能界面的初始化、实现管理员登录
class Gongnengjiemian:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window= tk.Tk()  # 初始框的声明
        self.window.title('功能选择界面')
        self.window.geometry('300x450')  # 这里的乘是小x
        Button(self.window, text="科室管理", width=18, font=tkFont.Font(size=12), command=lambda: AdminManage(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="医生资料管理", width=18, font=tkFont.Font(size=12), command=lambda: AdminManage1(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="护士资料管理", width=18, font=tkFont.Font(size=12),command=lambda: AdminManage2(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="患者资料管理", width=18, font=tkFont.Font(size=12),command=lambda: AdminManage3(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="药品资料管理", width=18, font=tkFont.Font(size=12),command=lambda: AdminManage4(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="病房资料管理", width=18, font=tkFont.Font(size=12), command=lambda: AdminManage5(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="病人用药记录管理", width=18, font=tkFont.Font(size=12),  command=lambda: AdminManage6(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="护士护理记录管理", width=18, font=tkFont.Font(size=12),  command=lambda: AdminManage7(self.window),fg='white', bg='green', activebackground='black', activeforeground='white').pack(pady=10)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None
        # 数据库操作 查询管理员表
        db = pymysql.Connect(
                     host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='hospital',
                     charset='utf8'
                     )  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login_k WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
                print("Error: unable to fecth data")
                messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接
        print("正在登陆管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)
        if self.admin_pass.get() == admin_pass:
            AdminManage(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')


    def back(self):

        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 游客登陆页面的初始化
class StudentPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('游客登陆')
        self.window.geometry('300x450')  # 这里的乘是小x
        label = tk.Label(self.window, text='游客登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()
        Label(self.window, text='游客账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.student_id.pack()
        Label(self.window, text='游客密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.student_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.student_pass.pack()
        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login,fg='white', bg='gray', activebackground='black', activeforeground='white').pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back,fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def login(self):
        print(str(self.student_id.get()))
        print(str(self.student_pass.get()))
        stu_pass = None
        # 数据库操作 查询管理员表
        db = pymysql.Connect(
                     host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='hospital',
                     charset='utf8'
                       )  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM stu_login_k WHERE stu_id = '%s'" % (self.student_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_pass = row[1]
                # 打印结果
                print("stu_id=%s,stu_pass=%s" % (stu_id, stu_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接
        print("正在登陆游客查看界面")
        print("self", self.student_pass.get())
        print("local", stu_pass)
        if self.student_pass.get() == stu_pass:
            StudentView(self.window, self.student_id.get())  # 进入学生信息查看界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# 科室资料管理操作界面
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('科室资料操作界面')
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)
        # 定义下方中心列表区域
        self.columns = ("科室名", "编号", "地址", "电话")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("科室名", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("编号", width=150, anchor='center')
        self.tree.column("地址", width=100, anchor='center')
        self.tree.column("电话", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.dpname = []
        self.dpno = []
        self.dpadr = []
        self.dptel = []
        # 打开数据库连接
        db = pymysql.Connect(

               host='127.0.0.1',

               port=3306,

               user='root',

               passwd='root',

               db='hospital',

               charset='utf8'

               )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM department"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.dpname.append(row[0])
                self.dpno.append(row[1])
                self.dpadr.append(row[2])
                self.dptel.append(row[3])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.dpname), len(self.dpno), len(self.dpadr), len(self.dptel))):  # 写入数据
            self.tree.insert('', i, values=(self.dpname[i], self.dpno[i], self.dpadr[i], self.dptel[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="科室信息",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_dpname = StringVar()  # 声明科室名
        self.var_dpno = StringVar()  # 声明编号
        self.var_dpadr = StringVar()  # 声明地址
        self.var_dptel = StringVar()  # 声明电话
        # 科室名
        self.right_top_dpname_label = Label(self.frame_left_top, text="科室名：", font=('Verdana', 15))
        self.right_top_dpname_entry = Entry(self.frame_left_top, textvariable=self.var_dpname, font=('Verdana', 15))
        self.right_top_dpname_label.grid(row=1, column=0)  # 位置设置
        self.right_top_dpname_entry.grid(row=1, column=1)
        # 编号
        self.right_top_dpno_label = Label(self.frame_left_top, text="编号：",font=('Verdana', 15))
        self.right_top_dpno_entry = Entry(self.frame_left_top, textvariable=self.var_dpno, font=('Verdana', 15))
        self.right_top_dpno_label.grid(row=2, column=0)  # 位置设置
        self.right_top_dpno_entry.grid(row=2, column=1)
        # 地址
        self.right_top_dpadr_label = Label(self.frame_left_top, text="地址：", font=('Verdana', 15))
        self.right_top_dpadr_entry = Entry(self.frame_left_top, textvariable=self.var_dpadr,font=('Verdana', 15))
        self.right_top_dpadr_label.grid(row=3, column=0)  # 位置设置
        self.right_top_dpadr_entry.grid(row=3, column=1)
        # 电话
        self.right_top_dptel_label = Label(self.frame_left_top, text="电话：", font=('Verdana', 15))
        self.right_top_dptel_entry = Entry(self.frame_left_top, textvariable=self.var_dptel, font=('Verdana', 15))
        self.right_top_dptel_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dptel_entry.grid(row=4, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建科室信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中科室信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中科室信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_dpname.set(self.row_info[0])
        self.var_dpno.set(self.row_info[1])
        self.var_dpadr.set(self.row_info[2])
        self.var_dptel.set(self.row_info[3])
        self.right_top_dpname_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_dpname,font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        print('123')
        print(self.var_dpname.get())
        print(self.dpname)
        if str(self.var_dpname.get()) in self.dpname:
            messagebox.showinfo('警告！', '该科室已存在！')
        else:
            if self.var_dpname.get() != '' and self.var_dpno.get() != '' and self.var_dpadr.get() != '' and self.var_dptel.get() != '':
                # 打开数据库连接
                db = pymysql.Connect(
                          host='127.0.0.1',

                          port=3306,

                          user='root',

                          passwd='root',

                          db='hospital',

                          charset='utf8'

                  )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO department(dpname, dpno, dpadr, dptel) VALUES('%s', '%s', '%s', '%s') " % (self.var_dpname.get(), self.var_dpno.get(), self.var_dpadr.get(), self.var_dptel.get())  # SQL 插入语句
                try:
                       cursor.execute(sql)  # 执行sql语句
                       db.commit()  # 提交到数据库执行
                except:
                       db.rollback()  # 发生错误时回滚
                       messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.dpname.append(self.var_dpname.get())
                self.dpno.append(self.var_dpno.get())
                self.dpadr.append(self.var_dpadr.get())
                self.dptel.append(self.var_dptel.get())
                self.tree.insert('', len(self.dpname) - 1, values=(
                self.dpname[len(self.dpname) - 1], self.dpno[len(self.dpname) - 1], self.dpadr[len(self.dpname) - 1],self.dptel[len(self.dpname) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写科室数据')
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_dpname.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE department SET dpno = '%s', dpadr = '%s', dptel = '%s' WHERE dpname= '%s'" % (self.var_dpno.get(), self.var_dpadr.get(), self.var_dptel.get(), self.var_dpname.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      dpname_index = self.dpname.index(self.row_info[0])
                      self.dpname[dpname_index] = self.var_dpname.get()
                      self.dpadr[dpname_index] = self.var_dpadr.get()
                      self.dptel[dpname_index] = self.var_dptel.get()
                      self.tree.item(self.tree.selection()[0], values=(self.var_dpname.get(), self.var_dpno.get(), self.var_dpadr.get(),self.var_dptel.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改科室姓名！')
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
        # 打开数据库连接
            db= pymysql.Connect(
                  host='127.0.0.1',
                  port=3306,
                  user='root',
                  passwd='root',
                  db='hospital',
                  charset='utf8'
)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM department WHERE dpname = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                  cursor.execute(sql)  # 执行sql语句
                  db.commit()  # 提交到数据库执行
                  messagebox.showinfo('提示！', '删除成功！')
            except:
                  db.rollback()  # 发生错误时回滚
                  messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接
            dpname_index = self.dpno.index(self.row_info[0])
            print(dpname_index)
            del self.dpname[dpname_index]
            del self.dpno[dpname_index]
            del self.dpadr[dpname_index]
            del self.dptel[dpname_index]
            print(self.dpno)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 医生资料管理操作界面
class AdminManage1:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('医生资料管理界面')
        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=700, height=800)
        self.frame_bottom = tk.Frame(width=700, height=10)
        # 定义下方中心列表区域
        self.columns = ("编号", "医生名", "职称", "性别","年龄","科室")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("编号", width=80, anchor='center')  # 表示列,不显示
        self.tree.column("医生名", width=100, anchor='center')
        self.tree.column("职称", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("科室", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.dno = []
        self.dname = []
        self.duty = []
        self.dsex = []
        self.dage = []
        self.dpno= []
        # 打开数据库连接
        db = pymysql.Connect(

               host='127.0.0.1',

               port=3306,

               user='root',

               passwd='root',

               db='hospital',

               charset='utf8'

               )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM doctor"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.dno.append(row[0])
                self.dname.append(row[1])
                self.duty.append(row[2])
                self.dsex.append(row[3])
                self.dage.append(row[4])
                self.dpno.append(row[5])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.dno), len(self.dname), len(self.duty), len(self.dsex),len(self.dage),len(self.dpno))):  # 写入数据
            self.tree.insert('', i, values=(self.dno[i], self.dname[i], self.duty[i], self.dsex[i],self.dage[i],self.dpno[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="医生信息",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_dno = StringVar()  # 声明医生编号
        self.var_dname= StringVar()  # 声明医生名字
        self.var_duty = StringVar()  # 声明职称
        self.var_dsex = StringVar()  # 声明性别
        self.var_dage= StringVar()  # 声明年龄
        self.var_dpno = StringVar()  # 声明科室
        # 医生编号
        self.right_top_dno_label = Label(self.frame_left_top, text="编号：", font=('Verdana', 15))
        self.right_top_dno_entry = Entry(self.frame_left_top, textvariable=self.var_dno, font=('Verdana', 15))
        self.right_top_dno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_dno_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_dname_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_dname_entry = Entry(self.frame_left_top, textvariable=self.var_dname, font=('Verdana', 15))
        self.right_top_dname_label.grid(row=2, column=0)  # 位置设置
        self.right_top_dname_entry.grid(row=2, column=1)
        # 职称
        self.right_top_duty_label = Label(self.frame_left_top, text="职称：", font=('Verdana', 15))
        self.right_top_duty_entry = Entry(self.frame_left_top, textvariable=self.var_duty,font=('Verdana', 15))
        self.right_top_duty_label.grid(row=3, column=0)  # 位置设置
        self.right_top_duty_entry.grid(row=3, column=1)
        # 性别
        self.right_top_dsex_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_dsex_entry = Entry(self.frame_left_top, textvariable=self.var_dsex, font=('Verdana', 15))
        self.right_top_dsex_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dsex_entry.grid(row=4, column=1)
        # 年龄
        self.right_top_dage_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_dage_entry = Entry(self.frame_left_top, textvariable=self.var_dage, font=('Verdana', 15))
        self.right_top_dage_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dage_entry.grid(row=5, column=1)
        # 科室
        self.right_top_dpno_label = Label(self.frame_left_top, text="科室：", font=('Verdana', 15))
        self.right_top_dpno_entry = Entry(self.frame_left_top, textvariable=self.var_dpno, font=('Verdana', 15))
        self.right_top_dpno_label.grid(row=6, column=0)  # 位置设置
        self.right_top_dpno_entry.grid(row=6, column=1)
        # 操作
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建医生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中医生信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中医生信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_dno.set(self.row_info[0])
        self.var_dname.set(self.row_info[1])
        self.var_duty.set(self.row_info[2])
        self.var_dsex.set(self.row_info[3])
        self.var_dage.set(self.row_info[4])
        self.var_dpno.set(self.row_info[5])
        self.right_top_dno_entry= Entry(self.frame_left_top, state='disabled', textvariable=self.var_dno,font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        print('123')
        print(self.var_dno.get())
        print(self.dno)
        if str(self.var_dno.get()) in self.dno:
            messagebox.showinfo('警告！', '该医生已存在！')
        else:
            if self.var_dno.get() != '' and self.var_dname.get() != '' and self.var_duty.get() != '' and self.var_dsex.get() != ''and self.var_dage.get()!=''and self.var_dpno.get()!='':
                # 打开数据库连接
                db = pymysql.Connect(
                          host='127.0.0.1',

                          port=3306,

                          user='root',

                          passwd='root',

                          db='hospital',

                          charset='utf8'

                  )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO doctor(dno, dname, duty, dsex,dage,dpno) VALUES('%s', '%s', '%s', '%s','%s','%s') " % (self.var_dno.get(), self.var_dname.get(), self.var_duty.get(), self.var_dsex.get(),self.var_dage.get(),self.var_dpno.get())  # SQL 插入语句
                try:
                       cursor.execute(sql)  # 执行sql语句
                       db.commit()  # 提交到数据库执行
                except:
                       db.rollback()  # 发生错误时回滚
                       messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.dno.append(self.var_dno.get())
                self.dname.append(self.var_dname.get())
                self.duty.append(self.var_duty.get())
                self.dsex.append(self.var_dsex.get())
                self.dage.append(self.var_dage.get())
                self.dpno.append(self.var_dpno.get())
                self.tree.insert('', len(self.dno) - 1, values=(
                self.dno[len(self.dno) - 1], self.dname[len(self.dno) - 1], self.duty[len(self.dno) - 1],self.dsex[len(self.dno) - 1],self.dage[len(self.dno) - 1],self.dpno[len(self.dno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                 messagebox.showinfo('警告！', '请填写医生数据')
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_dno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE doctor SET dname = '%s', duty = '%s',dsex='%s',dage='%s',dpno='%s' WHERE dno= '%s'" % (self.var_dname.get(),self.var_duty.get(), self.var_dsex.get(), self.var_dage.get(),self.var_dpno.get(),self.var_dno.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      dno_index = self.dno.index(self.row_info[0])
                      self.dname[dno_index] = self.var_dname.get()
                      self.duty[dno_index] = self.var_duty.get()
                      self.dsex[dno_index] = self.var_dsex.get()
                      self.dage[dno_index] = self.var_dage.get()
                      self.dpno[dno_index] = self.var_dpno.get()
                      self.tree.item(self.tree.selection()[0], values=(self.var_dno.get(), self.var_dname.get(), self.var_duty.get(),self.var_dsex.get(),self.var_dage.get(),self.var_dpno.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改医生编号！')
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
        # 打开数据库连接
            db= pymysql.Connect(
                  host='127.0.0.1',
                  port=3306,
                  user='root',
                  passwd='root',
                  db='hospital',
                  charset='utf8'
)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM doctor WHERE dno = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                  cursor.execute(sql)  # 执行sql语句
                  db.commit()  # 提交到数据库执行
                  messagebox.showinfo('提示！', '删除成功！')
            except:
                  db.rollback()  # 发生错误时回滚
                  messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接
            dno_index = self.dno.index(self.row_info[0])
            print(dno_index)
            del self.dno[dno_index]
            del self.dname[dno_index]
            del self.duty[dno_index]
            del self.dsex[dno_index]
            del self.dage[dno_index]
            del self.dpno[dno_index]
            print(self.dno)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
#护士资料管理操作界面
class AdminManage2:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('护士资料管理界面')
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)
        # 定义下方中心列表区域
        self.columns = ("护士编号", "护士名", "性别", "年龄")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("护士编号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("护士名", width=150, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.nno = []
        self.nname = []
        self.nsex = []
        self.nage = []
        # 打开数据库连接
        db = pymysql.Connect(

            host='127.0.0.1',

            port=3306,

            user='root',

            passwd='root',

            db='hospital',

            charset='utf8'

        )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM nurse"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.nno.append(row[0])
                self.nname.append(row[1])
                self.nsex.append(row[2])
                self.nage.append(row[3])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.nno), len(self.nname), len(self.nsex), len(self.nage))):  # 写入数据
            self.tree.insert('', i, values=(self.nno[i], self.nname[i], self.nsex[i], self.nage[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="护士信息",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_nno = StringVar()  # 声明编号名
        self.var_nname = StringVar()  # 声明护士名
        self.var_nsex = StringVar()  # 声明性别
        self.var_nage = StringVar()  # 声明年龄
        # 编号
        self.right_top_nno_label = Label(self.frame_left_top, text="护士编号：", font=('Verdana', 15))
        self.right_top_nno_entry = Entry(self.frame_left_top, textvariable=self.var_nno, font=('Verdana', 15))
        self.right_top_nno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_nno_entry.grid(row=1, column=1)
        # 护士名
        self.right_top_nname_label = Label(self.frame_left_top, text="护士名：", font=('Verdana', 15))
        self.right_top_nname_entry = Entry(self.frame_left_top, textvariable=self.var_nname, font=('Verdana', 15))
        self.right_top_nname_label.grid(row=2, column=0)  # 位置设置
        self.right_top_nname_entry.grid(row=2, column=1)
        # 性别
        self.right_top_nsex_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_nsex_entry = Entry(self.frame_left_top, textvariable=self.var_nsex, font=('Verdana', 15))
        self.right_top_nsex_label.grid(row=3, column=0)  # 位置设置
        self.right_top_nsex_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_nage_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_nage_entry = Entry(self.frame_left_top, textvariable=self.var_nage, font=('Verdana', 15))
        self.right_top_nage_label.grid(row=4, column=0)  # 位置设置
        self.right_top_nage_entry.grid(row=4, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建护士信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中护士信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中护士信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_nno.set(self.row_info[0])
        self.var_nname.set(self.row_info[1])
        self.var_nsex.set(self.row_info[2])
        self.var_nage.set(self.row_info[3])
        self.right_top_nno_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_nno,
                                         font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_nno.get())
        print(self.nno)
        if str(self.var_nno.get()) in self.nno:
            messagebox.showinfo('警告！', '该护士已存在！')
        else:
            if self.var_nno.get() != '' and self.var_nname.get() != '' and self.var_nsex.get() != '' and self.var_nage.get() != '':
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',

                    port=3306,

                    user='root',

                    passwd='root',

                    db='hospital',

                    charset='utf8'

                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO nurse(nno, nname, nsex, nage) VALUES('%s', '%s', '%s', '%s') " % (
                self.var_nno.get(), self.var_nname.get(), self.var_nsex.get(), self.var_nage.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.nno.append(self.var_nno.get())
                self.nname.append(self.var_nname.get())
                self.nsex.append(self.var_nsex.get())
                self.nage.append(self.var_nage.get())
                self.tree.insert('', len(self.nno) - 1, values=(
                    self.nno[len(self.nno) - 1], self.nname[len(self.nno) - 1], self.nsex[len(self.nno) - 1],
                    self.nage[len(self.nno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写护士数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_nno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE nurse SET nname = '%s', nsex = '%s', nage = '%s' WHERE nno= '%s'" % (self.var_nname.get(), self.var_nsex.get(), self.var_nage.get(), self.var_nno.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      nno_index = self.nno.index(self.row_info[0])
                      self.nname[nno_index] = self.var_nname.get()
                      self.nsex[nno_index] = self.var_nsex.get()
                      self.nage[nno_index] = self.var_nage.get()
                      self.tree.item(self.tree.selection()[0], values=(self.var_nno.get(), self.var_nname.get(), self.var_nsex.get(),self.var_nage.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改护士编号！')

    def del_row(self):
            res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
            if res == True:
                print(self.row_info[0])  # 鼠标选中的学号
                print(self.tree.selection()[0])  # 行号
                print(self.tree.get_children())  # 所有行
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "DELETE FROM nurse WHERE nno = '%s'" % (self.row_info[0])  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                nno_index = self.nno.index(self.row_info[0])
                print(nno_index)
                del self.nno[nno_index]
                del self.nname[nno_index]
                del self.nsex[nno_index]
                del self.nage[nno_index]
                print(self.nno)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
#患者资料管理操作界面
class AdminManage3:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('患者资料管理界面')
        self.window.geometry('800x1000')
        self.frame_left_top = tk.Frame(width=300, height=350)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=800, height=800)
        self.frame_bottom = tk.Frame(width=700, height=30)
        # 定义下方中心列表区域
        self.columns = ("编号", "患者名", "性别", "年龄","医生","病房","病症","治疗时间","康复时间")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("编号", width=80, anchor='center')  # 表示列,不显示
        self.tree.column("患者名", width=80, anchor='center')
        self.tree.column("性别", width=80, anchor='center')
        self.tree.column("年龄", width=80, anchor='center')
        self.tree.column("医生", width=80, anchor='center')
        self.tree.column("病房", width=80, anchor='center')
        self.tree.column("病症", width=80, anchor='center')
        self.tree.column("治疗时间", width=80, anchor='center')
        self.tree.column("康复时间", width=80, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.pno = []
        self.pname = []
        self.psex = []
        self.page = []
        self.dno = []
        self.rno= []
        self.illness=[]
        self.startdate=[]
        self.predictenddate=[]
        # 打开数据库连接
        db = pymysql.Connect(

               host='127.0.0.1',

               port=3306,

               user='root',

               passwd='root',

               db='hospital',

               charset='utf8'

               )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM patient"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.pno.append(row[0])
                self.pname.append(row[1])
                self.psex.append(row[2])
                self.page.append(row[3])
                self.dno.append(row[4])
                self.rno.append(row[5])
                self.illness.append(row[6])
                self.startdate.append(row[7])
                self.predictenddate.append(row[8])

            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.pno), len(self.pname), len(self.psex), len(self.page),len(self.dno),len(self.rno),len(self.illness),len(self.startdate),len(self.predictenddate))):  # 写入数据
            self.tree.insert('', i, values=(self.pno[i], self.pname[i], self.psex[i], self.page[i],self.dno[i],self.rno[i],self.illness[i],self.startdate[i],self.predictenddate[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="患者信息", bg='green',font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_pno = StringVar()  # 声明编号
        self.var_pname= StringVar()  # 声明名字
        self.var_psex = StringVar()  # 声明性别
        self.var_page = StringVar()  # 声明年龄
        self.var_dno= StringVar()  # 声明医生
        self.var_rno = StringVar() # 声明病房
        self.var_illness= StringVar()
        self.var_startdate = StringVar()
        self.var_predictenddate= StringVar()
        # 护士编号
        self.right_top_pno_label = Label(self.frame_left_top, text="编号：", font=('Verdana', 15))
        self.right_top_pno_entry = Entry(self.frame_left_top, textvariable=self.var_pno, font=('Verdana', 15))
        self.right_top_pno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_pno_entry.grid(row=1, column=1)
        # 护士姓名
        self.right_top_pname_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_pname_entry = Entry(self.frame_left_top, textvariable=self.var_pname, font=('Verdana', 15))
        self.right_top_pname_label.grid(row=2, column=0)  # 位置设置
        self.right_top_pname_entry.grid(row=2, column=1)
        # 性别
        self.right_top_psex_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_psex_entry = Entry(self.frame_left_top, textvariable=self.var_psex,font=('Verdana', 15))
        self.right_top_psex_label.grid(row=3, column=0)  # 位置设置
        self.right_top_psex_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_page_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_page_entry = Entry(self.frame_left_top, textvariable=self.var_page, font=('Verdana', 15))
        self.right_top_page_label.grid(row=4, column=0)  # 位置设置
        self.right_top_page_entry.grid(row=4, column=1)
        # 医生
        self.right_top_dno_label = Label(self.frame_left_top, text="医生编号：", font=('Verdana', 15))
        self.right_top_dno_entry = Entry(self.frame_left_top, textvariable=self.var_dno, font=('Verdana', 15))
        self.right_top_dno_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dno_entry.grid(row=5, column=1)
        # 病房
        self.right_top_rno_label = Label(self.frame_left_top, text="科室：", font=('Verdana', 15))
        self.right_top_rno_entry = Entry(self.frame_left_top, textvariable=self.var_rno, font=('Verdana', 15))
        self.right_top_rno_label.grid(row=6, column=0)  # 位置设置
        self.right_top_rno_entry.grid(row=6, column=1)
        # 病症
        self.right_top_illness_label = Label(self.frame_left_top, text="病症：", font=('Verdana', 15))
        self.right_top_illness_entry = Entry(self.frame_left_top, textvariable=self.var_illness, font=('Verdana', 15))
        self.right_top_illness_label.grid(row=7, column=0)  # 位置设置
        self.right_top_illness_entry.grid(row=7, column=1)
        # 治疗时间
        self.right_top_startdate_label = Label(self.frame_left_top, text="治疗时间：", font=('Verdana', 15))
        self.right_top_startdate_entry = Entry(self.frame_left_top, textvariable=self.var_startdate, font=('Verdana', 15))
        self.right_top_startdate_label.grid(row=8, column=0)  # 位置设置
        self.right_top_startdate_entry.grid(row=8, column=1)
        # 康复时间
        self.right_top_predictenddate_label = Label(self.frame_left_top, text="康复时间：", font=('Verdana', 15))
        self.right_top_predictenddate_entry = Entry(self.frame_left_top, textvariable=self.var_predictenddate, font=('Verdana', 15))
        self.right_top_predictenddate_label.grid(row=9, column=0)  # 位置设置
        self.right_top_predictenddate_entry.grid(row=9, column=1)
        # 操作
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建患者信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新患者信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除患者信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_pno.set(self.row_info[0])
        self.var_pname.set(self.row_info[1])
        self.var_psex.set(self.row_info[2])
        self.var_page.set(self.row_info[3])
        self.var_dno.set(self.row_info[4])
        self.var_rno.set(self.row_info[5])
        self.var_illness.set(self.row_info[6])
        self.var_startdate.set(self.row_info[7])
        self.var_predictenddate.set(self.row_info[8])
        self.right_top_pno_entry= Entry(self.frame_left_top, state='disabled', textvariable=self.var_pno,font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        print('123')
        print(self.var_pno.get())
        print(self.pno)
        if str(self.var_pno.get()) in self.pno:
            messagebox.showinfo('警告！', '该患者已存在！')
        else:
            if self.var_pno.get() != '' and self.var_pname.get() != '' and self.var_psex.get() != '' and self.var_page.get() != ''and self.var_dno.get()!=''and self.var_rno.get()!=''and self.var_illness.get() != ''and self.var_startdate.get()!=''and self.var_predictenddate.get()!='':
                # 打开数据库连接
                db = pymysql.Connect(
                          host='127.0.0.1',

                          port=3306,

                          user='root',

                          passwd='root',

                          db='hospital',

                          charset='utf8'

                  )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO patient(pno, pname, psex, page,dno,rno,illness,startdate,predictenddate) VALUES('%s', '%s', '%s', '%s','%s','%s', '%s','%s','%s') " % (self.var_pno.get(), self.var_pname.get(), self.var_psex.get(), self.var_page.get(),self.var_dno.get(),self.var_rno.get(), self.var_illness.get(),self.var_startdate.get(),self.var_predictenddate.get())  # SQL 插入语句
                try:
                       cursor.execute(sql)  # 执行sql语句
                       db.commit()  # 提交到数据库执行
                except:
                       db.rollback()  # 发生错误时回滚
                       messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.pno.append(self.var_pno.get())
                self.pname.append(self.var_pname.get())
                self.psex.append(self.var_psex.get())
                self.page.append(self.var_page.get())
                self.dno.append(self.var_dno.get())
                self.rno.append(self.var_rno.get())
                self.illness.append(self.var_illness.get())
                self.startdate.append(self.var_startdate.get())
                self.predictenddate.append(self.var_predictenddate.get())
                self.tree.insert('', len(self.pno) - 1, values=(
                self.pno[len(self.pno) - 1], self.pname[len(self.pno) - 1], self.psex[len(self.pno) - 1],self.page[len(self.pno) - 1],self.dno[len(self.pno) - 1],self.rno[len(self.pno) - 1],self.illness[len(self.pno) - 1],self.startdate[len(self.pno) - 1],self.predictenddate[len(self.pno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                 messagebox.showinfo('警告！', '请填写患者数据')
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_pno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE patient SET pname = '%s', psex = '%s',page='%s',dno='%s',rno='%s',illness='%s',startdate='%s',predictenddate='%s' WHERE pno= '%s'" % (self.var_pname.get(),self.var_psex.get(), self.var_page.get(), self.var_dno.get(),self.var_rno.get(),self.var_illness.get(), self.var_startdate.get(),self.var_predictenddate.get(),self.var_pno.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      pno_index = self.pno.index(self.row_info[0])
                      self.pname[pno_index] = self.var_pname.get()
                      self.psex[pno_index] = self.var_psex.get()
                      self.page[pno_index] = self.var_page.get()
                      self.dno[pno_index] = self.var_dno.get()
                      self.rno[pno_index] = self.var_rno.get()
                      self.illness[pno_index] = self.var_illness.get()
                      self.startdate[pno_index] = self.var_startdate.get()
                      self.predictenddate[pno_index] = self.var_predictenddate.get()

                      self.tree.item(self.tree.selection()[0], values=(self.var_pno.get(), self.var_pname.get(), self.var_psex.get(),self.var_page.get(),self.var_dno.get(),self.var_rno.get(),self.var_illness.get(),self.var_startdate.get(),self.var_predictenddate.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改患者编号！')
    def del_row(self):
            res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
            if res == True:
                print(self.row_info[0])  # 鼠标选中的学号
                print(self.tree.selection()[0])  # 行号
                print(self.tree.get_children())  # 所有行
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "DELETE FROM patient WHERE pno= '%s'" % (self.row_info[0])  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                pno_index = self.pno.index(self.row_info[0])
                print(pno_index)
                del self.pno[pno_index ]
                del self.pname[pno_index]
                del self.psex[pno_index]
                del self.page[pno_index]
                del self.dno[pno_index]
                del self.rno[pno_index]
                del self.illness[pno_index]
                del self.startdate[pno_index]
                del self.predictenddate[pno_index]
                print(self.pno)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
#药品资料管理操作界面
class AdminManage4:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('药品资料管理界面')
        self.window.geometry('800x1000')
        self.frame_left_top = tk.Frame(width=300, height=220)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=800)
        self.frame_bottom = tk.Frame(width=500, height=30)
        # 定义下方中心列表区域
        self.columns = ("编号", "药品名", "产名", "库存","价格")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=15, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("编号", width=80, anchor='center')  # 表示列,不显示
        self.tree.column("药品名", width=80, anchor='center')
        self.tree.column("产名", width=80, anchor='center')
        self.tree.column("库存", width=80, anchor='center')
        self.tree.column("价格", width=80, anchor='center')


        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.dgno = []
        self.dgname = []
        self.dgpro = []
        self.dgnum = []
        self.dgprice = []

        # 打开数据库连接
        db = pymysql.Connect(

               host='127.0.0.1',

               port=3306,

               user='root',

               passwd='root',

               db='hospital',

               charset='utf8'

               )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM drug"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.dgno.append(row[0])
                self.dgname.append(row[1])
                self.dgpro.append(row[2])
                self.dgnum.append(row[3])
                self.dgprice.append(row[4])

            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.dgno), len(self.dgname), len(self.dgpro), len(self.dgnum),len(self.dgprice))):  # 写入数据
            self.tree.insert('', i, values=(self.dgno[i], self.dgname[i], self.dgpro[i], self.dgnum[i],self.dgprice[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="药品信息",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_dgno = StringVar()  # 声明编号
        self.var_dgname= StringVar()  # 声明药品名
        self.var_dgpro = StringVar()  # 声明厂家
        self.var_dgnum = StringVar()  # 声明库存
        self.var_dgprice= StringVar()  # 声明价格

        # 药品编号
        self.right_top_dgno_label = Label(self.frame_left_top, text="编号：", font=('Verdana', 15))
        self.right_top_dgno_entry = Entry(self.frame_left_top, textvariable=self.var_dgno, font=('Verdana', 15))
        self.right_top_dgno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_dgno_entry.grid(row=1, column=1)
        # 药品名
        self.right_top_dgname_label = Label(self.frame_left_top, text="药品名：", font=('Verdana', 15))
        self.right_top_dgname_entry = Entry(self.frame_left_top, textvariable=self.var_dgname, font=('Verdana', 15))
        self.right_top_dgname_label.grid(row=2, column=0)  # 位置设置
        self.right_top_dgname_entry.grid(row=2, column=1)
        # 厂家
        self.right_top_dgpro_label = Label(self.frame_left_top, text="厂家：", font=('Verdana', 15))
        self.right_top_dgpro_entry = Entry(self.frame_left_top, textvariable=self.var_dgpro,font=('Verdana', 15))
        self.right_top_dgpro_label.grid(row=3, column=0)  # 位置设置
        self.right_top_dgpro_entry.grid(row=3, column=1)
        # 库存
        self.right_top_dgnum_label = Label(self.frame_left_top, text="库存：", font=('Verdana', 15))
        self.right_top_dgnum_entry = Entry(self.frame_left_top, textvariable=self.var_dgnum, font=('Verdana', 15))
        self.right_top_dgnum_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dgnum_entry.grid(row=4, column=1)
        # 价钱
        self.right_top_dgprice_label = Label(self.frame_left_top, text="价格：", font=('Verdana', 15))
        self.right_top_dgprice_entry = Entry(self.frame_left_top, textvariable=self.var_dgprice, font=('Verdana', 15))
        self.right_top_dgprice_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dgprice_entry.grid(row=5, column=1)
        # 操作
        self.right_top_title = Label(self.frame_right_top, text="操作", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建药品信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新药品信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除药品信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_dgno.set(self.row_info[0])
        self.var_dgname.set(self.row_info[1])
        self.var_dgpro.set(self.row_info[2])
        self.var_dgnum.set(self.row_info[3])
        self.var_dgprice.set(self.row_info[4])
        self.right_top_dgno_entry= Entry(self.frame_left_top, state='disabled', textvariable=self.var_dgno,font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        print('123')
        print(self.var_dgno.get())
        print(self.dgno)
        if str(self.var_dgno.get()) in self.dgno:
            messagebox.showinfo('警告！', '该药品已存在！')
        else:
            if self.var_dgno.get() != '' and self.var_dgname.get() != '' and self.var_dgpro.get() != '' and self.var_dgnum.get() != ''and self.var_dgprice.get()!='':
                # 打开数据库连接
                db = pymysql.Connect(
                          host='127.0.0.1',

                          port=3306,

                          user='root',

                          passwd='root',

                          db='hospital',

                          charset='utf8'

                  )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO drug(dgno, dgname, dgpro, dgnum,dgprice) VALUES('%s', '%s', '%s', '%s','%s') " % (self.var_dgno.get(), self.var_dgname.get(), self.var_dgpro.get(), self.var_dgnum.get(),self.var_dgprice.get())  # SQL 插入语句
                try:
                       cursor.execute(sql)  # 执行sql语句
                       db.commit()  # 提交到数据库执行
                except:
                       db.rollback()  # 发生错误时回滚
                       messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.dgno.append(self.var_dgno.get())
                self.dgname.append(self.var_dgname.get())
                self.dgpro.append(self.var_dgpro.get())
                self.dgnum.append(self.var_dgnum.get())
                self.dgprice.append(self.var_dgprice.get())
                self.tree.insert('', len(self.dgno) - 1, values=(
                self.dgno[len(self.dgno) - 1], self.dgname[len(self.dgno) - 1], self.dgpro[len(self.dgno) - 1],self.dgnum[len(self.dgno) - 1],self.dgprice[len(self.dgno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                 messagebox.showinfo('警告！', '请填写药品数据')
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_dgno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE drug SET dgname = '%s', dgpro = '%s',dgnum='%s',dgprice='%s' WHERE dgno= '%s'" % (self.var_dgname.get(),self.var_dgpro.get(), self.var_dgnum.get(), self.var_dgprice.get(),self.var_dgno.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      dgno_index = self.dgno.index(self.row_info[0])
                      self.dgname[dgno_index] = self.var_dgname.get()
                      self.dgpro[dgno_index] = self.var_dgpro.get()
                      self.dgnum[dgno_index] = self.var_dgnum.get()
                      self.dgprice[dgno_index] = self.var_dgprice.get()


                      self.tree.item(self.tree.selection()[0], values=(self.var_dgno.get(), self.var_dgname.get(), self.var_dgpro.get(),self.var_dgnum.get(),self.var_dgprice.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改药品编号！')

    def del_row(self):
            res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
            if res == True:
                print(self.row_info[0])  # 鼠标选中的学号
                print(self.tree.selection()[0])  # 行号
                print(self.tree.get_children())  # 所有行
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "DELETE FROM drug WHERE dgno = '%s'" % (self.row_info[0])  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                dgno_index = self.dgno.index(self.row_info[0])
                print(dgno_index)
                del self.dgno[dgno_index]
                del self.dgname[dgno_index]
                del self.dgpro[dgno_index]
                del self.dgnum[dgno_index]
                del self.dgprice[dgno_index]
                print(self.dgno)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
#病房资料管理
class AdminManage5:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('病房资料操作界面')
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)
        # 定义下方中心列表区域
        self.columns = ("病房号", "地址", "所属科室")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("病房号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("地址", width=150, anchor='center')
        self.tree.column("所属科室", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.rno = []
        self.radr = []
        self.dpno = []
        # 打开数据库连接
        db = pymysql.Connect(

            host='127.0.0.1',

            port=3306,

            user='root',

            passwd='root',

            db='hospital',

            charset='utf8'

        )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM room"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.rno.append(row[0])
                self.radr.append(row[1])
                self.dpno.append(row[2])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.rno), len(self.radr), len(self.dpno))):  # 写入数据
            self.tree.insert('', i, values=(self.rno[i], self.radr[i], self.dpno[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="病房信息",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_rno = StringVar()  # 声明病房号
        self.var_radr = StringVar()  # 声明地址
        self.var_dpno = StringVar()  # 声明科室

        # 病房号
        self.right_top_rno_label = Label(self.frame_left_top, text="病房号：", font=('Verdana', 15))
        self.right_top_rno_entry = Entry(self.frame_left_top, textvariable=self.var_rno, font=('Verdana', 15))
        self.right_top_rno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_rno_entry.grid(row=1, column=1)
        # 地址
        self.right_top_radr_label = Label(self.frame_left_top, text="地址：", font=('Verdana', 15))
        self.right_top_radr_entry = Entry(self.frame_left_top, textvariable=self.var_radr, font=('Verdana', 15))
        self.right_top_radr_label.grid(row=2, column=0)  # 位置设置
        self.right_top_radr_entry.grid(row=2, column=1)
        # 科室
        self.right_top_dpno_label = Label(self.frame_left_top, text="科室号：", font=('Verdana', 15))
        self.right_top_dpno_entry = Entry(self.frame_left_top, textvariable=self.var_dpno, font=('Verdana', 15))
        self.right_top_dpno_label.grid(row=3, column=0)  # 位置设置
        self.right_top_dpno_entry.grid(row=3, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建病房信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新病房信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中病房信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_rno.set(self.row_info[0])
        self.var_radr.set(self.row_info[1])
        self.var_dpno.set(self.row_info[2])
        self.right_top_rno_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_rno,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_rno.get())
        print(self.rno)
        if str(self.var_rno.get()) in self.rno:
            messagebox.showinfo('警告！', '该病房已存在！')
        else:
            if self.var_rno.get() != '' and self.var_radr.get() != '' and self.var_dpno.get() != '':
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',

                    port=3306,

                    user='root',

                    passwd='root',

                    db='hospital',

                    charset='utf8'

                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO room(rno, radr, dpno) VALUES('%s', '%s', '%s') " % (
                self.var_rno.get(), self.var_radr.get(), self.var_dpno.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.rno.append(self.var_rno.get())
                self.radr.append(self.var_radr.get())
                self.dpno.append(self.var_dpno.get())
                self.tree.insert('', len(self.rno) - 1, values=(
                    self.rno[len(self.rno) - 1], self.radr[len(self.rno) - 1],
                    self.dpno[len(self.rno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写病房数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_rno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE room SET radr = '%s', dpno = '%s'WHERE rno= '%s'" % (
                self.var_radr.get(), self.var_dpno.get(), self.var_rno.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                rno_index = self.rno.index(self.row_info[0])
                self.rno[rno_index] = self.var_rno.get()
                self.radr[rno_index] = self.var_radr.get()
                self.dpno[rno_index] = self.var_dpno.get()
                self.tree.item(self.tree.selection()[0], values=(
                self.var_rno.get(), self.var_radr.get(), self.var_dpno.get()))
            else:
                messagebox.showinfo('警告！', '不能修改病房号！')

    def del_row(self):
            res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
            if res == True:
                print(self.row_info[0])  # 鼠标选中的学号
                print(self.tree.selection()[0])  # 行号
                print(self.tree.get_children())  # 所有行
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "DELETE FROM room WHERE rno = '%s'" % (self.row_info[0])  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '删除成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                rno_index = self.rno.index(self.row_info[0])
                print(rno_index)
                del self.rno[rno_index]
                del self.radr[rno_index]
                del self.dpno[rno_index]
                print(self.rno)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
#病人用药记录管理
class AdminManage6:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('患者用药记录')
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)
        # 定义下方中心列表区域
        self.columns = ("药品号", "患者号", "用药次数")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("药品号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("患者号", width=150, anchor='center')
        self.tree.column("用药次数", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.dgno = []
        self.pno = []
        self.num= []
        # 打开数据库连接
        db = pymysql.Connect(

            host='127.0.0.1',

            port=3306,

            user='root',

            passwd='root',

            db='hospital',

            charset='utf8'

        )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM PD"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.dgno.append(row[0])
                self.pno.append(row[1])
                self.num.append(row[2])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.dgno), len(self.pno), len(self.num))):  # 写入数据
            self.tree.insert('', i, values=(self.dgno[i], self.pno[i], self.num[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="病人用药记录",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_dgno= StringVar()  # 声明药品号
        self.var_pno = StringVar()  # 声明病人号
        self.var_num = StringVar()  # 声明次数

        # 病房号
        self.right_top_dgno_label = Label(self.frame_left_top, text="药品编号：", font=('Verdana', 15))
        self.right_top_dgno_entry = Entry(self.frame_left_top, textvariable=self.var_dgno, font=('Verdana', 15))
        self.right_top_dgno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_dgno_entry.grid(row=1, column=1)
        # 地址
        self.right_top_pno_label = Label(self.frame_left_top, text="患者编号：", font=('Verdana', 15))
        self.right_top_pno_entry = Entry(self.frame_left_top, textvariable=self.var_pno, font=('Verdana', 15))
        self.right_top_pno_label.grid(row=2, column=0)  # 位置设置
        self.right_top_pno_entry.grid(row=2, column=1)
        # 次数
        self.right_top_num_label = Label(self.frame_left_top, text="用药次数：", font=('Verdana', 15))
        self.right_top_num_entry = Entry(self.frame_left_top, textvariable=self.var_num, font=('Verdana', 15))
        self.right_top_num_label.grid(row=3, column=0)  # 位置设置
        self.right_top_num_entry.grid(row=3, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建用药记录信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新用药记录信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中用药记录信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_dgno.set(self.row_info[0])
        self.var_pno.set(self.row_info[1])
        self.var_num.set(self.row_info[2])
        self.right_top_dgno_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_dgno,font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def new_row(self):
        print('123')
        print(self.var_dgno.get())
        print(self.dgno)
        if str(self.var_dgno.get()) in self.dgno:
            messagebox.showinfo('警告！', '该用药记录已存在！')
        else:
            if self.var_dgno.get() != '' and self.var_pno.get() != '' and self.var_num.get() != '':
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',

                    port=3306,

                    user='root',

                    passwd='root',

                    db='hospital',

                    charset='utf8'

                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO PD(dgno, pno, num) VALUES('%s', '%s', '%s') " % (
                self.var_dgno.get(), self.var_pno.get(), self.var_num.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.dgno.append(self.var_dgno.get())
                self.pno.append(self.var_pno.get())
                self.num.append(self.var_num.get())
                self.tree.insert('', len(self.dgno) - 1, values=(
                    self.dgno[len(self.dgno) - 1], self.pno[len(self.dgno) - 1],
                    self.num[len(self.dgno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写病房数据')

    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_dgno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.Connect(
                    host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='hospital',
                    charset='utf8'
                )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE PD SET pno = '%s', num = '%s'WHERE dgno= '%s'" % (
                self.var_pno.get(), self.var_num.get(), self.var_dgno.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                dgno_index = self.dgno.index(self.row_info[0])
                self.dgno[dgno_index] = self.var_dgno.get()
                self.pno[dgno_index] = self.var_pno.get()
                self.num[dgno_index] = self.var_num.get()
                self.tree.item(self.tree.selection()[0], values=(
                self.var_dgno.get(), self.var_pno.get(), self.var_num.get()))
            else:
                messagebox.showinfo('警告！', '不能修改药品号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.Connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='root',
                db='hospital',
                charset='utf8'
            )
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM PD WHERE dgno = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接
            dgno_index = self.dgno.index(self.row_info[0])
            print(dgno_index)
            del self.dgno[dgno_index]
            del self.pno[dgno_index]
            del self.num[dgno_index]
            print(self.dgno)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
#病人护理记录管理
class AdminManage7:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = Tk()  # 初始框的声明
        self.window.title('患者护理记录操作界面')
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)
        # 定义下方中心列表区域
        self.columns = ("患者编号", "护士编号", "护理内容", "时间")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的标题
        self.tree.column("患者编号", width=150, anchor='center')  # 表示列,不显示
        self.tree.column("护士编号", width=150, anchor='center')
        self.tree.column("护理内容", width=100, anchor='center')
        self.tree.column("时间", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.pno = []
        self.nno = []
        self.content = []
        self.time = []
        # 打开数据库连接
        db = pymysql.Connect(

               host='127.0.0.1',

               port=3306,

               user='root',

               passwd='root',

               db='hospital',

               charset='utf8'

               )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM PN"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.pno.append(row[0])
                self.nno.append(row[1])
                self.content.append(row[2])
                self.time.append(row[3])
            # print(self.id)

            # print(self.name)

            # print(self.gender)

            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接
        print("test***********************")
        for i in range(min(len(self.pno), len(self.nno), len(self.content), len(self.time))):  # 写入数据
            self.tree.insert('', i, values=(self.pno[i], self.nno[i], self.content[i], self.time[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
        # 定义顶部区域

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="病人护理记录",bg='green', font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_pno = StringVar()  # 声明病人编号
        self.var_nno = StringVar()  # 声明护士编号
        self.var_content = StringVar()  # 声明内容
        self.var_time = StringVar()  # 声明时间
        # pno
        self.right_top_pno_label = Label(self.frame_left_top, text="患者编号：", font=('Verdana', 15))
        self.right_top_pno_entry = Entry(self.frame_left_top, textvariable=self.var_pno, font=('Verdana', 15))
        self.right_top_pno_label.grid(row=1, column=0)  # 位置设置
        self.right_top_pno_entry.grid(row=1, column=1)
        # 护士编号
        self.right_top_nno_label = Label(self.frame_left_top, text="护士编号：", font=('Verdana', 15))
        self.right_top_nno_entry = Entry(self.frame_left_top, textvariable=self.var_nno, font=('Verdana', 15))
        self.right_top_nno_label.grid(row=2, column=0)  # 位置设置
        self.right_top_nno_entry.grid(row=2, column=1)
        # 内容
        self.right_top_content_label = Label(self.frame_left_top, text="护理内容：", font=('Verdana', 15))
        self.right_top_content_entry = Entry(self.frame_left_top, textvariable=self.var_content,font=('Verdana', 15))
        self.right_top_content_label.grid(row=3, column=0)  # 位置设置
        self.right_top_content_entry.grid(row=3, column=1)
        # 时间
        self.right_top_time_label = Label(self.frame_left_top, text="时间：", font=('Verdana', 15))
        self.right_top_time_entry = Entry(self.frame_left_top, textvariable=self.var_time, font=('Verdana', 15))
        self.right_top_time_label.grid(row=4, column=0)  # 位置设置
        self.right_top_time_entry.grid(row=4, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建护理记录信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中护理记录信息', width=20, command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中护理记录信息', width=20, command=self.del_row)
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
       Gongnengjiemian(self.window)  # 显示主窗口 销毁本窗口
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行
        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_pno.set(self.row_info[0])
        self.var_nno.set(self.row_info[1])
        self.var_content.set(self.row_info[2])
        self.var_time.set(self.row_info[3])
        self.right_top_pno_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_pno,font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def new_row(self):
        print('123')
        print(self.var_pno.get())
        print(self.pno)
        if str(self.var_pno.get()) in self.pno:
            messagebox.showinfo('警告！', '该护理记录已存在！')
        else:
            if self.var_pno.get() != '' and self.var_nno.get() != '' and self.var_content.get() != '' and self.var_time.get() != '':
                # 打开数据库连接
                db = pymysql.Connect(
                          host='127.0.0.1',

                          port=3306,

                          user='root',

                          passwd='root',

                          db='hospital',

                          charset='utf8'

                  )
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO PN(pno, nno, content, time) VALUES('%s', '%s', '%s', '%s') " % (self.var_pno.get(), self.var_nno.get(), self.var_content.get(), self.var_time.get())  # SQL 插入语句
                try:
                       cursor.execute(sql)  # 执行sql语句
                       db.commit()  # 提交到数据库执行
                except:
                       db.rollback()  # 发生错误时回滚
                       messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                self.pno.append(self.var_pno.get())
                self.nno.append(self.var_nno.get())
                self.content.append(self.var_content.get())
                self.time.append(self.var_time.get())
                self.tree.insert('', len(self.pno) - 1, values=(
                self.pno[len(self.pno) - 1], self.nno[len(self.pno) - 1], self.content[len(self.pno) - 1],self.time[len(self.pno) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                 messagebox.showinfo('警告！', '请填写科室数据')
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
               if self.var_pno.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                      db =pymysql.Connect(
                                 host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='root',
                                 db='hospital',
                                 charset='utf8'
                                )
                      cursor = db.cursor()  # 使用cursor()方法获取操作游标
                      sql = "UPDATE PN SET nno = '%s', content = '%s', time = '%s' WHERE pno= '%s'" % (self.var_nno.get(), self.var_content.get(), self.var_time.get(), self.var_pno.get())  # SQL 插入语句
                      try:
                            cursor.execute(sql)  # 执行sql语句
                            db.commit()  # 提交到数据库执行
                            messagebox.showinfo('提示！', '更新成功！')
                      except:
                            db.rollback()  # 发生错误时回滚
                            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                      db.close()  # 关闭数据库连接
                      pno_index = self.pno.index(self.row_info[0])
                      self.nno[pno_index] = self.var_nno.get()
                      self.content[pno_index] = self.var_content.get()
                      self.time[pno_index] = self.var_time.get()
                      self.tree.item(self.tree.selection()[0], values=(self.var_pno.get(), self.var_nno.get(), self.var_content.get(),self.var_time.get()))
               else:
                      messagebox.showinfo('警告！', '不能修改患者编号！')
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
        # 打开数据库连接
            db= pymysql.Connect(
                  host='127.0.0.1',
                  port=3306,
                  user='root',
                  passwd='root',
                  db='hospital',
                  charset='utf8'
)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM PN WHERE pno = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                  cursor.execute(sql)  # 执行sql语句
                  db.commit()  # 提交到数据库执行
                  messagebox.showinfo('提示！', '删除成功！')
            except:
                  db.rollback()  # 发生错误时回滚
                  messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接
            pno_index = self.pno.index(self.row_info[0])
            print(pno_index)
            del self.pno[pno_index]
            del self.nno[pno_index]
            del self.content[pno_index]
            del self.time[pno_index]
            print(self.pno)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 游客登录后的界面初始化和操作
class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('医院基本信息')
        self.window.geometry('300x450')  # 这里的乘是小x
        label = tk.Label(self.window, text='医院信息查看', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)
        self.id = '编号:' + ''
        self.hpname = '医院名称:' + ''
        self.host = '院长:' + ''
        self.hadr = '地址:' + ''
        self.htel = '联系号码:' + ''
        # 打开数据库连接
        db = connect = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='hospital',
            charset='utf8'
        )
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM h WHERE id = '%s'" % (student_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id='编号:'+row[0]
                self.hpname= '医院名称:' + row[1]
                self.host = '院长:' + row[2]
                self.hadr = '地址:' + row[3]
                self.htel = '电话:' + row[4]
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接
        Label(self.window, text=self.id, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.hpname, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.host, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.hadr, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.htel, font=('Verdana', 18)).pack(pady=5)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16), command=self.back).pack(pady=25)
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
# About页面
class AboutPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        self.window.geometry('300x450')  # 这里的乘是小x
        label = tk.Label(self.window, text='医院信息管理系统', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()
        Label(self.window, text='作者：', font=('Verdana', 18)).pack(pady=30)
        Label(self.window, text='', font=('Verdana', 18)).pack(pady=5)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=100)
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
if __name__ == '__main__':
    try:
        # 打开数据库连接 连接测试
        db = connect = pymysql.Connect(
                   host='127.0.0.1',
                   port=3306,
                   user='root',
                   passwd='root',
                   db='hospital',
                   charset='utf8'
)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 如果数据表不存在则创建表 若存在则跳过
        #
        # 设置主键唯一
        sql = """
        CREATE TABLE IF NOT EXISTS department(
            dpname char(10) NOT NULL,
            dpno char(1) NOT NULL,
            dpadr char(20) default NULL,
            dptel char(20) default NULL,
            PRIMARY KEY (dpname)
            ) ENGINE = InnoDB
            DEFAULT    CHARSET = utf8
            """
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """
        CREATE TABLE IF NOT EXISTS admin_login_k(
                  admin_id char(20) NOT NULL,
                  admin_pass char(20) default NULL,
                  PRIMARY KEY (admin_id)
                  ) ENGINE = InnoDB
                  DEFAULT    CHARSET = utf8
                  """
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """
        CREATE TABLE IF NOT EXISTS stu_login_k(
                  stu_id char(20) NOT NULL,
                  stu_pass char(20) default NULL,
                  PRIMARY KEY (stu_id)
                  ) ENGINE = InnoDB
                  DEFAULT    CHARSET = utf8
                  """
        cursor.execute(sql)
        # 关闭数据库连接
        db.close()
        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')

