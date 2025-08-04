import os
import random
import shutil
import time
import urllib.request
from lxml import etree
import csv

# 1.手动获得京东搜索页面源代码，并读取内容返回
def getHTMLText():
    try:
        url = 'https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Cookie': 'unpl=JF8EAJhnNSttUBgHVR4HHhdEHg5SWw9fSUcAOzcBV1QKTQcHSAITRhZ7XlVdWBRKFR9sZBRXXVNIXQ4eAysSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-SVxRWFULShIAZmcBZG1bS2QFGjIcFRRJWlJZWwl7FjNoVzVkVVlLUQMSMhoiEXsfAAJaAUoWCmoqAlNZWkxSAh0DKxMgSA; __jdv=76161171|baidu-search|t_262767352_baidusearch|cpc|304792042815_0_9bba4444edb74cf3a2ea528c7b3b19e7|1711114121265; __jdu=665367670; areaId=27; PCSYCityID=CN_610000_610100_0; shshshfpa=83c9d4f4-713b-328f-b794-15939dfeae98-1711114123; shshshfpx=83c9d4f4-713b-328f-b794-15939dfeae98-1711114123; pinId=NIukwSMcIYLepA-Um876lbV9-x-f3wj7; pin=jd_549fd53d56462; unick=jd_181921fyz; _tp=ZglR7fC%2FsM66sNwju7HTLFH5z4wsyC%2B8jP6wjrk7Dvw%3D; _pst=jd_549fd53d56462; ipLoc-djd=27-2376-50232-53749; mt_xid=V2_52007VwQVVl9fVF0ZSClVBWUGFFJbWE4JHEAZQABjCkFODVxVCgMZTAwNYVAaV1haVVgvShhfAHsCEE5eUENbFkIaXQ5nAiJQbVhiUxtIGFkAbwcVVFVRV10bSBBYAFcGE1tb; wlfstk_smdl=nijjbn468lbcdvso6etutc84x16t9isx; TrackID=1_VlHyKhOwNnaeuM5HhUWI73SKi54T7pgt8mLfhWY3N7_hIv5KSAasvfc3FRoecyYnX4ZFllZXIcIqsJ6Cxdx1i7eqYnUNn5G3bXtgg3-a2Q; thor=419E28C0E8FB9C3195A8644472302C63CE420B4B0632D8494478A29D47700430E0D58357D6E88766FF30BC4CC2B91495B83D2C04AFD2E52BE15F95E9790209F163E27770D39963C1BB074F142F957308CAAC65493F803DDB574C2E0D0F9C8120CE96B6A64B187FC4C10C94F7C4E64FF17216750D96AEC8DF116B8734D5C0305862850EF3956D1BA9B6D3B19409073827114F28AF76E779B5940A368A10FEF2B0; flash=2_FisQhWqmgkR1ptmeouuOn_-PvJfdnEln3N3H5RHB9Zeue74ST4qwn-zhXqYNn7lA3nlhAcx5YEMiT7b1Q9YEpClT1oDujmaUestnxYKVYHN*; ceshi3.com=203; jsavif=1; __jda=143920055.665367670.1711114120.1711670892.1711676193.16; __jdc=143920055; shshshfpb=BApXeoVLUhOtAP3rkg3zcOwVdfOQmOB9CBlNQRgxl9xJ1MgdPHoC2; 3AB9D23F7A4B3C9B=SBIIZUXGB3YKRCXK3AG23LA7YDXCBBCST5VAY2EBKGNRNBKZTE5VBLR6J7RCRUQJRXUQNY7KK3MUXGJLRL3RZDGRIU; joyya=1711676192.1711676435.25.1nb98pl; __jdb=143920055.8.665367670|16.1711676193; 3AB9D23F7A4B3CSS=jdd03SBIIZUXGB3YKRCXK3AG23LA7YDXCBBCST5VAY2EBKGNRNBKZTE5VBLR6J7RCRUQJRXUQNY7KK3MUXGJLRL3RZDGRIUAAAAMOQ7PHIVYAAAAAD3KXIJAUPZJ5IQX; _gia_d=1'
        }
        res = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(res)
        html = response.read().decode()
        with open('京东书包搜索.html', 'w+', encoding='utf-8') as fp:
            fp.write(html)
        return html
    except Exception as err:
        print(err)
        return ""
# 2.通过Xpath等方法，提取商品的价格和商品名称
def parsePage(goodsListInfo, html):
    try:
        selector = etree.HTML(getHTMLText())
        # <em>￥</em><i data-price="100010372895">688.00</i>
        #//*[@id="J_goodsList"]/ul/li/div/div[3]/strong/i
        prices = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/strong/i/text()')
        # print(len(prices))
        # <em> Gmt for kids儿童<font class ="skcolor_ljg"> 书包 </font> 小学生超轻护脊大容量抗菌礼物1-4年级女寻梦独角兽22L </em>
        firstStr = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/em/text()[1]')
        secondStr = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/em/font/text()')
        thirdStr = selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[4]/a/em/text()[2]')
        imgUrls= selector.xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a/img/@data-lazy-img')
        # print(len(imgUrls))
        # print(firstStr)
        # print(secondStr)
        # print(thirdStr)
        # print(len(imgUrls))
        for i in range(30):
            price = prices[i]
            title = firstStr[i] + secondStr[i] + thirdStr[i]
            imgUrl = 'https:' + imgUrls[i]
            goodsListInfo.append([price , title, imgUrl[0:-5]])
    except:
        print("")
 # 3.输出商品信息到控制台
def printGoodsList(goodsListInfo):
    print("{:4}\t{:8}\t{:60}\t{:16}".format("序号", "价格", "商品名称", "图片地址"))
    count = 0
    # print(goodsListInfo)
    for g in goodsListInfo:
        print("{:4}\t{:8}\t{:60}".format(count+1, g[0], g[1]), g[2])
        count = count + 1

# 4.保存商品信息到csv文件
def saveGoodsInfoToCsvFile(goodsListInfo):
    header = ["序号", "价格", "商品名称", "图片地址"]
    data = []
    for i, g in enumerate(goodsListInfo):
        data.append((i+1,g[0],g[1],g[2]))
    with open('Xpath-京东商品搜索信息列表.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(data)

def creadDir(desc):
    if not os.path.exists('京东搜索页面图片-{0}'.format(desc)):
        os.mkdir('京东搜索页面图片-{0}'.format(desc))
    else:
        shutil.rmtree('京东搜索页面图片-{0}'.format(desc))
        os.mkdir('京东搜索页面图片-{0}'.format(desc))

def saveImgsToDir(goodsListInfo, desc):
    creadDir('Xpath')
    for g in goodsListInfo:  # 列表循环
        try:
            print('正在下载：{}'.format(g[2]))
            # urlretrieve(url,local)方法根据图片的url将图片保存到本机
            urllib.request.urlretrieve(g[2],'./京东搜索页面图片-{0}/{1}'.format(desc,str(g[2]).split('/')[-1]))
            time.sleep(random.randint(1,2))
        except:
             continue
    print('下载图片总数-{0}：'.format(desc), len(goodsListInfo))


# 通过main函数把几个步骤串联起来，完成整个功能
def main():
    #定义存放商品信息的列表
    goodsListInfo = []
    try:
        html = getHTMLText()
        parsePage(goodsListInfo, html)
        printGoodsList(goodsListInfo)
        saveGoodsInfoToCsvFile(goodsListInfo)
        saveImgsToDir(goodsListInfo, 'Xpath')
    except Exception as err:
        print(err)

# 程序入口函数
main()