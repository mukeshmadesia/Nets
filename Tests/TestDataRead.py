from pathlib import Path
import os
import pytest


class TestDataRead:
    @pytest.mark.skip    # Otherwise, pytest will consider it as Testcase
    def test_data_read(self):
        path = '../Tests/testData.txt'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("testData.txt", "r")
        data = f.read(100)

        test_username = data.split(";")[0]
        test_password = data.split(";")[1]

        f.close()
        return test_username, test_password

    @pytest.mark.skip           # Otherwise, pytest will consider it as Testcase
    def test_data_write(self, outdata):
        path = '../Tests/outData.txt'

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        # home_path = Path('../Config')

        f = open("outData.txt", "w")
        data = f.write("name:" + outdata)
        f.close()
