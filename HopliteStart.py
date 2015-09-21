from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import time

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Samsung'
desired_caps['appPackage'] = 'com.magmafortress.hoplite'
desired_caps['appActivity'] = 'MainActivity'

wd = selenium.webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


time.sleep(5)

try:
    for y in [1257, 1138, 1846, 1367]:
        wd.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 547, "y": y})
        time.sleep(1.5)

finally:
    if not success:
        raise Exception("Test failed.")

time.sleep(6000)
