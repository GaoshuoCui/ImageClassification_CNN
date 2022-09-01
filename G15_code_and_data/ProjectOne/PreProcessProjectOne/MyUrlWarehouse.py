import threading
from queue import Queue, Empty


class MyUrlWarehouse:
	# semaphore
	__smp1_queue_str_urlToRequest = threading.Semaphore(1)	#添加一个计数器
	__smp1_set_str_urlToRequest = threading.Semaphore(1)  # 添加一个计数器
	#
	__queue_str_urlToRequest = Queue(maxsize=2000)
	set_str_urlToRequest = set()

	def add_queue_str_urlToRequest(self, str, **kargs):
		if self.__queue_str_urlToRequest.qsize() % 100 == 0:
			print("url num: ", self.__queue_str_urlToRequest.qsize())
		#print("put in")
		self.__smp1_queue_str_urlToRequest.acquire()	#计数器获得锁
		#
		self.__queue_str_urlToRequest.put(str,timeout=kargs["timeout"])
		#
		self.__smp1_queue_str_urlToRequest.release()	#计数器释放锁
		#print("put out")

	# python 的get 包括了 弹出
	def get_queue_str_urlToRequest(self, **kargs):
		#print("get in")
		str_rs = ""
		self.__smp1_queue_str_urlToRequest.acquire()	#计数器获得锁
		#
		#print(kargs["timeout"])
		#str_rs = self.__queue_str_urlToRequest.get(timeout=kargs["timeout"])
		try:
			#str_rs = self.__queue_str_urlToRequest.get(timeout=kargs["timeout"])
			#str_rs = self.__queue_str_urlToRequest.get(timeout=kargs["timeout"])
			str_rs = self.__queue_str_urlToRequest.get_nowait()
			if str_rs == None:
				self.__smp1_queue_str_urlToRequest.release()
				return None
		except Empty:
			self.__smp1_queue_str_urlToRequest.release()
			return None
		#
		self.__smp1_queue_str_urlToRequest.release()	#计数器释放锁
		#
		#print("put out")
		return str_rs
