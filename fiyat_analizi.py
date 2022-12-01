# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:02:19 2022

@author: Osman VARIŞLI
"""

import requests;
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import time
import smtplib
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}


def mail_gonder(urun_adi,site):
    email_adres = 'benim_mailim_guzel_mailim'     # mail adresi eklenmeli
    konu = 'Fiyat Düştü'
    icerik = ' Ürün Adi : '+urun_adi+' <br> site :'+site
    zemin = '- Test' 
    sifre = 'benim_sifrem_guzel_sifrem'   # Şifre eklenmeli
    

    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) 
    conn.ehlo()
    conn.login(email_adres, sifre)
    conn.sendmail(email_adres,
                  email_adres,
                  konu + icerik + zemin)
    conn.quit()
                  
def fiyat_getir(dom,site):

    try:
        if site=="hepsiburada":
            fiyat = dom.xpath('//*[@data-bind="markupText:\'currentPriceBeforePoint\'"]')[0].text
        elif site=="amazon":
            fiyat = dom.xpath('//*[@class="a-price-whole"]')[0].text
        elif site=="n11":
            fiyat = dom.xpath('//*[@class="price"]')[0].text
        elif site=="ciceksepeti":
            fiyat = dom.xpath('//*[@class="price__integer-value"]')[1].text           
        elif site=="trendyol":
            fiyat = dom.xpath('//*[@class="prc-box-dscntd"]')[0].text            
            
    except AttributeError:
        fiyat = 0	
    fiyat,virguldensonra,blaa=fiyat.partition(',')
    fiyat,virguldensonra,blaa=fiyat.partition(' ')
    print(fiyat+'---------')
    return fiyat


df = pd.DataFrame(columns=['urun_adi','URL','min_fiyat','site'])

urun_adi='monitor'
URL = "https://www.hepsiburada.com/dell-ultrasharp-u2722d-27-60hz-5ms-hdmi-display-type-c-qhd-ips-led-monitor-p-HBCV000008PNFZ"
min_fiyat=5000
site="hepsiburada"
df.loc[len(df.index)] = [urun_adi,URL, min_fiyat, site]


urun_adi='monitor'
URL = "https://www.amazon.com.tr/s?k=U2722D&i=computers&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
min_fiyat=5000
site="amazon"
df.loc[len(df.index)] = [urun_adi,URL, min_fiyat, site]


urun_adi='monitor'
URL = "https://www.n11.com/urun/dell-ultrasharp-u2722d-27-8-ms-60-hz-qhd-ips-led-monitor-2019502?magaza=techburada"
min_fiyat=5000
site="n11"
df.loc[len(df.index)] = [urun_adi,URL, min_fiyat, site]


urun_adi='monitor'
URL = "https://www.ciceksepeti.com/arama?query=u2722d%20&qt=u2722d%20&choice=2"
min_fiyat=5000
site="ciceksepeti"
df.loc[len(df.index)] = [urun_adi,URL, min_fiyat, site]

urun_adi='monitor'
URL = "https://www.trendyol.com/sr?q=u2722d%20&qt=u2722d%20&st=u2722d%20&os=1"
site="trendyol"
df.loc[len(df.index)] = [urun_adi,URL, min_fiyat, site]



print(df)
df.to_csv('out.csv') 


#df = pd.read_csv('out.csv')
#belki sonra

donudur=True
while donudur:
    try:
        for index, row in df.iterrows():
            #print(row['c1'], row['c2'])
            URL=row['URL']
            site=row['site']
            min_fiyat=row['min_fiyat']
            
            print(site)
            webpage = requests.get(URL, headers=headers)
            soup = BeautifulSoup(webpage.content, "lxml")
            #print(soup)
            dom = etree.HTML(str(soup))
            
            fiyat=fiyat_getir(dom,site).replace(".", "")
            if int(fiyat)<min_fiyat:
                mail_gonder(urun_adi,site)
                print("Fiyat Düştü")
                #donudur=False
            else:
                print("Fiyat yüksek")
            print("Ürün Fiyatı =", fiyat)
            print('-------------------')
    except AttributeError:
        print('La bunu kim kırdı....')
        
    time.sleep(300) #5dk

