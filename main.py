import multiprocessing
import time 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
def open_website(website_url, wait_time):
    # Start a Chrome browser service and create a webdriver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.set_window_size(400, 400)
    # Navigate to the website and wait for the specified amount of time
    driver.get(website_url)
    time.sleep(wait_time)

    # Close the web browser
    driver.quit()

# Create a list of websites to visit
website_urls = [
    "https://jingbeishui.github.io/2015/05/11/see-u-ali/",
    "https://36kr.com/p/1724055306241",
    "https://kenvix.com/post/computer-vision-getting-started/",
    "https://jingbeishui.github.io/2015/05/11/see-u-ali/",
    "https://vcb-s.com/archives/10563",
    "https://vcb-s.com/archives/10563",
    "https://kenvix.com/post/computer-vision-getting-started/",
    "https://www.playpi.org/2019061301.html",
    "https://vcb-s.com/archives/10563",
    "https://36kr.com/p/1724055306241",

]

# Create a process for each website
processes = []
wait_time = 10  # Wait 10 seconds on each website
for url in website_urls:
    process = multiprocessing.Process(target=open_website, args=(url, wait_time))
    processes.append(process)

if __name__ == '__main__':
    # Start all of the processes
    for process in processes:
        process.start()

    # Wait for all of the processes to complete
    for process in processes:
        process.join()

    # All of the processes have completed
    print("All processes finished")
