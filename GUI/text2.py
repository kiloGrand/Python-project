import tkinter

window = tkinter.Tk()#实例化object,建立窗口

window.title('MY WINDOW')#给窗口起名字

window.geometry('500x300')#设置窗口大小

var = tkinter.StringVar()#在图形界面上设定标签,将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

label = tkinter.Label(window,
                      textvariable = var,
                      bg = 'green',
                      fg = 'white',
                      font = ('Arial',12),
                      width = 30,
                      height = 2)# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

label.pack()


# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('!')


#在窗口界面设置放置Button按键
button = tkinter.Button(window,
                        text = 'hit me',
                        font = ('AArial',12),
                        width = 10,
                        height = 1,
                        command = hit_me)

button.pack()

window.mainloop()
