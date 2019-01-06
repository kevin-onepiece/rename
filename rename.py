import cv2
import os
import io
import sys
# 解决终端输出为乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

names = ["王晨宝.jpg","刘昭阳.jpg","付强.jpg","廖泽铭.jpg","陈先辉.jpg","张跃.jpg","谢凌寅.jpg","赵宇轩.jpg",
"徐文鹏.jpg","钟运幸.jpg","黄晓磊.jpg","张建鹏.jpg","吴金奇.jpg","李辉.jpg","郭添成.jpg","陈文杰.jpg","严嘉城.jpg",
"赵书霖.jpg","谢松.jpg","江展鸿.jpg","叶勇.jpg","李书梁.jpg"]
path = "imgs"
count = 0;
original_imgs = [os.path.join(path,i) for i in os.listdir(path)]
renames = [os.path.join(path,i) for i in names]

for i in original_imgs:
    img = cv2.imread(i)
    # imwrite写入的图片的名字是乱码
    # cv2.imwrite(names[count],img)
    cv2.imencode('.jpg',img)[1].tofile(renames[count])
    print("count is: "+str(count))
    count = count+1
    os.remove(i)
