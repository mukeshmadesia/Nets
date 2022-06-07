# Nets

Allure Rport link - http://192.168.0.44:55433/index.html#packages/8b43f39217f2951f21c3b1bd7a79236d/d2b2d7bdd36b3ce/
TestCase 4 - has ScreenShot - for refernce

SeleniumPython-TestAutomatiom
This project is based on Page Object Model 
            using Selenium Python & Pytest -
            Reporting Used - Allure
            URL Input and Title - Input from json file in Config/data.json
            Test data - Username;password - from txt file - Tests/testData.txt
            
 Structure :
 Nets
      Pages
          BasePage.py - for common function used accross All pages
          LoginPage.py - for LoginPage function - Input Username & password and Click for login
          DashboardPage.py - Next landing page after login - 
      Tests
          conftest.py   - To create fixture for pytest 
          testLoginPage - To Create test case for login Page
          test_base.py  - To create common functions for different pages
          ReadData.py   - To Read URL from Config\data.json
      
      Config
          data.json     - To supply constanst/config data - URL
          
      Allure Reports
          To save Allure reports and Screenshots
          
