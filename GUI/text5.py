import tkinter 
 
# 实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
# 设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

#在图形界面上创建一个标签label用以显示并放置
var1 = tkinter.StringVar()# 创建变量，用var1用来接收鼠标点击具体选项的内容
var1.set('please insert')#默认显示
label = tkinter.Label(window,
                      bg = 'yellow',
                      fg = 'red',
                      font = ('Arial',12),
                      width = 10,
                      textvariable = var1)
label.pack()

#创建一个按钮并放置，点击按钮调用print_selection函数
def print_selection():
    value = listbox.get(listbox.curselection()) # 获取当前选中的文本
    var1.set(value)# 为label设置值
    
button = tkinter.Button(window,
                        text = 'print selection',
                        width = 15,
                        height = 2,
                        command = print_selection)
button.pack()

# 创建Listbox并为其添加内容
var2 = tkinter.StringVar()
var2.set((1,2,3,4))# 为变量var2设置值
# 创建Listbox
listbox = tkinter.Listbox(window,
                          listvariable = var2)#将var2的值赋给Listbox
'''
#创建一个list元组并将值循环添加到Listbox控件中
list_items = [11,22,33,44]
for item in list_items:
    listbox.insert('end',item)# 从最后一个位置开始加入值
listbox.insert(1, 'first')       # 在第一个位置加入'first'字符
listbox.insert(2, 'second')      # 在第二个位置加入'second'字符
listbox.delete(2)                # 删除第二个位置的字符'''
listbox.pack()
 
# 第8步，主窗口循环显示
window.mainloop()

