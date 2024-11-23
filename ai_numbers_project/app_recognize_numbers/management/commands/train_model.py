import sys
from django.core.management.base import BaseCommand, CommandError
import tensorflow as tf
from tensorflow import keras

class Command(BaseCommand):
    help = "Trains model from scratch"
    # Trains a new model = old model is lost.

    def handle(self, *args, **kwargs):
        try:
            # Handwritten digits (dataset)
            (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

            # Normalize data
            x_train = keras.utils.normalize(x_train, axis=-1)
            x_test = keras.utils.normalize(x_test, axis=-1)

            # Select model
            model = keras.models.Sequential()

            # Flatten converts input into single array. Expected input is 28x28
            model.add(keras.layers.Flatten(input_shape=(28, 28)))
            # Set activation functions
            model.add(keras.layers.Dense(units=128, activation="relu"))
            model.add(keras.layers.Dense(units=10, activation="softmax"))

            # Set optimizer and loss functions
            model.compile(
                optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']
            )

            # Train model
            model.fit(x_train, y_train, epochs=5)

            # Evaluate accuracy
            evaluation = model.evaluate(x_test, y_test, verbose=0)
            print(f'loss: {evaluation[0]}', file=sys.stderr)
            print(f'accuracy: {evaluation[1]}', file=sys.stderr)

            # Save model in .keras format
            model.save('./digits.keras')

        except Exception as e:
            raise CommandError(f'Could not train model. Something went wrong: {str(e)}')
