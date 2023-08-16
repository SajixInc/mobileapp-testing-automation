 
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

![Screenshot 2023-06-06 115325](https://vivifyassets.s3.ap-south-1.amazonaws.com/Appium_Server.png)

- After download Appium Inspector, Complete the installation process then Open the Appium inspector

- In Appium Server and Appium Inspector "Host and Remote Host" are needs to be same

- In Appium Server and Appium Inspector "Port and Remote Port" are needs to be same

        Remote path - /wd/hud
  
   ![image (3)](https://vivifyassets.s3.ap-south-1.amazonaws.com/Appium-Inspector.png)

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


<img src = "https://vivifyassets.s3.ap-south-1.amazonaws.com/Appium_Results.png"><br><br><br>








# Appium Report in HTML and MongoDB Connection

Appium can support to generate report by using pytest framework. This framework libraries provide how to generate detailed and organized report for test runs.

# Advantages

* By integrating HTML reporting libraries into your Python-based Appium tests, you can generate detailed and visually appealing test reports.
* HTML reports can be easily shared among team members and stakeholders.
* HTML reports can help in debugging test failures by providing detailed information about the test environment, steps executed, and any error messages encountered. This aids in quicker issue identification and resolution.
* HTML reports present test results in a human-readable format, making it simpler for both technical and non-technical team members to understand the outcomes of the tests.


# To generate an Appium HTML Report using python

# Prerequisites:

* Install Appium, Python and MongoDB on your system
* Install necessary packages

        pip install pytest
        pip install pytest-reporter-html1
        pip install pymongo


# Python environment setup:
* Create an virtual environment on Windows :

        python -m venv your_environment_name

* Activate the virtual environment :

        your_environment_name\Scripts\activate

# Configure the mongoDB Connection:

* Create New Connection and then give your mongoDB URI.
* Click on Advanced connection option and then click onAuthentication option.
* Inside Authentication, give your **Username** , **Password** and then click on Connect .

# Example Code:
* In Pycharm you need to import MongoClient 

* Establishing a connection to the MongoDB server:

        client = MongoClient(host='your_host', port=your_port, username='your_user_name', password='your_password', authSource='your_authsource')

* Accessing the database and collection:

        mydb = client['database_name']
        collection = mydb["collection_name"]

* The script selects the database named 'database_name' and the collection named 'collection_name' within that database.        

* Defining the mobile function:

        def mobile(PhoneNumber):
        lis = []
        print(lis)
        query = {"PhoneNumber": PhoneNumber}
        results = collection.find(query)
        for doc in results:
                b = doc['PhoneNumber']
                lis.append(b)
        if PhoneNumber in lis:
                print("Data was successfully found in MongoDB.")
        else:
                print("No data was found in MongoDB.")
        return lis

* The mobile function takes a PhoneNumber as an argument. Inside the function:

* An empty list 'lis' is initialized.
* A query dictionary query is created with the key "PhoneNumber" and the provided PhoneNumber as the value.
* The collection.find(query) function is used to search for documents in the collection that match the query.
* The loop iterates through the results and appends the "PhoneNumber" field of each document to the 'lis' list.
* It then checks if the provided PhoneNumber is in the 'lis' list. If it is, a success message is printed; otherwise, a failure message is printed.

* Calling the mobile function and printing the results:

        print(mobile(number))

* The mobile function is called with the argument number, and the result is printed. 

# Usage:
* Specify the html1 template and the output path of the report

* If You want to change report name "report.html" to "example_test.html" 

* To run the folling command in Terminal:

        pytest --template=html1/index.html --report=report.html  

# Result:

<img src= "https://vivifyassets.s3.ap-south-1.amazonaws.com/image+(3).png" width="500">


<img src= "https://vivifyassets.s3.ap-south-1.amazonaws.com/image+(2).png" width="500">

<p align="center">
<img src="https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png" margin_left="100"/>
</p>



