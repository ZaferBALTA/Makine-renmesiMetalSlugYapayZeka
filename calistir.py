from keras.models import Model
from keras.applications.vgg19 import VGG19
from keras.layers import GlobalAveragePooling2D, Dense
from keras import optimizers

def dene(resim):
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

    model.load_weights('metalslugFuning')
    resim = resim.reshape(1, 224, 224, 3)
    print(model.predict(resim))
    return model.predict(resim)
