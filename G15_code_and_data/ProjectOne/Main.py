import datetime

from ImageProcess import *

from TrainCNNModel import *
from EvaluateModel import *
import os
from keras import backend as k
import tensorflow as tf
import time


with tf.device("gpu:0"):

    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))



    # image preprocessing
    train_data_dir = os.getcwd() + '\\data\\traindata'
    test_data_dir = os.getcwd() + '\\data\\testdata'


    train_subdir = os.listdir(train_data_dir)

    for k in train_subdir:
        allfile = os.listdir(train_data_dir + '\\' + k)
        print(len(allfile))
        #fit_size(train_data_dir + '\\' + k, allfile)
        resize_by_ratio(train_data_dir + '\\' + k, allfile)


    test_subdir = os.listdir(test_data_dir)

    for k in test_subdir:
        allfile = os.listdir(test_data_dir + '\\' + k)
        print(len(allfile))
        #fit_size(test_data_dir + '\\' + k, allfile)
        resize_by_ratio(test_data_dir + '\\' + k, allfile)

    #transform image into array and save
    dataset_to_array(train_data_dir,train_subdir,"train")
    dataset_to_array(test_data_dir,test_subdir,"test")

    #load dataset
    X = np.load("train_data.npy")
    Y = np.load("train_label.npy")

    X_test = np.load("test_data.npy")
    Y_test = np.load("test_label.npy")


    class_weight_dict = create_class_weight(Y)
    print("classweight:",class_weight_dict)


    #start = time.process_time()
    #train_fc_weight(X,Y,class_weight)
    cnn_train_model(X,Y,class_weight_dict)
    evaluate_model(X_test,Y_test,'cnn_model.h5')
    #print("training time: %s sec" % time.process_time()-start)


    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


    # release the memory
    k.clear_session()




