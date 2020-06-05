import tkinter  # 使用Tkinter前需要先导入
 
# 实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
#设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 在图形界面上创建一个标签label用以显示并放置
var = tkinter.StringVar()# 定义一个var用来将radiobutton的值和Label的值联系在一起
label = tkinter.Label(window,
                      bg = 'yellow',
                      width = 20,
                      text = 'please choose'
                      )
label.pack()

#定义选项触发函数功能
def print_selection():
    label.config(text='you have selected ' + var.get())
# 创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
radiobutton1 = tkinter.Radiobutton(window,
                                   text = 'option A',
                                   variable = var,
                                   value = 'A',
                                   command = print_selection)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(window,
                                   text = 'option B',
                                   variable = var,
                                   value = 'B',
                                   command = print_selection)
radiobutton2.pack()
radiobutton3 = tkinter.Radiobutton(window,
                                   text = 'option C',
                                   variable = var,
                                   value = 'C',
                                   command = print_selection)
radiobutton3.pack()

# 主窗口循环显示
window.mainloop()
