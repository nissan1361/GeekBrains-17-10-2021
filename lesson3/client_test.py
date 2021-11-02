import client
import unittest


class TestCreatePres(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_client1(self):
        r = client.create_pres()
        self.assertEqual(r,{1: [1, 2, 3], 2: 255, 3: '1024абвгд'})

    def test_answers(self):
        r = client.create_pres(400)
        self.assertEqual(r, 400)


if __name__ == '__main__':
    unittest.main()

