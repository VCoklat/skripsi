import matplotlib.pyplot as plt
import numpy as np
import sys
from skimage import data,io,img_as_float,exposure
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist

CLASS1=0
CLASS2=1
Label_kelas = ["benar","salah"]
count_datas = 10 #jumlah gambar per folder
KNN=5

ic = io.ImageCollection('benar/*jpg') #load semua data benar
ic2 = io.ImageCollection('salah/*jpg') #load semua data salah
ic3 = io.imread('test/1.jpg') #image yang di tes


def acquire_image(k,index):
	result = np.empty((0))
	result2 = np.empty((0))
	
	data_per_slice = (count_datas/k)
	begin_datas_slice = index*data_per_slice

	for i in range(begin_datas_slice,begin_datas_slice+data_per_slice):
		result = np.append(result,i)

	for j in range(0,count_datas):
		if j not in result:
			result2 = np.append(result2,j)
	
	# return testing index and training index for k-fold
	return result,result2


def classification(index_testing,index_training):
	distances = []
	distance_i=[]

# calculate all distance
	for j in index_training:
		image_test=extract_feature(ic3)
		image_train=extract_feature(ic[int(j)])
		distance_i.append(distance_formula(image_test,image_train))
		
		# Test class2
		image_test=extract_feature(ic3)
		image_train=extract_feature(ic2[int(j)])
		distance_i.append(distance_formula(image_test,image_train))

	distances.append(distance_i)
	# print distances
	# knn process
	
	predict_true = 0.0

	for idx1,item in enumerate(distances):		
		index_choosen = np.array([])
		for i in range(KNN):
			minimum = sys.maxint
			minimum_index = 0

			for idx,val in enumerate(item):
				if val < minimum and idx not in index_choosen:
					minimum=val
					minimum_index=idx
			
			index_choosen = np.append(index_choosen,minimum_index)

		classified = classified_as(index_choosen)
		print "diklasifikasikan sebagai : "+classified
		
def print_k_nearest(index_choosen,dis):
	string = "\n"
	for i in index_choosen:
		string += Label_kelas[int(i%2)]
		string+="="+str(dis[int(i)])
		
		string+="\n"
	return string

def classified_as(index_choosen): #connectedlabel
	kelas1=0
	kelas2=0
	for i in index_choosen:
		if(i%2==0):
			kelas1=kelas1+1
		else:
			kelas2=kelas2+1

	if kelas1>kelas2:
		return Label_kelas[0]
	elif kelas2>kelas1:
		return Label_kelas[1]
	else:
		return "tidak tahu"


def extract_feature(img):
	image_resized = resize(img, (100, 100), mode='reflect') #resize image
	gray_image = rgb2gray(image_resized) #grayscaling
	equalized_image = equalize_hist(gray_image) #histogramgray
	gray_image[gray_image>0.75]=1.0 #threshold gray 0.75
	return gray_image


def distance_formula(img1,img2):
	distance = np.abs(img1-img2)
	return np.sum(distance)


# K=1
testing,training=acquire_image(10,0)
classification(testing,training)





