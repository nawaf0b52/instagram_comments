import time
import sys
from selenium import webdriver

counter = []
counter2 = 0
list_info = []
list_url = []
info_user_list = []
list_url = []
user = []
comments = []
tag = []
replies = []

url_inst = str(input('enter user:>> '))
def url_post(url_inst):
    add = 0
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get('https://www.instagram.com/{}/'.format(url_inst))
    info_f = driver.find_element_by_class_name('k9GMp')
    info = info_f.find_elements_by_class_name('g47SY')
    for i in info:
        list_info.append(i.text)

    add_post = list_info[0]
    p = int(add_post) / 100
    p = p * 9
    print(int(p))
    print(add_post)
    while int(p) > add:
        driver.execute_script('window.scrollTo(0,10000000)')
        time.sleep(1)
        add = add + 1
        url_post = driver.find_element_by_class_name('FyNDV')
        url = url_post.find_elements_by_tag_name('a')
        for test_url in url:
            try:
                print(test_url.get_attribute("href"))
                url1 = test_url.get_attribute("href")
                if url1 not in list_url:
                    list_url.append(url1)
                # time.sleep(0.3)
            except:
                break
    print("عدد المنشورات {}".format(len(list_url)))
    driver.close()


def comment_post(url):
    driver = webdriver.Chrome()
    # driver.implicitly_wait(30)
    driver.get(str(url))
    try:
        questions_table = driver.find_element_by_class_name("k59kT")
        button = questions_table.find_elements_by_tag_name("button")
        try:
            button = questions_table.find_elements_by_tag_name("button")
            button = button[0]
            while True:
                try:
                    button.click()
                    time.sleep(1)
                except:
                    break
            trs = questions_table.find_elements_by_tag_name("a")
            tco = questions_table.find_elements_by_tag_name("span")
            for tr in trs:
                tr = tr.text
                if "#" in tr:
                    tag.append(tr)
                    print(tag)
                elif "@" in tr:
                    replies.append(tr)
                else:
                    user.append(tr)
            for i in tco:
                comments.append(i.text)
            driver.close()
            # counter_threads.remove(url)
        except:
            print('not button in the url : {}'.format(url))
            trs = questions_table.find_elements_by_tag_name("a")
            tco = questions_table.find_elements_by_tag_name("span")
            for tr in trs:
                tr = tr.text
                if "#" in tr:
                    tag.append(tr)
                    print(tag)
                elif "@" in tr:
                    replies.append(tr)
                else:
                    user.append(tr)
            for i in tco:
                comments.append(i.text)
            driver.close()



    except:
        print("لا يوجد تعليقات في هذي الصفحة")
        print(url)
        driver.close()


url_post(url_inst)
for i in list_url:
    comment_post(i)

print("عدد الحسابات المتفاعلة {}".format(len(user)))
print('{} عدد الردود'.format(len(comments)))
file = open('com.txt', 'w', encoding='utf-8')
for i in range(0,len(comments)):
    file.write("{}: {} \n".format(user[i],comments[i]))
file.close()