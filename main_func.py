
def main_func(echo=bool,link=None,we_sub=bool,our_sub=bool,
friend_msg=bool,non_friend_msg=bool,non_friend_add=bool,demo=bool):
    import pyperclip
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import time
    import random
    import datetime
    import os
    from subprocess import CREATE_NO_WINDOW



    now = str(datetime.datetime.now().replace(second=0, microsecond=0))
    google_path = (f'{os.path.expanduser("~")}/AppData/Local/Google/Chrome/User Data')
    

    options = webdriver.ChromeOptions()
    options.add_argument(r'user-agent=Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.77')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
 

    act = ActionChains(driver)
    
    #чек URL *фикс от забаненых пользователей
    def checkurl(args):
        cur = driver.current_url
        if args == cur:
            return True
        else: return False

    #чтение
    with open("old_pers.txt", "r", encoding='utf-8') as g:
        old_pers = [old_pers.rstrip() for old_pers in g]
    with open("target.txt", "r", encoding='utf-8') as g:
        target = [target.rstrip() for target in g]
    #внизу пишет отступ для удобства
    with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n")

    

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

    #лен юзерс длинна списка юзерс начинается с 1(не с нуля)
    len_users = len(users)
    
    #логин каунтер будет считать от 1 - ...n количество аккаунтов отработанных чтобы обратиться по индексу к следующему
    login_counter = 1

    #login
    def login(login_counter):
        try:
            if driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]'):
                    #driver.find_element(By.XPATH, '//*[@id="quick_login"]/button["войти"]').click()
                    #driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]').click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').clear()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="index_email"]').send_keys(users[f'{login_counter}']['login'])
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/form/button[1]/span/span["войти"]').click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').clear()
                    time.sleep(1.3)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input').send_keys(users[f'{login_counter}']['password'])
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[2]/button[1]/span[1]/span["продолжить"]').click()
                    print('прошел авторизацию')
                    time.sleep(3) 
                    driver.get('https:vk.com/feed')
        except: pass

    #logout
    def logout():
        driver.get("http://vk.com/feed")
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="top_profile_link"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="top_logout_link"]/span').click()
        time.sleep(1)
    
    global pic
    pic = ''
    with open('pic.txt','r',encoding='utf-8') as file:
        pic = [pic for pic in file]
    def sendPic():
        with open('pic.txt','r',encoding='utf-8') as file:
            pic = [pic for pic in file]
        try:
            pyperclip.copy(random.choice(pic))
        
            time.sleep(2)
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(2)
            act.key_down(Keys.CONTROL).send_keys("z").key_up(Keys.CONTROL).perform()
        except:
            pass
    




    
    test_list = []

    #чтение с текстового файла MSG - {}= имя , {1}=перенос строки
    global name
    name='s'
    def msg_generator():
        with open('msg.txt','r',encoding='utf-8') as file:
            global msg
            global name
            msg = [msg.rstrip().format(name.split()[0],'\n') for msg in file]
            msg = list(filter(None,msg))
            return msg
    msg_generator()
    print(msg)


    try:
        #всегда ON
        driver.delete_all_cookies()
        #
        #
        driver.get("http://vk.com/login")
        time.sleep(2)
        login(login_counter)
        limit = 0 
        limit_add = 0
        for d in target:
            if d in old_pers: continue
            driver.get(d)
            time.sleep(2)
            
            #проверки на забаненых
            if checkurl(d) == False: continue
            #проверка на логаут
            login(login_counter)


            print(limit, ' из 20')
            #выход из цикла
            if limit >= 20:
                login_counter = login_counter + 1
                
                if len_users < login_counter:
                    break
                else:
                    logout()
                    continue
            
            try:
                if driver.find_element(By.XPATH, '//div[@class="ProfileHeaderButton"]/button/span/span[contains(.,"Добавить в друзья")]'):
                    time.sleep(1)
                    print('Пользователь еще не друг')
                    time.sleep(1)
                    if driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button/span[1]/span'):
                        if non_friend_add ==True:
                            print('non_friend_add ПРОШЕЛ')
                            if demo == True:
                                pass
                            else:
                                if limit_add >= 40:
                                    limit_add = limit_add + 1
                                    driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/button/span[1]/span').click()

                        print('Я нашел кнопку добавить в друзья')
                        time.sleep(2)

                    if driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span[1]/span/div'):
                        print('я нашел кнопку написать сообщение')
                        if non_friend_msg == True:
                            print('non_friend_msg ПРОШЕЛ')
                            driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span[1]/span/div').click()
                            time.sleep(2)
                            try:#проверка на картинку
                                driver.find_element(By.XPATH, '//div[@class="ui_thumb_x_button _close_btn" or role="link"]').click()
                            except: pass
                            time.sleep(2)
                            name = ""
                            time.sleep(2)
                            try:#заносим имя в переменную
                                
                                name = driver.find_element(By.XPATH, '//div[@class="fl_l mail_box_sinlgle_recepient_info"]/a["mail_box_label_peer"]').text
                            except:
                                print('Сообщение отправить не удалось, не нашел имя')
                                if demo == True:
                                    pass
                                else:
                                    with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' добавлен в друзья, но' + ' СООБЩЕНИЕ НЕ БЫЛО ОТПРАВЛЕНО')
                            
                                continue
                            time.sleep(2)
                            #делаем диалог
                            driver.find_element(By.XPATH,'//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()
                            time.sleep(2)
                            try:
                                driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').clear()
                            except:pass
                            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                            sendPic()
                            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                            msg_generator()
                            time.sleep(2)
                            pyperclip.copy(random.choice(msg))
                            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                            time.sleep(1)
                            if demo == True:
                                pass
                            else:
                                act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()                
                            time.sleep(1)
                            
                            limit = limit + 1
                            if demo == True:
                                pass
                            else:
                                with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' добавлен в друзья, сообщение отправлено')

                            continue
                        else:
                            print('Закрыта личка')
                            if demo == True : pass
                            else: 
                                with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' добавлен в друзья, ' + ' СООБЩЕНИЕ НЕ БЫЛО ОТПРАВЛЕНО')
                            continue

            except:
                pass   
                    
            try:
                if driver.find_element(By.XPATH, '//div[@class="ProfileHeaderButton"]/button/span/span[contains(.,"Вы подписаны")]'):
                    time.sleep(1)
                    print('Мы подписаны')
                    #with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' мы подписаны')
                    
                    
                if we_sub == True:    
                    print('we_sub ПРОШЕЛ')
                    if driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span[1]/span/div'):
                        print('я нашел кнопку написать сообщение')
                        time.sleep(2)
                        driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/a/span[1]/span/div').click()
                        time.sleep(5)
                        name = ""
                        time.sleep(2)
                        try:#заносим имя в переменную
                            name = driver.find_element(By.XPATH, '//div[@class="fl_l mail_box_sinlgle_recepient_info"]/a["mail_box_label_peer"]').text
                        except:
                            print('Сообщение отправить не удалось, причина - закрыта личка')
                            if demo == True: pass
                            else:
                                with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' мы подписаны, сообщение не отправлено')
                            continue    
                        time.sleep(2)
                        driver.find_element(By.XPATH,'//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()
                        time.sleep(3)
                        try:
                            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').clear()
                        except:pass
                        driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                        sendPic()
                        driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                        msg_generator()
                        time.sleep(2)
                        pyperclip.copy(random.choice(msg))
                        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        if demo == True:
                            pass
                        else:    
                            act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()                 
                        time.sleep(1)
                        
                        limit = limit + 1
                        if demo == True:
                            pass
                        else:
                            with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' мы подписаны, сообщение отправлено')

            except:
                pass           
            try:
                if driver.find_element(By.XPATH, '//div[@class="ProfileHeaderButton"]/a/span/span[contains(.,"Сообщение")]'):
                    time.sleep(1)
                    print('уже друг')
                    if friend_msg == True:
                        print('friend_msg ПРОШЕЛ')
                        time.sleep(2)
                        driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/span[1]/span').click()
                        time.sleep(2)
                        name = ""
                        time.sleep(2)
                        try:#заносим имя в переменную
                            name = driver.find_element(By.XPATH, '//div[@class="fl_l mail_box_sinlgle_recepient_info"]/a["mail_box_label_peer"]').text
                        except:
                            print('Сообщение отправить не удалось, причина - закрыта личка')
                            if demo == True: pass
                            else:
                                with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' наш друг, сообщение не отправлено')
                            continue    
                        time.sleep(2)
                        driver.find_element(By.XPATH,'//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()
                        time.sleep(2)
                        try:
                            driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').clear()
                        except:pass
                        driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                        sendPic()
                        driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                        msg_generator()
                        time.sleep(2)
                        pyperclip.copy(random.choice(msg))
                        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        if demo == True:
                                pass
                        else:
                            act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                     
                        time.sleep(1)
                        if demo == True:
                            pass
                        else:
                            with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' наш друг, сообщение отправлено')
            except:
                pass
            try:
                if driver.find_element(By.XPATH, '//div[@class="ProfileHeaderButton"]/button/span/span[contains(.,"Ответить на заявку")]'):
                    time.sleep(1)
                    print('наш подписчик')
                if our_sub == True:
                    print('our_sub ПРОШЕЛ')
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/a/span[1]').click()
                    time.sleep(2)
                    name = ""
                    time.sleep(2)
                    try:#заносим имя в переменную
                        name = driver.find_element(By.XPATH, '//div[@class="fl_l mail_box_sinlgle_recepient_info"]/a["mail_box_label_peer"]').text
                    except:
                        print('Сообщение отправить не удалось, причина - закрыта личка')
                        if demo==True:
                            pass
                        else:
                            with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' наш подписчик, сообщение не отправлено')
                        continue
                    time.sleep(2)
                    driver.find_element(By.XPATH,'//*[@id="box_layer"]/div[2]/div/div[1]/div[2]/a').click()
                    time.sleep(2)
                    try:
                        driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').clear()
                    except:pass
                    driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                    sendPic()
                    driver.find_element(By.XPATH, '//div[(@class="im_editable im-chat-input--text _im_text")]').click()
                    msg_generator()
                    time.sleep(2)
                    pyperclip.copy(random.choice(msg))
                    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                    time.sleep(1)
                    if demo == True:pass
                    else:
                        act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

                    time.sleep(1)    
                    if demo == True:
                        pass                
                    else:
                        with open("old_pers.txt", "a+", encoding='utf-8') as g: g.write("\n" + d + "\n" + now + ' наш подписчик, сообщение отправлено')
                    
            except:
                pass            
            
            
            continue
            

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    main_func(echo=False,link=None)