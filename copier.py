import shutil

for i in range(100):
    shutil.copy2('D:/Img/annotation.xml', 'D:/copies/annotation{}.xml'.format(i))
    shutil.copy2('D:/Img/annotation.jpg', 'D:/copies/annotation{}.jpg'.format(i))
    shutil.copy2('D:/Img/annotation1.xml', 'D:/copies/annotation1{}.xml'.format(i))
    shutil.copy2('D:/Img/annotation1.jpg', 'D:/copies/annotation1{}.jpg'.format(i))
    shutil.copy2('D:/Img/annotation2.xml', 'D:/copies/annotation2{}.xml'.format(i))
    shutil.copy2('D:/Img/annotation2.jpg', 'D:/copies/annotation2{}.jpg'.format(i))
    shutil.copy2('D:/Img/annotation3.xml', 'D:/copies/annotation3{}.xml'.format(i))
    shutil.copy2('D:/Img/annotation3.jpg', 'D:/copies/annotation3{}.jpg'.format(i))

