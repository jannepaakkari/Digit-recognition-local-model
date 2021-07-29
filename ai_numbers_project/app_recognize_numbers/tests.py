from rest_framework.test import APITestCase


"""
The model should recognize digits from 0-9. Test if that is the case with digits that are NOT from train set.
You can replace images with your own digits if you wish. Remember to change path here accordingly if you change img name/path.
You could loop these tests (in TestModelWithSelfMadeDigits and save space, but then it would not tell explictly how many digits potentially failed
    as the test stops when it is a fail.
"""


class TestModelWithSelfMadeDigits(APITestCase):
    def test_zero(self):
        with open('./app_recognize_numbers/example_digits/zero.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("0"))

    def test_one(self):
        with open('./app_recognize_numbers/example_digits/one.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("1"))

    def test_two(self):
        with open('./app_recognize_numbers/example_digits/two.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("2"))

    def test_three(self):
        with open('./app_recognize_numbers/example_digits/three.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("3"))

    def test_four(self):
        with open('./app_recognize_numbers/example_digits/four.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("4"))

    def test_five(self):
        with open('./app_recognize_numbers/example_digits/five.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("5"))

    def test_six(self):
        with open('./app_recognize_numbers/example_digits/six.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("6"))

    def test_seven(self):
        with open('./app_recognize_numbers/example_digits/seven.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("7"))

    def test_eight(self):
        with open('./app_recognize_numbers/example_digits/eight.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("8"))

    def test_nine(self):
        with open('./app_recognize_numbers/example_digits/nine.png', 'rb') as img:
            response = self.client.post(
                "/api/recognize/digit/", {'image': img})
            self.assertEqual((response.content), str.encode("9"))
