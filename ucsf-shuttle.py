"""ucsf-shuttle.py
Purpose:
    This script will automatically open chrome and click on the specified route and stop to load bus times.

Usage:
    cd /Users/anguyen11/PycharmProjects/automate/websites
    source env/bin/activate
    python ucsf-shuttle.py

In development:
    ucsf-shuttle.py ROUTE_COLOR SHUTTLE_STOP
    ucsf-shuttle.py (-h | --help)
    ucsf-shuttle.py --version

Options:
    -h --help     Show this screen.
    --version     Show version.

"""
from selenium import webdriver
from docopt import docopt

# def get_times(color, stop):


def get_times():
    route_element = driver.find_element_by_xpath('// *[ @ id = "shuttle-button-off"] / div[1]')
    route_element.click()
    color_element = driver.find_element_by_xpath('// *[ @ id = "myRoutes"] / li[4] / nobr / a')
    color_element.click()
    location_element = driver.find_element_by_xpath('// *[ @ id = "shuttle-location-off"] / div[1] / strong')
    location_element.click()
    ''' can also try explicit wait -> code below execute every 500 ms for 10 s until sucessful or quits after 10 s
    # https://selenium-python.readthedocs.io/waits.html
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    driver = webdriver.Firefox()
    driver.get("http://somedomain/url_that_delays_loading")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()
    '''
    driver.implicitly_wait(2)  # wait 2 seconds
    stop_element = driver.find_element_by_xpath('// *[ @ id = "myLocations1"] / li[2] / nobr / a')
    stop_element.click()
    driver.execute_script("window.scrollTo(0, 500)")  # scroll down 500 pixels


if __name__ == '__main__':
    # arguments = docopt(__doc__, version='ucsf-shuttle 1.0')
    # color = arguments['ROUTE_COLOR']
    # stop = arguments['SHUTTLE_STOP']

    # load chrome
    driver = webdriver.Chrome('./chromedriver')
    # go to url
    driver.get("https://campuslifeservices.ucsf.edu/liveshuttle/")

    get_times()
