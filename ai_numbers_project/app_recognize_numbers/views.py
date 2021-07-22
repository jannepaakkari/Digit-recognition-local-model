from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


'''
Work in progress. 
- Slightly experimental still
- TestView(APIView) for example retrains model each times it is called which is not probably a good practise.
'''


class TestView(APIView):
    def post(self, request):
        # Handwritten digits (dataset)
        (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

        # Normalize data
        x_train = keras.utils.normalize(x_train, axis=-1)
        x_test = keras.utils.normalize(x_test, axis=-1)

        '''
        # Alternative way to normalize - seems cause massive amounts of loss, so probably something wrong
        x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
        '''

        # Select model
        model = keras.models.Sequential()

        # Flatten converts input into single array. Expected input is 28x28
        model.add(keras.layers.Flatten(input_shape=(28, 28)))
        # Set activation functions
        model.add(keras.layers.Dense(units=128, activation="relu"))
        model.add(keras.layers.Dense(units=10, activation="softmax"))

        # Set optimizer and loss functions
        model.compile(
            optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # Train model
        model.fit(x_train, y_train, epochs=5)

        # Evaluate accuracy
        evaluation = model.evaluate(x_test, y_test, verbose=0)
        print(f'loss: {evaluation[0]}', file=sys.stderr)
        print(f'accuracy: {evaluation[1]}', file=sys.stderr)

        # Save model
        model.save('digits.model')

        # Modify sent file (image) so it can be evaluated
        img = cv2.imdecode(np.fromstring(
            request.FILES['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)

        img = img.reshape(-1, 28, 28)
        #img = cv2.resize(img, (28, 28))
        #img = np.invert(img)

        # Make prediction
        prediction = model.predict(img)
        most_likely_result = np.argmax(prediction)

        print(f'Result array: {prediction[0]}', file=sys.stderr)
        print(f'Result: {most_likely_result}', file=sys.stderr)

        return Response(str(most_likely_result), status=200)
