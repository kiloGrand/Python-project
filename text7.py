import tkinter  # 使用Tkinter前需要先导入
 
# 实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
# 设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 在图形界面上创建一个标签label用以显示并放置
label = tkinter.Label(window,
                      bg='yellow',
                      width=20,
                      text='please check')
label.pack()

# 定义触发函数功能
def print_selection():
    if(var1.get() == 1) & (var2.get() == 0):# 如果选中第一个选项，未选中第二个选项
        label.config(text = 'i love only Python')
    elif(var1.get() == 0) & (var2.get() == 1): # 如果选中第二个选项，未选中第一个选项
        label.config(text = 'i love only C')
    elif(var1.get() == 1) & (var2.get() == 1):# 如果两个选项都选中
        label.config(text = 'i love both')
    else:
        label.config(text = 'i do not love either')



#定义var1和var2整型变量用来存放选择行为返回值
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
# 定义两个Checkbutton选项并放置
checkbutton1 = tkinter.Checkbutton(window,
                                   text = 'python',
                                   variable = var1,
                                   onvalue = 1,
                                   offvalue = 0,
                                   command = print_selection) # 传值原理类似于radiobutton部件
checkbutton1.pack()
checkbutton2 = tkinter.Checkbutton(window,
                                   text = 'C',
                                   variable = var2,
                                   onvalue = 1,
                                   offvalue = 0,
                                   command = print_selection) # 传值原理类似于radiobutton部件
checkbutton2.pack()

# 主窗口循环显示
window.mainloop()
