from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.management.base import BaseCommand, CommandError
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class RecognizeDigit(APIView):
    def post(self, request):
        try:
            model = keras.models.load_model("./digits.model", compile=True)
            # Modify sent image so it can be evaluated
            img = cv2.imdecode(np.fromstring(
                request.FILES['file'].read(), np.uint8), cv2.IMREAD_GRAYSCALE)
            img = img.reshape(-1, 28, 28)
            prediction = model.predict(img)
            most_likely_result = np.argmax(prediction)
            print(f'Result array: {prediction[0]}', file=sys.stderr)
            print(f'Result: {most_likely_result}', file=sys.stderr)
            return Response(str(most_likely_result), status=200)
        except Exception as e:
            return Response({str(e)}, status=400)
