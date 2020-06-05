import tkinter   # 使用Tkinter前需要先导入
 
#实例化object，建立窗口window
window = tkinter.Tk()
 
# 给窗口的可视化起名字
window.title('My Window')
 
# 设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tkinter.Canvas(window,
                        bg = 'yellow',
                        height = 200,
                        width = 500)
# 说明图片位置，并导入图片到画布上
image_file = tkinter.PhotoImage(file = 'E:\\py-project\\a.gif')# 图片位置
image = canvas.create_image(250,20,anchor = 'n',image = image_file)# 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='red')  # 画圆 用黄色填充
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形

canvas.pack()

window.mainloop()
