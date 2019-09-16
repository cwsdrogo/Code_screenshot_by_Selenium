from selenium import webdriver
from PIL import Image

'''
    登录界面截图，并对验证码进行截取
'''

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://sec.ssc85.com/')


def get_pic(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('pic.png')
    #  打开一个图片文件
    pic = Image.open('pic.png')
    #  返回图片对象
    return pic

#  验证码图片位置的定位
captcha_element = driver.find_element_by_id('validate')
#  获得验证码的位置和大小
location = captcha_element.location
size = captcha_element.size
left = location['x']
top = location['y']
right = left + size['width']
bottom = top + size['height']

pic = get_pic(driver)
image = pic.crop((left, top, right, bottom))
image.save('result.png')