from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np
import cv2
import sys
import tensorflow as tf
from tensorflow import keras
from PIL import Image


class RecognizeDigit(APIView):
    def post(self, request):
        try:
            model = keras.models.load_model("./digits.model", compile=True)
            read_image = cv2.imdecode(np.fromstring(
                request.FILES['file'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
            save_image = Image.fromarray(read_image)
            save_image.save("digit.png")
            img = cv2.imread("digit.png")[:, :, 0]
            img = img.reshape(-1, 28, 28)
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            most_likely_result = np.argmax(prediction)
            print(f'Result array: {prediction[0]}', file=sys.stderr)
            print(f'Result: {most_likely_result}', file=sys.stderr)
            return Response(str(most_likely_result), status=200)
        except Exception as e:
            return Response({str(e)}, status=400)
