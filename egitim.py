import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras import optimizers
from keras.applications.vgg19 import VGG19
from keras.models import load_model, Model
import cv2

girisverisi = np.load("/content/drive/My Drive/App/metalslug-500screen.npy")
girisverisi = girisverisi.reshape(500,224,224,3)
cikisverisi = np.load("/content/drive/My Drive/App/metalslug-500key.npy")
cikisverisi = cikisverisi.reshape(500,24)
girisverisi = girisverisi/255

temelmodel = VGG19(weights='imagenet', include_top=False)
x = temelmodel.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
tahmin = Dense(24, activation='softmax')(x)

# this is the model we will train
model = Model(inputs=temelmodel.input, outputs=tahmin)

for katman in temelmodel.layers:
    katman.trainable = False

temelmodel.summary()

model.compile(loss="categorical_crossentropy", optimizer=optimizers.RMSprop(lr=0.001), metrics=["accuracy"])

model.fit(girisverisi, cikisverisi, batch_size=1, epochs=200)

model.save('metalslugFuning')
