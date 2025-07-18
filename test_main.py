import unittest
from main import get_platform_name

class TestMain(unittest.TestCase):
    def test_platform_name(self):
        self.assertEqual(get_platform_name(), "DevFlix - Plataforma de Video Bajo Demanda")

if __name__ == '__main__':
    unittest.main()
