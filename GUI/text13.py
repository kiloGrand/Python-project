# Grid：The Grid Geometry Manager　　
#grid 是方格, 所以所有的内容会被放在这些规律的方格中。例如：
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        
'''
以上的代码就是创建一个三行三列的表格，其实 grid 就是用表格的形式定位的。
这里的参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，
ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距。
'''

#2. Pack：The Pack Geometry Manager
#我们常用的pack(), 他会按照上下左右的方式排列.例如：
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='red').pack(side='bottom') # 下
tk.Label(window, text='P', fg='red').pack(side='left')   # 左
tk.Label(window, text='P', fg='red').pack(side='right')  # 右


#3. Place：The Place Geometry Manager
#再接下来我们来看place(), 这个比较容易理解，就是给精确的坐标来定位，如此处给的(50, 100)，
#就是将这个部件放在坐标为(x=50, y=100)的这个位置, 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。例如：
tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw') 
