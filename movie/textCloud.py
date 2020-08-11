import jieba        # 分词
from matplotlib import pyplot as plt    # 数据可视化
from wordcloud import WordCloud     # 词云
from PIL import Image       # 图片处理
import numpy as np      # 矩阵运算
import sqlite3      # 数据库

# 连接数据库，获取数据
con = sqlite3.connect("movie.db")
cur = con.cursor()
sql = 'select introduction from movieTop250'
data = cur.execute(sql)
text = ''
for item in data:
    text = text + item[0]
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'.\static\assets\img\tree.jpg')   # 打开图片
img_array = np.array(img)       # 将图片转换成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='C:/Windows/Fonts/msyh.ttc',      # 字体所长位置：C:\Windows\Fonts
    width=800, height=500, random_state=21, max_font_size=110
)   # 生成词云对象，并设置好背景、字体
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')     # 不显示坐标轴

# 保存图片
plt.savefig(r'.\static\assets\img\word.jpg', dpi=500)

# 显示图片
plt.show()

