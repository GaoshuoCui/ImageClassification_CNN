# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pickle
from queue import Queue
from xml.dom.minidom import parse

from PIL import Image

from myutil.MyDealFile import MyDealFile

import time, threading


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def product(name):
    count = 1
    while True:
        #q.put('气球兵{}'.format(count))
        print('{}训练气球兵{}只'.format(name, count))
        count += 1
        time.sleep(5)


def consume(name):
    while True:
        print('{}使用了{}'.format(name, q.get()))
        time.sleep(1)
        #q.task_done()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    path = os.getcwd()
    '''
    

    strTmp = MyDealFile.myReadFile("./try/0.xml")
    ##print(strTmp)

    datasource = open('./try/0.xml')
    dom2 = parse(datasource)
    print(dom2)
    strr = dom2.getElementsByTagName("Content")
    print("value:",strr[0].childNodes[0].nodeValue)
    datasource.close()


    test_im1 = Image.open(r"./try/0.jpg")
    im1 = test_im1.save(r"./try_save/geeks.jpg")


    MyDealFile.mymkdir("./kk")



    q = Queue(maxsize=0)

    t1 = threading.Thread(target=product, args=('wpp',))
    t2 = threading.Thread(target=consume, args=('ypp',))
    t3 = threading.Thread(target=consume, args=('others',))

    t1.start()
    t2.start()
    t3.start()
    '''

    q = Queue(maxsize=200)

    # provider
    # 把e:\get_key\目录下的文件名全部获取保存在files中
    try_xml_dir = path + "/tryxml"
    try_img_dir = path + "/tryimg"
    try_store_img_dir = path + "/classifierfolder"
    files = os.listdir(try_xml_dir)

    for i in range(0,len(files),1):
        # 准确获取一个txt的位置，利用字符串的拼接
        myxmlfile_path = try_xml_dir+"/" + files[i]
        # 把结果保存了在contents中
        datasource = open(myxmlfile_path)
        dom2 = parse(datasource)
        datasource.close()
        #
        #print(dom2)
        strFileNames = dom2.getElementsByTagName("FileName")
        strFileName = strFileNames[0].childNodes[0].nodeValue
        print("value:", strFileName)
        strPlantCles = dom2.getElementsByTagName("Content")
        strPlantCls = strPlantCles[0].childNodes[0].nodeValue
        print("value:", strPlantCls)
        lstTmp = [{"org_dir_path" : try_img_dir ,"str_file_name" : strFileName, "str_plant_class" : strPlantCls}]
        q.put(lstTmp)

    # consumer

    for i in range(0,q.qsize(),1):
        mynodes = q.get(1000)
        # path \\ name
        str_org_path = mynodes[0]["org_dir_path"] + "\\" + mynodes[0]["str_file_name"]
        # path \\ class
        str_trgt_path = try_store_img_dir + "\\" + mynodes[0]["str_plant_class"]
        MyDealFile.mymkdir(str_trgt_path)
        # path \\ class \\ name
        test_im1 = Image.open(str_org_path)
        im1 = test_im1.save(str_trgt_path + "\\" + mynodes[0]["str_file_name"])
        print(q.qsize())

    print(q.qsize())