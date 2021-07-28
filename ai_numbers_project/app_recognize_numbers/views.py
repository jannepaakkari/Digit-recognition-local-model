from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from . import serializers


class RecognizeDigit(APIView):
    def post(self, request):
        try:
            serializer = serializers.ImageSerializer(
                data=request.data)
            if serializer.is_valid(raise_exception=True):
                # Load model
                model = keras.models.load_model("./digits.model", compile=True)
                # Save image if it is valid
                serializer.save()
                # Read image and predict result
                img = cv2.imread(serializer.data['image'].strip("/"))[:, :, 0]
                img = np.invert(np.array([img]))
                prediction = model.predict(img)
                most_likely_result = np.argmax(prediction)
                return Response(str(most_likely_result), status=200)
        except Exception as e:
            return Response({str(e)}, status=400)
