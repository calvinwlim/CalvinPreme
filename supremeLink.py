#from config import keys

from selenium import webdriver
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

#first url is main second url is unique
atcwebhook_urls = ['']
atcwebhook = DiscordWebhook(url=atcwebhook_urls)

# create embed object for webhook
atcembed = DiscordEmbed(title='Added To Cart', description='ATC Bruh', color=242424)
atcembed.set_footer(text='PengoofPreme')
atcembed.set_timestamp()
atcembed.add_embed_field(name='Site', value='Supreme US')
atcembed.add_embed_field(name='Item', value='Waist Bag Black')
atcembed.add_embed_field(name='Mode', value='Browser')
atcwebhook.add_embed(atcembed)

#first url is main second url is unique
captchawebhook_urls = ['']
captchawebhook = DiscordWebhook(url=captchawebhook_urls)

# create embed object for webhook
captchaembed = DiscordEmbed(title='Requires Captcha', description='Please Solve ReCaptcha Challenge', color=242424)
captchaembed.set_footer(text='PengoofPreme')
captchaembed.set_timestamp()
captchaembed.add_embed_field(name='Site', value='Supreme US')
captchaembed.add_embed_field(name='Item', value='Waist Bag Black')
captchaembed.add_embed_field(name='Mode', value='Browser')
captchawebhook.add_embed(captchaembed)

#first url is main second url is unique
paymentwebhook_urls = ['']
paymentwebhook = DiscordWebhook(url=paymentwebhook_urls)

# create embed object for webhook
paymentembed = DiscordEmbed(title='Successful Checkout', description='Payment Processed', color=242424)
paymentembed.set_footer(text='PengoofPreme')
paymentembed.set_timestamp()
paymentembed.add_embed_field(name='Site', value='Supreme US')
paymentembed.add_embed_field(name='Item', value='Waist Bag Black')
paymentembed.add_embed_field(name='Mode', value='Browser')
paymentwebhook.add_embed(paymentembed)


keys = {
    "productlink": "https://www.supremenewyork.com/shop/sweatshirts/cjb56hgul/s8ns7tlqy",
    "name": "John Doe",
    "email": "bruh@gmail.site",
    "tel": "1231234123",
    "address": "12345 Bot Avenue",
    "apt": "",
    "zip": "94555",
    "city": "Preme Town",
    "state": "AL",
    "country": "United States",
    "card number": "1234123412341234",
    "month": "04",
    "year": "20",
    "cvv": "123"
}

def order(keys):
    driver = webdriver.Chrome('./chromedriver')
    #go to product page
    driver.get(keys['productlink'])
    #atc
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    atcwebhook.execute()
    time.sleep(.75)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    #name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys["name"])
    #email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys["email"])
    #phone number
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys["tel"])
    #address
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys["address"])
    #zip code
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys["zip"])
    #city
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys["city"])
    #card number
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys["card number"])
    #cvv
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["cvv"])
    #captcha
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    captchawebhook.execute()
    #process payment
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    paymentwebhook.execute()
    time.sleep(180)

order(keys)