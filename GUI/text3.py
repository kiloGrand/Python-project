import tkinter

window = tkinter.Tk()#实例化object,建立窗口

window.title('MY WINDOW')#给窗口起名字

window.geometry('500x300')#设置窗口大小

#在图形界面上设定输入框控件entry并放置控件
e1 = tkinter.Entry(window,
                   show = '*',
                   font = ('Arial',14))# 显示成密文形式

e2 = tkinter.Entry(window,
                   show = None,
                   font = ('Arial',14)) # 显示成明文形式

e1.pack()
e2.pack()

window.mainloop()
