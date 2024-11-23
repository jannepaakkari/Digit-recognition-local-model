from rest_framework.test import APITestCase

class TestModelWithSelfMadeDigits(APITestCase):
    def test_digits(self):
        digits = [
            ('zero.png', 0),
            ('one.png', 1),
            ('two.png', 2),
            ('three.png', 3),
            ('four.png', 4),
            ('five.png', 5),
            ('six.png', 6),
            ('seven.png', 7),
            ('eight.png', 8),
            ('nine.png', 9),
        ]
        
        for img_name, expected_result in digits:
            with open(f'./app_recognize_numbers/example_digits/{img_name}', 'rb') as img:
                response = self.client.post(
                    "/api/recognize/digit/", {'image': img}, format='multipart'
                )
                self.assertEqual(response.data, {"result": expected_result})