import csv, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def csv_url_reader(url_obj):
    reader = csv.DictReader(url_obj,delimiter=';')
        for line in reader :
        urls = line['URL']
        title = line['Title']
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        #chrome_options.add_argument("--window-size=1920,1080")
        #chrome_options.add_argument("--incognito")
        #chrome_options.add_argument('--disable-application-cache')
        driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver')
        driver.get(urls)
        time.sleep(2)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        domInteractive = driver.execute_script("return window.performance.timing.domInteractive")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
        domContentLoaded = driver.execute_script("return window.performance.timing.domContentLoadedEventEnd")
        loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")
        ttfb = responseStart - navigationStart
        interactive = domInteractive - navigationStart
        contentloaded = domContentLoaded - navigationStart
        complete = domComplete - navigationStart
        loaddone = loadEventEnd - navigationStart

        print('Testing------->>>>' + urls + "TTFB [responseStart - navigationStart] %s" % ttfb)
        print('Testing------->>>>' + urls + "Interactive [domInteractive - responseStart] %s" % interactive )
        print('Testing------->>>>' + urls + "Contetloaded [domContentLoaded - navigationStart] %s" % contentloaded)
        print('Testing------->>>>' + urls + "Complete [domComplete - navigationsStart] %s" % complete)
        print('Testing------->>>>' + urls + "LoadDone [loadeventend - responseStart] %s" % loaddone)
        

        results = open("results.csv", "a")

        print(urls + "-TTFP perfomance [mileseconds download] %s" % ttfb, file=results)
        print(urls + "-Interactive perfomance [mileseconds download] %s" % interactive, file=results)
        print(urls + "-ContentLoaded perfomance [mileseconds download] %s" % contentloaded, file=results)
        print(urls + "-Complete perfomance [mileseconds download] %s" % complete, file=results)
        print(urls + "-LoadDone perfomance [mileseconds download] %s" % loaddone, file=results)



        results.close()



        driver.quit()


if __name__ == "__main__":
    with open("URL.csv") as url_obj, open("results.csv", "w") as result_file:

        csv_url_reader(url_obj)
