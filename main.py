from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyocr
import pyocr.builders

driver = webdriver.Chrome()

window = (800, 660+123)
driver.set_window_size(*window)

target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()
sleep(10)

center_x = 250 
center_y = 256

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()
print("スタートボタンをクリックしました。")
sleep(2)

actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()
print("おすすめコースのボタンをクリックしました。")

target_xpath = 'html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

tool = pyocr.get_available_tools()[0]

from time import time
start = time()
while time() - start < 90.0:

    # 移動した
    # ファイル名
    fname = "sample_image.png"
    # スクショをする
    driver.save_screenshot(fname)

    # 画像をPILのImageを使って読み込む
    # ローマ字の部分を取り出す
    im = Image.open(fname).crop((340,710,1250,760))
    # im.save('aaa.png', quality=95)

    # # tool で文字を認識させる
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    # # text を確認
    print(text)

    # # 文字を入力させる
    element.send_keys(text)

input("何か入力してください")
driver.close()
driver.quit()