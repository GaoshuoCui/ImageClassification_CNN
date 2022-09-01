README for G15

####################### data #######################
the classified raw data could be download from the 
url: https://drive.google.com/file/d/17mOiINbOQy2pAYGrbNKz2OgvzZn-nZD6/view?usp=sharing

because the data is too large to submit in moodel
please extract the zip and move the whole folder(including the parent fold "data") under the project folder "ProjectOne"
####################### requirements #######################
if you use GPU training with 20 epoch settings:
* Training takes ~4 hours

if you use CPU training with 20 epoch settings:
* Training takes ~8 hours
############################################################
####################### steps to run #######################
Tips:
	because the data given has been classified by our team, 
	you needn't run ./PreProcessProjectOne/TestMain.py to classfied again
############################################################
you are just required to run in the following order:
step1:
	run Main.py would start training the model
		result:
		1. the model would be save in file "cnn_model.h5"
		2. the loss and accuracy result would be plot in the figure, 
		   it is saved in "acc_loss_plot.png" 

step2:
	if you want to use the model to predict the single picture, 
	you can input as following in the terminal, for example: 

		1. if the picture you want to use is named "mytt_pic1.jpg",
		 	please place it under the fold "ProjectOne"

		2. enter the line in the terminal as the following: 
			python PredictImage.py --model  cnn_model.h5  --labelbin  lb.pickle  --image  ./mytt_pic1.jpg

########### you can change these variables to tune ###########
in the script of ./TrainCNNModel.py:

you can change the epoch, which has been initialized in the front of this script:
epochs = 20

you can change the K-fold, which has been initialized in the front of this script
split_num = 5
##############################################################
####################### file structure #######################
./PreProcessProjectOne/TestMain.py   	<--script to classfied the raw train data and test data
./Main.py   			     	<--script to run baseline
./PredictImage.py		     	<--script to predict the single image


./TrainCNNModel.py		     	<--function about train the data
./PredictImage.py		     	<--function about to predict the single image
./EvaluateModel.py		     	<--function about evaluate the test data
./ImageProcess.py              	     	<--function about prepocess the image

./cnn_model.h5              	     	<-- trained model
./lb.pickle			     	<-- lable binarizerred
./acc_loss_plot.png			<-- result plot figure

./data/traindata/*			<-- classified train data
./data/testdata/*			<-- classified test data
