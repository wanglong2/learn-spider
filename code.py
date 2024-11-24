from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

browser = webdriver.Chrome()
chrome_options = Options()
# 添加user-agent    --user-agent=
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                            "like Gecko) Chrome/131.0.0.0 Safari/537.36")
# 添加代理  --proxy-server=ip:port
chrome_options.add_argument('--proxy-server=59.54.238.167:17506')
browser.get("https://dazi.kukuw.com/")
button = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/form/ul[6]/li[2]/input")
button.click()
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/form/div[3]/div[1]/div/span")))
contents = browser.find_elements(By.XPATH, "/html/body/div[2]/form/div[3]/div[@class='typing' or @class='typing "
                                           "typing_on']")
len_contents = len(contents)
for i in range(1, len_contents + 1):
    try:
        content = browser.find_element(By.XPATH, f"/html/body/div[2]/form/div[3]/div[{i}]/div/span")
        t = content.text
        input_box = browser.find_element(By.XPATH, f"/html/body/div[2]/form/div[3]/div[{i}]/input[@class='typing']")
        browser.execute_script("arguments[0].removeAttribute('readonly');", input_box)
        print(content.text)
        for j in range(0, len(t)):
            input_box.send_keys(t[j])
        pyautogui.press('space')
    except KeyError:
        print("it is over ......")
        break
input("按 Enter 键继续，手动关闭浏览器...")
browser.close()
