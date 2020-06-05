import tkinter

window = tkinter.Tk()#实例化object,建立窗口

window.title('MY WINDOW')#给窗口起名字

window.geometry('500x300')#设置窗口大小

label = tkinter.Label(window,
                      text = 'hello!',
                      bg = 'red',#标签背景颜色
                      font = ('Arial',12),#字体类型和大小
                      width = 30,
                      height = 2)#标签有30个字符宽度，2个字符高度

label.pack()#label内容conent区域放置位置，自动调节尺寸
            #放置label的方法有1.pack();2.place()


window.mainloop()#主窗口循环显示,注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
