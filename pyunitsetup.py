import os
from os import environ
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

class PyUnitTestSetup:
    def __init__(self):
        # Get environment variables
        lt_username = environ.get('LT_USERNAME', None)
        lt_access_key = environ.get('LT_ACCESS_KEY', None)

        # Set LambdaTest options
        lt_options = {
            'build': 'Best 13 Python Automation Scripts',
            'project': 'Project: Best 13 Python Automation Scripts',
            'name': 'Test: Best 13 Python AutomationScripts',
            'platform': 'Windows 10',
            'browserName': 'MicrosoftEdge',
            'version': 'latest',
            'visual': True,  # Enable visual testing
            'network': True,  # Enable network capture
            'console': True,  # Enable console logs
            'video': True,  # Enable video recording
            'timezone': 'UTC'  # Set timezone
        }

        # Initialize Edge browser with LambdaTest options
        edge_options = EdgeOptions()
        edge_options.set_capability('LT:Options', lt_options)
        self.driver = webdriver.Remote(
            command_executor=f"https://{lt_username}:{lt_access_key}@hub.lambdatest.com/wd/hub",
            options=edge_options
        )

    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
