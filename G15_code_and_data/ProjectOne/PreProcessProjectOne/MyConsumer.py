import gc
import os
import threading
import time
from queue import Queue, Empty
from xml.dom.minidom import parse

from PIL import Image

from myutil.MyDealFile import MyDealFile


class MyConsumer(threading.Thread):
	# private
	__prj_root_path = ""
	__myxml_source_dir = ""
	__myimg_source_dir = ""
	__mystore_img_dir = ""
	__myurlWarehouse = None

	def __init__(self, prj_root_path, myurlWarehouse):
		super(MyConsumer, self).__init__() # 重构run函数必须要写
		#
		self.__prj_root_path = prj_root_path
		self.__myxml_source_dir = prj_root_path + "/tryxml"
		self.__myimg_source_dir = prj_root_path + "/tryimg"
		self.__mystore_img_dir = prj_root_path + "/classifierfolder"
		# url 仓库
		self.__myurlWarehouse = myurlWarehouse

	def run(self):
		# provider
		# 把e:\get_key\目录下的文件名全部获取保存在files中
		try_xml_dir = self.__myxml_source_dir
		try_img_dir = self.__myimg_source_dir
		try_store_img_dir = self.__mystore_img_dir
		files = os.listdir(try_xml_dir)
		#
		#mynodes = self.__myurlWarehouse.get_queue_str_urlToRequest(timeout="1000")
		int_myempty_times = 0
		while True :
			mynodes = self.__myurlWarehouse.get_queue_str_urlToRequest(timeout=2)
			if mynodes == None:
				int_myempty_times = int_myempty_times + 1
				# 如果等待了100次都是空的，那么就当结束了
				if int_myempty_times >= 100:
					print("over")
					return 0
				else:
					if int_myempty_times%10 == 0:
						print("empty times: ", int_myempty_times)
						time.sleep(5)
					continue

			# path \\ name
			str_org_path = mynodes[0]["org_dir_path"] + "/" + mynodes[0]["str_file_name"]
			# path \\ class
			str_trgt_path = try_store_img_dir + "/" + mynodes[0]["str_plant_class"]
			MyDealFile.mymkdir(str_trgt_path)
			'''
			用pillow 读取再存取
			# path \\ class \\ name
			test_im1 = Image.open(str_org_path)
			test_im1.save(str_trgt_path + "\\" + mynodes[0]["str_file_name"], quality = 100)
			test_im1.close()
			'''
			MyDealFile.myCopyFile(str_org_path, str_trgt_path + "/" + mynodes[0]["str_file_name"])
			#
			# 这次能够拿到内容，那么下次empty times 又是从0开始算
			int_myempty_times = 0
			#
			del mynodes, str_org_path, str_trgt_path
			gc.collect()
		return 0
