
def BD(echo=bool,link=None,demo=bool):
    import random
    import pyperclip
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import time
    import os
    from subprocess import CREATE_NO_WINDOW

    global name

    google_path = (f'{os.path.expanduser("~")}/AppData/Local/Google/Chrome/User Data')

    options = webdriver.ChromeOptions()
    options.add_argument(r'user-agent=Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.add_argument(r'--user-data-dir=C:/Users/Leonid/AppData/Local/Google/Chrome/User Data/')
    if os.path.exists(f'{os.path.expanduser("~")}/AppData/Local/Google/Chrome/User Data') == False:
        print("у вас не установлен Gogle Chrome")
    options.add_argument(f'--user-data-dir={google_path}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    if echo == True:
        options.add_argument("--headless")
    s = Service(executable_path='chromedriver.exe')
    s.creationflags = CREATE_NO_WINDOW
    
    driver = webdriver.Chrome(service=s, options=options)
    act = ActionChains(driver)



    global pic
    pic = []
    #with open('pic_bd.txt','r',encoding='utf-8') as file:
    #    pic = []
    #    for i in file:
    #        if i == "\n":
    #            continue
    #        else:
    #            pic.append(i)
    def sendPic():
        with open('pic_bd.txt','r',encoding='utf-8') as file:
            for i in file:
                if i =="\n":
                    continue
                else:
                    pic.append(i)
            #pic = [pic for pic in file]
        try:
            pyperclip.copy(random.choice(pic))
        
            time.sleep(2)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(2)
            act.key_down(Keys.CONTROL).send_keys("z").key_up(Keys.CONTROL).perform()
        except:
            pass
    print(pic)
    
    def msg_generator_bd():
        with open('msg_bd.txt','r',encoding='utf-8') as file:

            global msg
            global name
            msg = [msg.rstrip().format(name.split()[0],'\n') for msg in file]
            msg = list(filter(None,msg))
            return msg
    

    def checkurl(args):
        cur = driver.current_url
        if args == cur:
            return True
        else: return False
    
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

    #лен юзерс длинна списка юзерс начинается с 1(не с нуля)
    len_users = len(users)

    #логин каунтер будет считать от 1 - ...n количество аккаунтов отработанных чтобы обратиться по индексу к следующему
    login_counter = 1

    #login
    def login():
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

    try:
        #всегда ON
        driver.delete_all_cookies()
        

        driver.get('http://vk.com/login')
        time.sleep(2)
        login()
        
        driver.get("https://vk.com/feed?section=notifications&w=calendar")
        time.sleep(7)#НЕ МЕНЯТь

        # "//div[contains(.,'сегодня')]/div[(@class='bd_name')]") - код
        elems = driver.find_elements(By.XPATH, "//div[contains(.,'сегодня')]/div[(@class='bd_name')]/a[@href]")
        links = []
        for elem in elems:
            print(elem.text)

        for elem in elems:
            print(elem.get_attribute("href"))
            links.append(elem.get_attribute("href"))
        
        print(links)
        for d in links:
            driver.get(d)
            time.sleep(4)
            checkurl(d)
            time.sleep(1)

            driver.find_element(By.XPATH, '//span[@class="vkuiButton__in"]').click()# нажать на кнопку отправить сообщение
            time.sleep(1)
            try:
                driver.find_element(By.XPATH, '//div[@class="ui_thumb_x_button _close_btn" or role="link"]').click()#проверка на картинку
            except: pass
            time.sleep(2)
            name = ""
            time.sleep(1)
            try:
                
                name = driver.find_element(By.XPATH, '//div[@class="fl_l mail_box_sinlgle_recepient_info"]/a["mail_box_label_peer"]').text
            except:
                print('Сообщение отправить не удалось, причина - закрыта личка')
                continue
            time.sleep(1)
        
            #делаем диалог
            driver.find_element(By.XPATH,'//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').clear()
            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
            sendPic()
            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
            msg_generator_bd()
            time.sleep(2)
            pyperclip.copy(random.choice(msg))
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(1)
            if demo == True:
                pass
            else:
                act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
            time.sleep(1)
            
            
            continue
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    BD(echo=False,demo=True)
# проверка на бота driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
