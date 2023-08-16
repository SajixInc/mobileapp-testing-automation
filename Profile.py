import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pymongo import MongoClient
import pymongo


@pytest.fixture(scope='function')
def driver(request):
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.platformVersion = '9'
    options.device_name = 'DUK-AL20'
    options.automation_name = 'Appium'
    options.app_activity = 'MainActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    return driver

def test_add_profile(driver):
    driver.find_element('xpath', '//android.widget.TextView[@index="2"]').click()
    driver.implicitly_wait(30)

    driver.find_element('xpath', '//android.widget.Button[@bounds="[0,136][154,494]"]').click()
    driver.find_element('xpath', '//android.view.View[@content-desc="Profile"]').click()

    driver.find_element('xpath', '//android.widget.EditText[@index="6"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//android.widget.EditText[@index="6"]').send_keys('Rathnam')
    time.sleep(2)
    for i in range(2):
        driver.swipe(106, 1706, 980, 750, 100)
        time.sleep(2)

    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[2]').click()
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[2]').send_keys('Jaggayyapeta')

    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.Button[2]').click()

    driver.find_element('xpath', '//android.widget.Button[@bounds="[829,641][961,773]"]').click()
    driver.find_element('xpath', '//android.widget.EditText[@index="1"]').click()
    driver.find_element('xpath', '//android.widget.EditText[@index="1"]').clear()
    driver.find_element('xpath', '//android.widget.EditText[@index="1"]').send_keys('08/18/1995')
    driver.find_element('xpath', '//android.widget.Button[@content-desc="OK"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//android.widget.RadioButton[@index="11"]').click()
    driver.find_element('xpath','//android.widget.EditText[@index="13"]').click()
    driver.find_element('xpath','//android.widget.EditText[@index="13"]').send_keys('abc@gmail.com')
    number="YOUR_PHONE_NUMBER"
    driver.find_element('xpath','//android.widget.EditText[@index="14"]').click()
    driver.find_element('xpath','//android.widget.EditText[@index="14"]').send_keys(number)
    for i in range(3):
        driver.swipe(148, 2072, 906, 582, 100)
        time.sleep(2)
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[3]').click()
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[3]').send_keys('Onetowne')
    time.sleep(2)
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[4]').click()
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[4]').send_keys('Vijayawada')
    time.sleep(2)
    driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                'android.widget.EditText[5]').click()
    driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                'android.widget.EditText[5]').send_keys('Andhrapradesh')
    time.sleep(2)
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/'
                                 'android.widget.ScrollView/android.widget.EditText[6]').click()
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/'
                                 'android.widget.ScrollView/android.widget.EditText[6]').send_keys('520001')
    for i in range(2):
        driver.swipe(143, 622, 373, 337, 80)
        time.sleep(2)
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[6]').click()
    driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                                 'android.widget.EditText[6]').send_keys('Your_descreption')

    driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/'
                        'android.widget.ScrollView/android.widget.EditText[7]').click()
    driver.find_element('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/'
                        'android.widget.EditText[7]').send_keys('Indian')
    for i in range(2):
        driver.swipe(143, 622, 373, 337, 80)
        time.sleep(2)
    driver.find_element('xpath', '//android.view.View[@content-desc="Save & Next"]').click()
    # driver.quit()
    client = MongoClient(host='your_host', port='your_port', username='your_username', password='your_password',
                         authSource='your_authsource')
    mydb = client['your_db']
    collection = mydb["your_collection"]
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
    print(mobile(number))

    assert driver.current_activity == ".MainActivity"
    driver.quit()
    client.close()
