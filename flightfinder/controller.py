from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Controller:
    XPATHS = {
        1: "./div[3]/div[2]/a",
        2: "./div[3]/div[1]/a",
        3: "./div[2]/div[2]/a",
        4: "./div[2]/div[1]/a"
    }
    WEBSITE = "https://www.nexxchange.com/search/teetimes/"

    def __init__(self, locations, slots):
        self.locations = locations
        self.slots = slots
        self.result = {}

    def run(self, date, hour):
        driver = webdriver.Chrome()
        params = "?hour={}&date={}".format(hour, date)

        for location in self.locations:
            link = Controller.WEBSITE + location + params

            driver.get(link)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "teetime-box"))
            )
            teetime_boxes = driver.find_elements(By.CLASS_NAME, "teetime-box")
            for teetime_box in teetime_boxes:
                teetime = teetime_box.find_element(By.XPATH, "./div[1]/div[1]/span").get_attribute("innerHTML")
                courses = teetime_box.find_elements(By.CLASS_NAME, "facet-section")
                for course_box in courses:
                    course = course_box.find_element(By.XPATH, "./div[1]/div[1]").get_attribute("innerHTML")
                    free = course_box.find_element(By.XPATH, Controller.XPATHS[self.slots]).get_attribute("class") \
                           != "show-flight"
                    if free:
                        if location + " " + course not in self.result:
                            self.result[location + " " + course] = []
                        self.result[location + " " + course].append(teetime)
        driver.close()
        return self.result
