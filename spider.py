from bs4 import BeautifulSoup
import re
from CalendarDate import CalendarDate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# convert raw calendar_data to the list
# in the form of tuple (date, event)
#
# @param: data_set A set that contain raw calendar tags
# @return: A list that contains tuple (date,event)
def analyze_calendar_data(data_set):
    data_list = list()
    i = 0
    while i < len(data_set):
        # parse the date into CalendarDate
        data_list.append((data_set[i].string, data_set[i + 1].string))
        i += 2
    return data_list


# convert a  date string list into CalendarDate
#
# @param date_split is a part of raw date string eg. March 10, 2019
# @return CalendarDate that represents this input date
#
def convert_calendar_date(date_split):
    year = date_split[2]
    month = date_split[0]
    day = date_split[1][:-1]
    return CalendarDate(year, month, day)


#
# process tuition time from extract date
#
# @param data_list, raw calendar data extracted from HTML5
# @return a list that contain tuple (event, date)
def analyze_tuition_time(data_list):
    tuition_date_list = []
    pattern = re.compile(r'.*?tuition.*?', re.I)
    for date, event in data_list:
        if pattern.match(event):
            # process the date into CalendarDate
            calendar_date = convert_calendar_date(date.split(' '))
            # passed event is ignored
            if not calendar_date.is_passed():
                tuition_date_list.append((calendar_date, event))

    return tuition_date_list



def main():
    url = 'http://www.rpi.edu/academics/calendar/'

    # set up chrome option
    chrome_options = Options()
    # 不显示browser
    chrome_options.add_argument("--headless")

    # set up selemium webdriver browser
    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    driver.get(url)

    # use Bs4 to extract the calendar from page source
    soup = BeautifulSoup(driver.page_source, "lxml")
    calendar_data = soup.find_all('td')

    # process data into list form (date, event)
    calendar_list = analyze_calendar_data(calendar_data)

    analyze_tuition_time(calendar_list)



    # # create html file to store page source
    # file = open("rpi_calendar.html", "w", encoding="utf-8")
    # for date, event in calendar_list:
    #     file.write(date + ": " + event + "\n")


if __name__ == '__main__':
    main()
