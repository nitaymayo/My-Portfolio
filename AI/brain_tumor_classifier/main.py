# Data from the "brain tumor image dataset" at https://www.kaggle.com/datasets/denizkavi1/brain-tumor

import pickle
from PIL import Image
import numpy
import tensorflow as tf
import pathlib
import numpy as np
from keras.layers import BatchNormalization, Dropout, InputLayer, Conv2D, MaxPool2D, AvgPool2D, Flatten, Dense
import matplotlib.pyplot as plt
from plot_keras_history import show_history, plot_history
import random


dictionary = ["meningioma", "glioma", "pituitary tumor"]

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

dataset_url = '/home/nitay/Pictures/brain tumor/brain tumor train'
data_dir = pathlib.Path(dataset_url)

batch_size = 16
epochs = 10
img_height = 180
img_width = 180

train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="both",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

dataset_url = '/home/nitay/Pictures/brain tumor/brain tumor test'
data_dir = pathlib.Path(dataset_url)

test_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)


def get_folder(dataset):
    plt.figure(figsize=(20, 5))
    for i in range(3):
        image_path = random.choice(dataset.file_paths)
        img = Image.open(image_path).resize((img_height, img_width))
        ax = plt.subplot(1, 3, i+1)
        plt.imshow(img)
    plt.show()


# get_folder(train_ds)
# get_folder(val_ds)

model = tf.keras.Sequential([
    InputLayer((img_height, img_width, 3)),
    Conv2D(128, 3, activation='relu', padding='same'),
    Conv2D(128, 3, activation='relu', padding='same'),
    MaxPool2D(),
    Conv2D(64, 3, activation='relu', padding='same'),
    Conv2D(64, 3, activation='relu', padding='same'),
    Conv2D(64, 3, activation='relu', padding='same'),
    Dropout(0.3),
    MaxPool2D(),
    Conv2D(32, 3, activation='relu', padding='same'),
    Conv2D(32, 3, activation='relu', padding='same'),
    Conv2D(32, 3, activation='relu', padding='same'),
    AvgPool2D(),
    MaxPool2D(),
    Conv2D(16, 3, activation='relu', padding='same'),
    Conv2D(16, 3, activation='relu', padding='same'),
    MaxPool2D(),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])
model.summary()
model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    metrics=['accuracy'])

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    batch_size=batch_size
)

test_loss, test_acc = model.evaluate(test_ds, verbose=2)

print('\nTest accuracy:', test_acc)

show_history(history)
plot_history(history, path="standard.png")
plt.close()


if input("self evaluate?: ") == 'y':
    while True:
        predictions = []
        plt.figure(figsize=(20, 5))
        for i in range(3):
            image_path = random.choice(test_ds.file_paths)
            img = Image.open(image_path).resize((img_height, img_width)).convert('RGB')
            predictions[i] = numpy.argmax(model.__call__(np.array(img)))
            ax = plt.subplot(1, 3, i + 1)
            ax.title.set_text("image predicted as " + dictionary[int(predictions[i]) - 1])
            plt.imshow(img)
        plt.show()
        input("try again?")
