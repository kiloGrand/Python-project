import tkinter

# 实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

#在图形界面上设定输入框控件entry框并放置
e = tkinter.Entry(window,show = None)
e.pack()

# 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point(): # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert',var)

def insert_end():#在文本框内容最后接着插入输入内容
    var = e.get()#e指的是上面定义的输入框变量
    t.insert('end',var)#t指的是下面定义的文本框变量

# 创建并放置两个按钮分别触发两种情况
b1 = tkinter.Button(window,
                    text = 'insert point',
                    width = 10,
                    height = 2,
                    command = insert_point)
b1.pack()

b2 = tkinter.Button(window,
                    text = 'insert end',
                    width = 10,
                    height = 2,
                    command = insert_end)
b2.pack()

#创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tkinter.Text(window,height = 3)
t.pack()

window.mainloop()
