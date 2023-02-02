import os
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from keras import regularizers
from keras.layers import Dense, Conv2D, MaxPool2D, AvgPool2D, Dropout, InputLayer, Flatten
import pandas as pd
import pickle



def load_data(filename):
    res = []
    try:
        open_file = open(filename, "rb")
        res = pickle.load(open_file)
        open_file.close()
        return res
    except Exception as err:
        print(err.args)
        return "error"


def save_data(filename, data):
    try:
        file = open(filename, "wb")
        pickle.dump(data, file)
        file.close()
        return True
    except Exception as err:
        print(err.args)
        return False


dictonary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z']

# data extraction from /home/nitay/Documents/sign language interpeter/data for precepti/Gesture Image Data
pass
# data = []
#
# listdir = os.listdir("/home/nitay/Documents/sign language interpeter/data for precepti/Gesture Image Data")
#
# for letter in dictonary:
#     list_sub_dir = os.listdir("/home/nitay/Documents/sign language interpeter/data for precepti/Gesture Image Data/{0}".format(letter))
#     for img in list_sub_dir:
#         data.append([dictonary.index(letter), np.array(Image.open("/home/nitay/Documents/sign language interpeter/data for precepti/Gesture Image Data/{0}/{1}".format(letter, img)).resize((28, 28)).convert("L"))])
#
# data = np.array(data)
# data = data.T
# new_data, new_labels, t = data[1], data[0], []
# for i in new_labels:
#     t.append(i)
# new_labels = np.array(t)
# t = []
# count = 0
# for i in new_data:
#     t.append(i)
#     if count % 100 == 0:
#         print(count)
#     count = count + 1
# new_data = np.array(t)
# save_data("data3.txt", [new_labels, new_data])

new_data = load_data("data3.txt")

new_data, new_labels = np.array(new_data[1]), np.array(new_data[0])
new_data = new_data / 255

train_data, test_data = pd.read_csv("sign_mnist_train.csv"), pd.read_csv("sign_mnist_test.csv")

train_data, test_data = np.array(train_data), np.array(test_data)

data_train, data_test = train_data.T, test_data.T
Y_train, Y_test = data_train[0], data_test[0]
X_train, X_test = data_train[1:], data_test[1:]
X_train, X_test = X_train.T / 255, X_test.T / 255

n_train, m_train = X_train.shape
n_test, m_test = X_test.shape

X_train, X_test = np.reshape(X_train, (-1, 28, 28)), np.reshape(X_test, (-1, 28, 28))

if input("load or create: ") == 'l':
    model = load_data("models/{0}.txt".format(input("model name: ")))
else:
    model = tf.keras.Sequential([
        InputLayer(input_shape=(28, 28, 1)),
        Conv2D(20, kernel_size=(5, 5), padding='same', activation="leaky_relu", kernel_regularizer=regularizers.l2(0.001)),
        MaxPool2D(pool_size=(3, 3), strides=3),
        Flatten(),
        Dense(20, activation="leaky_relu", kernel_regularizer=regularizers.l2(0.001)),
        Dropout(0.5),
        Dense(26, activation="softmax")
    ])

    model.summary()
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['accuracy'])

    model.fit(new_data, new_labels, epochs=5, batch_size=16, callbacks=[tf.keras.callbacks.TensorBoard("logs/new_data")])
#     model.fit(X_train, Y_train, epochs=5, batch_size=16, callbacks=[tf.keras.callbacks.TensorBoard("logs/old_data")])
#
# test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=2)

# print('\nTest accuracy:', test_acc)

if input("save?: ") == 'y':
    save_data("models/{0}.txt".format(input("model name: ")), model)

while True:
    letter = input("input letter: ")
    image = Image.open("examples/{0}.jpg".format(letter)).resize((28, 28)).convert("L")
    image_arr = np.array(image)
    image_arr = image_arr / 255
    prediction = model.__call__(np.array((image_arr,)))

    prediction = dictonary[np.argmax(prediction)]

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Horizontally stacked subplots')
    ax1.imshow(image)
    ax1.set_title("input: " + letter)
    ax2.imshow(Image.open("examples/{0}.jpg".format(prediction)).resize((28, 28)).convert("L"))
    ax2.set_title("output: " + prediction)
    fig.show()
