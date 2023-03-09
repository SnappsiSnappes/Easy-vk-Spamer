""" //div[@class="fans_rows"]/div[(@class="fans_fan_row inl_bl")]/div[(@class="fans_fan_name")]/a[@href]
xpath """



def parcing_group(echo=bool,link='',demo=bool,worker=None):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import time
    import os
    from subprocess import CREATE_NO_WINDOW
    #очистка
    open('target.txt', 'w',encoding='utf-8').close()




    google_path = (f'{os.path.expanduser("~")}/AppData/Local/Google/Chrome/User Data')
    options = webdriver.ChromeOptions()
    options.add_argument(r'user-agent=Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument(r'--user-data-dir=C:/Users/Leonid/AppData/Local/Google/Chrome/User Data/')
    if os.path.exists(f'{os.path.expanduser("~")}/AppData/Local/Google/Chrome/User Data') == False:
        print("у вас не установлен Gogle Chrome")
    options.add_argument(f'--user-data-dir={google_path}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--start-maximized")

    if echo == True:
        options.add_argument("--headless")


    s = Service(executable_path='chromedriver.exe')
    s.creationflags = CREATE_NO_WINDOW

    driver = webdriver.Chrome(service=s, options=options)


    #список юзерс с логинами и паролями читаем из файла users.txt
    users = {
        #'1':{'password':'qwerty123','login':'79000'},
        #'2':{'password':'asdq_w','login':'790000'}
    }
    #проверка на существование users.txt если false то создает пустой файл
    if os.path.exists('users.txt') == False:
        with open('users.txt',"a+",encoding='utf=8') as g: g.close()

    with open("users.txt","r",encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                continue
            key1, key2, value1, key3, value2 = line.split()
            users.update({key1:{key2:value1,key3:value2}})
        
    #def scrolldown():
    #    body = driver.find_element(By.XPATH, '/html/body')
    #    body.click()
    #    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

    try:
        #всегда ON
        driver.delete_all_cookies()
        #
        driver.get("http://vk.com/login")

        try:
            if driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]'):
                    #driver.find_element(By.XPATH, '//*[@id="quick_login"]/button["войти"]').click()
                    #driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]').click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').clear()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').send_keys(users['1']['login'])
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]').click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').clear()
                    time.sleep(1.3)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').send_keys(users['1']['password'])
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[2]/button[1]/span[1]/span["продолжить"]').click()
                    print('прошел авторизацию')
                    time.sleep(3) 
                    driver.get('https:vk.com/feed')
        except: pass
        print('я скинул аутентивифкацию. линк = ',link)
        time.sleep(2)
        driver.get(f"{link}")
        time.sleep(4)
        try:
            driver.find_element(By.XPATH, '//*[@id="group_followers"]/a/div/span[1]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="public_followers"]/a/div/span[1]').click()
        except:
            pass
        time.sleep(7)

        #"//div[contains(.,'сегодня')]/div[(@class='bd_name')]/a[@href]"
        c = driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/h2/ul/li[1]/div').text
        c = c.replace('Подписчики','')
        с = float(c)
        s = float(5)
        c = float(c) - s
        
        
        print(c)
        
        while True:
            d = 0
            dd = 10
            while d != dd:
                ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                d = d+1
                    
            elemsCount = len(driver.find_elements(By.XPATH, '//div[@class="fans_rows"]/div[(@class="fans_fan_row inl_bl")]/div[(@class="fans_fan_name")]/a[@href]'))
            print(elemsCount)
            if elemsCount >= int(c):
                break
        
        #last_pos = driver.find_element(By.XPATH, '//*[@id="layer_stl"]').get_attribute("style")
        #time.sleep(1)
        #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #time.sleep(1)
        #new_pos = driver.find_element(By.XPATH, '//*[@id="layer_stl"]').get_attribute("style")
        #
        #while new_pos != last_pos:
        #    last_pos = driver.find_element(By.XPATH, '//*[@id="layer_stl"]').get_attribute("style")
        #    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
        #    time.sleep(.7)
        #    new_pos = driver.find_element(By.XPATH, '//*[@id="layer_stl"]').get_attribute("style")
        #    if new_pos == last_pos:
        #        break
        

        
        elems = driver.find_elements(By.XPATH, '//div[@class="fans_rows"]/div[(@class="fans_fan_row inl_bl")]/div[(@class="fans_fan_name")]/a[@href]')
        links = []
        for e in elems:
            links.append(e.get_attribute("href"))
        
        
        

        for i in links:
            with open("target.txt", "a+", encoding='utf-8') as g:
                g.write("\n" + i)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# проверка на бота driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
if __name__ == '__main__':
    parcing_group(echo=False,link='https://vk.com/sunstudiosolo')