import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\rhari\\OneDrive\\DOM\\project_1\\login_data.csv")  # Update the path
    driver.maximize_window()
    driver.get("https://orangehrm.com/")  # Replace with the actual OrangeHRM URL
    request.cls.driver = driver
    yield
    driver.quit()
