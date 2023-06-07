 
 <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/lifeeazy-logo1.png" align="right" width="250"/> <img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/Appium.png" width="250"/> 

 
 
 <h1 font-size="50px" align="center">Mobile App Automation Testing Via Appium With Python</h1>


Appium is an open-source mobile application testing framework that allows you to automate testing of native, hybrid, and mobile web applications across various platforms, such as iOS and Android. It provides a cross-platform solution for automating mobile app testing, enabling you to write tests using familiar programming languages like Java, C#, Python, Ruby, and JavaScript.
- It is developed and supported by Sauce Labs and has great community support.
- Appium is cross-platform as it allows the same API which works for different mobile operating systems.
- Appium Testing is flexible, you can use the same code ios that you have written for Android.
- One of the key features of Appium is its ability to automate tests using the WebDriver protocol, which allows you to interact with mobile apps in a similar way to how you would interact with a web page in a browser. This means you can perform actions like tapping buttons, entering text, swiping, and validating UI elements within your tests.

# Features:

  - Multi-language support
  - Simplicity and ease of use
  - Real device and emulator/simulator support
  - Support for gestures and touch events
  - Integration with testing frameworks
  - It supports both Android and iOS

# Installation:

1.	Install Python
 - To install click on this link [Click](https://www.python.org/downloads/)
 - Download the latest version for windows

2.	Install Pycharm Community Edition
 - To install click on this link [Click](https://www.jetbrains.com/pycharm/download/#section=windows)

3.	Install Node JS
 - To install click on this link [Click](https://nodejs.org/en/)

4. Install Appium Server through Command

     
    ``pip install Appium-Python-Client``


5. Install Appium inspector
 - To install click on this link [Click](https://github.com/appium/appium-desktop/releases/tag/v1.21.0)

 - Download the latest version for windows

 - First we have to open Appium then click on start server 

 - After that click on inspector, it will direct to github page in that page we have to click on "Releases in installation option"

 - In “assets” choose the option which we want

 - It will download .exe file , we need to install it


6. Install Android Studio or MEmu Play (for Emulator purpose)

 - Android Studio Download link [Click](https://developer.android.com/studio )
 - MEmu Play Download link [Click](https://www.memuplay.com/)


7.	Create a Virtual Device for Android Studio

 - Select pixel device from the phone
 - Download the Android version
 - Launch the emulator


# How To Setup Appium:
<strong>Appium Desktop :</strong> It comes in two packages

    1. Appium Desktop (Server)

    2. Appium Inspector

 - Start Appium Server

 - Launch the Appium Desktop then give the Host & Port and then start the server.
example:

        Host : localhost
        Port : 4723
        
  
   
- By default it will run on localhost:4723. This example will consider the default.

![Screenshot 2023-06-06 115325](https://github.com/vivifyhealthcare/mobileapp-testing-automation/assets/128147303/2df838bd-48e0-43e8-96f9-0a1602ddd211)

- After download Appium Inspector, Complete the installation process then Open the Appium inspector

- In Appium Server and Appium Inspector "Host and Remote Host" are needs to be same

- In Appium Server and Appium Inspector "Port and Remote Port" are needs to be same

        Remote path - /wd/hud
  
   ![image (3)](https://github.com/vivifyhealthcare/mobileapp-testing-automation/assets/128147303/4deba379-7f17-4976-8d5f-799a06db709d)

- With Appium 2.0, you should also ensure you’re sending W3C standard capabilities within your test code such as the following
 capabilities:

        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platformVersion = '7.1.2'
        options.device_name = 'google G011A'
        options.automation_name = 'Appium'
        options.app_activity ='MainActivity'


- Create new python project in Pycharm

- Set the Interpreter and add the Appium dependency for the project

- Open Settings and Click on Project Interpreter,
   Click ‘+‘ and then search for Appium in Available Packages dialog box.

- Select Appium-Python-Client and click Install Package to install Appium Python Client.

# Appium Test Execution:
- Download APK file 
- Now drag and drop the APK file into the  Emulator
- Start Appium Server
- Run your filename.py 

# Example Test:
   - <strong>App</strong> : Flipkart
 
   - <strong>Description</strong> : Hear we are testing the flipkart app via Appium with Python and we are getting the laptop price in the console window
- First you need to create a .py file in that you have to write your code.
- <h4>Example Code :</h4>

        from appium import webdriver
        from appium.options.android import UiAutomator2Options

        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platformVersion = '7.1.2'
        options.device_name = 'google G011A'
        options.automation_name = 'Appium'
        options.app_activity = 'MainActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

        driver.find_element('xpath','//android.widget.TextView[@index="9"]').click()
        driver.implicitly_wait(50)

        # search lenovo laptops
        driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/'
                                'android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView').click()
        driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/'
                                'android.view.ViewGroup[1]/android.widget.EditText').send_keys('lenovo laptops')
        driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/'
                                'android.view.ViewGroup/android.view.ViewGroup[1]').click()

        price = driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/'
                                'android.view.ViewGroup/android.widget.TextView[4]').get_attribute("text")

        assert price == "₹33,990","Price not same"

        print("Laptop price = " + price)


# Result:


<img src = "https://github.com/vivifyhealthcare/mobileapp-testing-automation/assets/128147303/00e69104-ac18-475e-b5f1-6d2cbe68c03c">



<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>

