from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from PIL import Image as PILImage
import numpy as np
import keras

class RecognizeDigit(APIView):
    def post(self, request):
        try:
            serializer = serializers.ImageSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                # Load model
                model = keras.models.load_model("./digits.keras", compile=True)

                # Process image (without saving it)
                image = serializer.validated_data['image']
                
                # Open the image in memory (without saving it to disk)
                img = PILImage.open(image)

                # Convert to grayscale and scale to 28x28 (actually resizing is no-op as we require 28x28, but this is alternative approach)
                img = img.convert('L')
                #img = img.resize((28, 28))
                
                # Reshape image for the model 
                img_array = np.array(img) # to numpy array
                img_array = img_array / 255.0  # Normalize the image
                img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
                img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

                # Make prediction
                prediction = model.predict(img_array)
                most_likely_result = np.argmax(prediction)

                return Response({"result": most_likely_result}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=400)
