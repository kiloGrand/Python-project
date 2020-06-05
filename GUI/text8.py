import tkinter #使用Tkinter前需要先导入
 
# 实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
# 设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 在图形界面上创建一个标签label用以显示并放置
label = tkinter.Label(window,
                      bg='green',
                      fg='white',
                      width=20,
                      text='how much you like me?')
label.pack()

# 定义一个触发函数功能
def print_selection(v):
    label.config(text = '程度：' + v)
    
scale = tkinter.Scale(window,
                      label = '%',
                      from_ = 0,#从0开始
                      to = 100,#到100结束
                      orient = tkinter.HORIZONTAL,#水平方向
                      length = 200,#长度200个字符
                      tickinterval = 10,#每10一个刻度
                      resolution = 1,#精度为1
                      command = print_selection)
scale.pack()

# 主窗口循环显示
window.mainloop()
