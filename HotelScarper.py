from selenium import webdriver
import  time
import random
import requests
import csv
CHROMECAST = "C:\DEVELOPMENT\chromedriver.exe"





driver = webdriver.Chrome(CHROMECAST)



driver.get('https://downtowndallas.com/wearedowntown/')

popup = driver.find_element_by_xpath('/html/body/div[2]/div/a')
popup.click()
time.sleep(1)
experince = driver.find_element_by_xpath('/html/body/header/nav/div/ul/li[3]')
experince.click()
time.sleep(1)

stay = driver.find_element_by_xpath('/html/body/main/div/section[1]/section/div[4]/a')
stay.click()


time.sleep(3)


totalhotel = driver.find_elements_by_xpath('/html/body/main/div/section[2]/div')

number = random.randint(1,len(totalhotel))

location_image = driver.find_element_by_xpath(f'/html/body/main/div/section[2]/div[{number}]/div[1]/img').get_attribute('src')
response = requests.get(url=location_image,headers={'User-Agent': 'Mozilla/5.0'}).content


with open(f'images\image{number}.png',mode='wb') as file:
    file.write(response)




hotel = driver.find_element_by_xpath(f'/html/body/main/div/section[2]/div[{number}]')
hotel.click()


name = driver.find_element_by_xpath('/html/body/main/article/header/h1').text
location = driver.find_element_by_xpath('/html/body/main/article/div/div[1]/div[1]/a').text
location_map = driver.find_element_by_xpath('/html/body/main/article/div/div[1]/div[1]/a').get_attribute('href')

phone_number = driver.find_element_by_xpath('/html/body/main/article/div/div[1]/div[2]/div/a').text


reponse = requests.get(location_image).content
fields = ['Name','address','phonenumber','imageurl']
mydict = {'Name':f'{name}','address':f'{location}','phonenumber':f'{phone_number}','imageurl':f'{location_image}'}

try:
    with open('hoteldata.csv', mode='a', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writerow(mydict)

except:
    with open('hoteldata.csv', mode='w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerow(mydict)





driver.close()
