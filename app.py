import requests
import names
import random
from bs4 import BeautifulSoup
import string
import json

def randomLetter():
    return random.choice(string.ascii_uppercase)

with open('config.json') as config:
    config = json.load(config)



def loadProxy():
    with open('proxies.txt','r') as proxyIn:
        proxyInput = proxyIn.read().splitlines()
    
    proxyList = [i for i in proxyInput]
    p = random.choice(proxyList)
    p = p.split(':')
    try:
        proxies = {
            'http':f'http://{p[2]}:{p[3]}@{p[0]}:{p[1]}',
            'https':f'https://{p[2]}:{p[3]}@{p[0]}:{p[1]}'
        }
    except:
        proxies = {
            'http':f'http://{p[0]}:{p[1]}',
            'https':f'https://{p[0]}:{p[1]}'
        }
    return proxies

class Generator:
    def __init__(self):
        print("--------")
        print("CONFIG")
        print(config)
        print("--------")
        print("1. Create Accounts <> 2. Set Address")
        opt = input("Enter Input --> ")
        if opt == "1":
            opt2 = input("How many accounts ? --> ")
            for i in range(int(opt2)):
                self.getPage()
        if opt == "2":
            self.addySet2()


    def getPage(self):
        self.s = requests.session()
        page = self.s.get(f'https://www.solebox.com/{config["sbxRegion"]}/registration?url=1',proxies=loadProxy(),headers={
            'authority': 'www.solebox.com',
            'path': f'/{config["sbxRegion"]}/registration?rurl=1',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        })
        if page.status_code == 200:
            soup = BeautifulSoup(page.text,"html.parser")
            self.csrf = soup.find("input",{"name":"csrf_token"})["value"]
            self.create()


    def create(self):
        self.first = names.get_first_name()
        self.last = names.get_last_name()
        numbers = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
        form = {
            'dwfrm_profile_register_title': 'mr',
            'dwfrm_profile_register_firstName': self.first,
            'dwfrm_profile_register_lastName': self.last,
            'dwfrm_profile_register_email': f'{self.first}{self.last}{numbers}{config["catchall"]}',
            'dwfrm_profile_register_emailConfirm': f'{self.first}{self.last}{numbers}{config["catchall"]}',
            'dwfrm_profile_register_password': config["password"],
            'dwfrm_profile_register_passwordConfirm': config["password"],
            'dwfrm_profile_register_phone': config["phone"],
            'dwfrm_profile_register_birthday': '10.11.1995',
            'dwfrm_profile_register_acceptPolicy': True,
            'csrf_token': self.csrf,
        }
        createAcc = self.s.post(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Account-SubmitRegistration?rurl=1&format=ajax',proxies=loadProxy(),data=form,headers={
            'authority':'www.solebox.com',
            'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Account-SubmitRegistration?rurl=1&format=ajax',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language':'en-US,en;q=0.9',
            'content-length': '659',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.solebox.com',
            'referer': f'https://www.solebox.com/{config["sbxRegion"]}/registration?rurl=1',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        })
        print(createAcc.status_code)
        self.email = f'{self.first}{self.last}{numbers}{config["catchall"]}:{config["password"]}'
        print(f'{self.first}{self.last}{numbers}{config["catchall"]}:{config["password"]}')
        with open('accounts.txt','a') as accountFile:
            accountFile.write(f'{self.first}{self.last}{numbers}{config["catchall"]}:{config["password"]}\n')
        with open('accountsWithNames.txt','a') as accountFile:
            accountFile.write(f'{self.first}{self.last}{numbers}{config["catchall"]}:{config["password"]}:{self.first}:{self.last}\n')


    def addySet2(self):
        self.s = requests.session()

        with open('accountsWithNames.txt','r') as accountList:
            for a in accountList.readlines():
                acc = a.split(':')
                lastName = acc[3].replace('\n','')
                page = self.s.get(f'https://www.solebox.com/{config["sbxRegion"]}/login',proxies=loadProxy(),headers={
                    'authority': 'www.solebox.com',
                    'scheme': 'https',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                })
                if page.status_code == 200:
                    soup = BeautifulSoup(page.text,"html.parser")
                    try:
                        csrf = soup.find("input",{"name":"csrf_token"})["value"]
                    except:
                        pass
        
                form = {
                    'dwfrm_profile_customer_email': acc[0],
                    'dwfrm_profile_login_password': acc[1],
                    'csrf_token': csrf
                }
                loginACC = self.s.post(f'https://www.solebox.com/{config["sbxRegion"]}/authentication?rurl=1&format=ajax',proxies=loadProxy(),data=form,headers={
                    'authority':'www.solebox.com',
                    'path': f'/{config["sbxRegion"]}/authentication?rurl=1&format=ajax',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language':'en-US,en;q=0.9',
                    'content-length': '299',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.solebox.com',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/login',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })


                ### delivery
                
                addyPage = self.s.get(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-AddAddress?methodId=home-delivery_europe&format=ajax',proxies=loadProxy(),headers={
                    'authority':'www.solebox.com',
                    'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-AddAddress?format=ajax',
                    'scheme': 'https',
                    'accept': 'en-US,en;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language':'en-US,en;q=0.9',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/addresses',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })
                if addyPage.status_code == 200:
                    soup = BeautifulSoup(addyPage.text,"html.parser")
                    csrf = soup.find("input",{"name":"csrf_token"})["value"]
        
                randomFour = f'{randomLetter()}{randomLetter()}{randomLetter()}{randomLetter()}'
        
                street = f'{randomFour} {config["street"]}'
                set1 = {
                    'street': street,
                    'houseNo': config["house"],
                    'postalCode': config["postCode"],
                    'city': config["city"],
                    'country': config["countryCode"],
                    'csrf_token': csrf
                }
                setAddress1 = self.s.post(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/CheckoutAddressServices-Validate?format=ajax',proxies=loadProxy(),data=set1,headers={
                    'authority': 'www.solebox.com',
                    'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/CheckoutAddressServices-Validate?format=ajax',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '273',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.solebox.com',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/addresses',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })
        
                room = f'Room {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}'
                save1 = {
                    'dwfrm_address_title': 'Herr',
                    'dwfrm_address_firstName': acc[2],
                    'dwfrm_address_lastName': lastName,
                    'dwfrm_address_postalCode': config["postCode"],
                    'dwfrm_address_city': config["city"],
                    'dwfrm_address_street': street,
                    'dwfrm_address_suite': config["house"],
                    'dwfrm_address_address1': '',
                    'dwfrm_address_address2': room,
                    'dwfrm_address_phone': '',
                    'dwfrm_address_countryCode': config["countryCode"],
                    'csrf_token': csrf
                }
        
                saveAddress1 = self.s.post(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-SaveAddress?methodId=home-delivery_europe&countryCode={config["countryCode"]}&format=ajax',proxies=loadProxy(),data=save1,headers={
                    'authority': 'www.solebox.com',
                    'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-SaveAddress?methodId=home-delivery_europe&countryCode={config["countryCode"]}&format=ajax',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '268',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.solebox.com',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/addresses',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })

                self.s.get(f'https://www.solebox.com/{config["sbxRegion"]}/addresses?format=ajax')


                ### billing

                addyPage = self.s.get(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-AddBillingAddress?format=ajax',proxies=loadProxy(),headers={
                    'authority':'www.solebox.com',
                    'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-AddBillingAddress?format=ajax',
                    'scheme': 'https',
                    'accept': 'en-US,en;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language':'en-US,en;q=0.9',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/addresses',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })
                if addyPage.status_code == 200:
                    soup = BeautifulSoup(addyPage.text,"html.parser")
                    csrf = soup.find("input",{"name":"csrf_token"})["value"]
        
                randomFour = f'{randomLetter()}{randomLetter()}{randomLetter()}{randomLetter()}'
        
        
                set1 = {
                    'dwfrm_billingaddress_title': 'Herr',
                    'dwfrm_billingaddress_firstName': acc[2],
                    'dwfrm_billingaddress_lastName': lastName,
                    'dwfrm_billingaddress_postalCode': config["postCode"],
                    'dwfrm_billingaddress_city': config["city"],
                    'dwfrm_billingaddress_street': street,
                    'dwfrm_billingaddress_suite': config["house"],
                    'dwfrm_billingaddress_address1':'' ,
                    'dwfrm_billingaddress_address2': room,
                    'dwfrm_billingaddress_countryCode': config["countryCode"],
                    'csrf_token': csrf
                }
                setAddress1 = self.s.post(f'https://www.solebox.com/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-SaveAddress?isBilling=true&format=ajax',proxies=loadProxy(),data=set1,headers={
                    'authority': 'www.solebox.com',
                    'path': f'/on/demandware.store/Sites-solebox-Site/{config["sbxRegion"]}/Address-SaveAddress?isBilling=true&format=ajax',
                    'scheme': 'https',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '554',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.solebox.com',
                    'referer': f'https://www.solebox.com/{config["sbxRegion"]}/addresses',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest'
                })
                print(setAddress1.text)

                self.s.get(f'https://www.solebox.com/{config["sbxRegion"]}/addresses?format=ajax')

                with open('accountsWithAddress.txt','a') as accountFile:
                    accountFile.write(f'{acc[0]}:{config["password"]}\n')


    

Generator()
