from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from itertools import product
import time


try:
    # список id. пример: ids = ['inputtype_ece58af95f341f6d2fdb_11_1', 'inputtype_ece58af95f341f6d2fdb_15_1']
    ids = []
    d = webdriver.Chrome()
    d.get('https://sso.openedu.ru/login/?next=/oauth2/authorize%3Fstate%3DJ5HDCeGgupTlLBhldEep6y5c9lPFnCL8%26client_id%3D808f52636759e3616f1a%26redirect_uri%3Dhttps%3A//openedu.ru/complete/npoedsso/%26response_type%3Dcode%26auth_entry%3Dlogin')
    # вводишь логин и пароль от openedu
    d.find_element_by_name('username').send_keys('<login>')
    d.find_element_by_name('password').send_keys('<password>')
    d.find_element_by_id('auth_form_sub').click()
    time.sleep(2)
    d.get('https://courses.openedu.ru/courses/course-v1:ITMOUniversity+SOFTMETH+fall_2019_ITMO/courseware/c3badf7313cd45d6b175de88feaccd6d/8a011455652d41529ba888cb3dc36790/')
    for di in range(len(ids)):
        id = ids[di]
        # вместо <x> - кло-во правильных ответов на момент ЗАПУСКА порграммы
        xres = ids.index(id) + <x>
        time.sleep(3)
        label = d.find_element_by_id(id)
        checks = label.find_elements_by_css_selector('input[type="checkbox"]')
        m = list(product([False, True], repeat=len(checks)))
        del m[0]
        for i in m:
            # print(i)
            WebDriverWait(d, 10).until(
                EC.presence_of_element_located((By.ID, id))
            )
            label = d.find_element_by_id(id)
            checks = label.find_elements_by_css_selector('input[type="checkbox"]')
            for c in checks:
                if c.get_attribute('checked') == "true":
                    c.click()
            for x in range(len(checks)):
                if i[x]:
                    checks[x].click()
            time.sleep(.2)
            d.find_element_by_class_name('btn-brand').click()
            time.sleep(.1)
            WebDriverWait(d, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'btn-brand'))
            )
            if (str(xres)+'/18') in d.find_element_by_xpath('//*[@id="problem_'+id.split('_')[1]+'"]/div[2]/div[4]/span[2]')\
                    .text:
                print('\t\t\tAns: ' + str(i))
                break
            d.execute_script("$(window).scrollTop(0)")
finally:
    time.sleep(5)
    d.quit()
