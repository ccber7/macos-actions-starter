import platform
import sys
import unittest


class TestMacOSEnvironment(unittest.TestCase):
    def test_python_version(self):
        """Pastikan Python berjalan minimal versi 3.11+."""
        print(f"Running on Python {sys.version}")
        self.assertGreaterEqual(sys.version_info[:2], (3, 11))

    def test_platform_info(self):
        """Cetak informasi OS tempat pengujian dijalankan."""
        os_name = platform.system()
        arch = platform.machine()
        print(f"Detected OS: {os_name} ({arch})")
        self.assertIn(os_name, ["Darwin", "Linux", "Windows"])


if __name__ == "__main__":
    unittest.main()
