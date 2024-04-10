from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Controller:
    WEBSITE = "https://www.nexxchange.com/search/teetimes/"

    def __init__(self, locations, slots, driver_file):
        self.locations = locations
        self.slots = slots
        self.driver_file = driver_file
        self.result = {}

    def run(self, date, hour_from, hour_to):
        driver = webdriver.Chrome(self.driver_file)
        params = "?hour={}&date={}".format(hour_from, date)

        for location in self.locations:
            link = Controller.WEBSITE + location + params

            driver.get(link)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "teetime-box"))
            )
            teetime_boxes = driver.find_elements(By.CLASS_NAME, "teetime-box")
            for teetime_box in teetime_boxes:
                teetime = teetime_box.find_element(By.XPATH, "./div[1]/div[1]/span").get_attribute("innerHTML")
                if int(teetime.split(":")[0]) >= hour_to:
                    break
                courses = teetime_box.find_elements(By.CLASS_NAME, "facet-section")
                for course_box in courses:
                    course = course_box.find_element(By.XPATH, "./div[1]/div[1]").get_attribute("innerHTML")
                    flight_spots = course_box.find_elements(By.XPATH, "./div[position()>1]/div/a[@class='player-box none']")

                    if len(flight_spots) >= self.slots:
                        if location + " " + course not in self.result:
                            self.result[location + " " + course] = []
                        self.result[location + " " + course].append(teetime)
        driver.close()
        return self.result