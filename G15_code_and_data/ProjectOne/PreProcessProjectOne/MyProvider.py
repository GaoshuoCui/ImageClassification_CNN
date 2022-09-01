import gc
import os
import threading
import time
from queue import Queue
from xml.dom.minidom import parse


class MyProvider(threading.Thread):
	# private
	__prj_root_path = ""
	__myxml_source_dir = ""
	__myimg_source_dir = ""
	__mystore_img_dir = ""
	__myurlWarehouse = None

	def __init__(self, prj_root_path, myurlWarehouse):
		super(MyProvider, self).__init__() # 重构run函数必须要写
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
		print(len(files))

		for i in range(0, len(files), 1):
			# 准确获取一个txt的位置，利用字符串的拼接
			myxmlfile_path = try_xml_dir + "/" + files[i]
			# 把结果保存了在contents中
			datasource = open(myxmlfile_path)
			dom2 = parse(datasource)
			datasource.close()
			#
			# print(dom2)
			strFileNames = dom2.getElementsByTagName("FileName")
			strFileName = strFileNames[0].childNodes[0].nodeValue
			print("value:", strFileName)
			strPlantCles = dom2.getElementsByTagName("Content")
			strPlantCls = strPlantCles[0].childNodes[0].nodeValue
			print("value:", strPlantCls)
			lstTmp = [{"org_dir_path": try_img_dir, "str_file_name": strFileName, "str_plant_class": strPlantCls}]
			# 地址放入仓库
			#print("in")
			self.__myurlWarehouse.add_queue_str_urlToRequest(lstTmp,timeout=100)
			print(myxmlfile_path)
			time.sleep(0.05)
			#print("out")
			del dom2, datasource, strFileNames, strFileName, strPlantCles, strPlantCls,lstTmp
			gc.collect()
		#
		return 0
