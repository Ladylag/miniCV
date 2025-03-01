import unittest
import subprocess
import time

class TestGreenSquareApp(unittest.TestCase):
    def test_auto_close(self):
        # Launch the application and check if it closes after 5 seconds
        start_time = time.time()
        process = subprocess.Popen(['python', 'green_square_app.py'])
        process.wait()
        end_time = time.time()
        self.assertTrue(4.5 <= end_time - start_time <= 5.5, "The application did not close after 5 seconds")

    def test_stay_open(self):
        # Launch the application with the special parameter and check if it stays open
        process = subprocess.Popen(['python', 'green_square_app.py', '--stay-open'])
        time.sleep(6)  # Wait for more than 5 seconds
        self.assertIsNone(process.poll(), "The application closed unexpectedly")
        process.terminate()  # Clean up

if __name__ == '__main__':
    unittest.main() 