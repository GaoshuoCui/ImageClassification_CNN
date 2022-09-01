# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pickle
from queue import Queue
from xml.dom.minidom import parse

from PIL import Image

from MyConsumer import MyConsumer
from MyProvider import MyProvider
from MyUrlWarehouse import MyUrlWarehouse
from myutil.MyDealFile import MyDealFile

import time, threading


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    path = os.getcwd()
    #
    myUrlWarehouse1 = MyUrlWarehouse()
    #
    provider1 = MyProvider(path,myUrlWarehouse1)
    consumer1 = MyConsumer(path,myUrlWarehouse1)
    consumer2 = MyConsumer(path, myUrlWarehouse1)

    provider1.start()
    time.sleep(2)
    consumer1.start()
    consumer2.start()


