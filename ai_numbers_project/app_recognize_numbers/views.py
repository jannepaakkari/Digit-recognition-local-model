from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from . import serializers
import os

class RecognizeDigit(APIView):
    def post(self, request):
        try:
            serializer = serializers.ImageSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                # Load model
                model = keras.models.load_model("./digits.keras", compile=True)

                # Save image if it is valid
                serializer.save()

                # Read image and predict result
                image_path = serializer.data['image'].strip("/")
                image = Image.open(image_path).convert("L")

                # Resize the image to 28x28
                image = image.resize((28, 28))
                img_array = np.array(image)

                # Normalize the image
                img_array = img_array / 255.0

                # Reshape image for the model (add a batch dimension)
                img_array = np.expand_dims(img_array, axis=-1)
                img_array = np.expand_dims(img_array, axis=0)

                # Predict result
                prediction = model.predict(img_array)
                most_likely_result = np.argmax(prediction)

                return Response({"result": most_likely_result}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=400)
