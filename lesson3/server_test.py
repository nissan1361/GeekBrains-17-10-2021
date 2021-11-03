import server
import unittest


class TestServer1(unittest.TestCase):
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def test_client1(self):
        r = server.process_client_message(400)
        self.assertEqual(r, 400)


if __name__ == '__main__':
    unittest.main()
