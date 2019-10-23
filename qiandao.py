import time
from splinter import Browser
def qiandao(username, password):
    browser.find_by_xpath('//*[@id="aw-login-user-name"]').fill(username)
    browser.find_by_xpath('//*[@id="aw-login-user-password"]').fill(password)
    time.sleep(2)
    browser.find_by_xpath('//*[@id="login_submit"]').click()
    time.sleep(6)
    browser.execute_script("sign()")
    time.sleep(4)
    print(username,'签到完成')
    browser.back()
with Browser() as browser:
    url = 'https://webvpn.tjise.edu.cn'
    browser.visit(url)
    browser.find_by_xpath('//*[@id="user_login"]').fill('ssqy021')
    browser.find_by_xpath('//*[@id="user_password"]').fill('12qwaszx')
    browser.find_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/input').click()
    time.sleep(1)
    # browser.find_by_xpath
    
    browser.find_by_xpath('/html/body/div[4]/div/ul/li/a/h4').click()
    time.sleep(1)
    browser.windows.current=browser.windows[1]
    qiandao('17361831774','12qwaszx')
    qiandao('13333523958','hello19981123LM')
    qiandao('15822667022','123456Pp')
    qiandao('15900358343','TRredhot1')
    qiandao('15922081855','abcd1234')
    qiandao('18622120155','abcd1234')
    qiandao('18984446041','byy727599')
    qiandao('18222610056','ws19971222')
    qiandao('18748236262','nailiang97')
    qiandao('13032253755','jiawei83332416')
    print('所有签到完成')