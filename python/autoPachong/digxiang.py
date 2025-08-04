import os
import random
import re
import csv
import shutil
import time
import urllib.request
import urllib.parse


def getHTMLText():# 1.手动获得京东搜索页面源代码，并读取内容返回
    try:
        url = 'https://search.jd.com/Search?keyword=python%E7%B3%BB%E5%88%97%E4%B8%9B%E4%B9%A6&enc=utf-8&wq=python%E7%B3%BB%E5%88%97%E4%B8%9B%E4%B9%A6&pvid=0014cc1992e049f8a1fa7320b62dd053'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'Cookie': '__jdu=17049731372361461162252; shshshfpa=f0267f10-1464-3077-3a54-fb5ac399bc23-1704973138; shshshfpx=f0267f10-1464-3077-3a54-fb5ac399bc23-1704973138; pinId=ypXfuKS3uuZ8D0EMFRbTfbV9-x-f3wj7; pin=jd_6adee5f09ef53; unick=%E8%90%8C%E7%8B%BC%E8%B5%AB%E8%90%9D%E9%85%B1w; _tp=nFoh9PX3moGpoCXYxe4%2B8LyF%2FAp90YBRaWi3QDsoFR0%3D; _pst=jd_6adee5f09ef53; __jdv=95931165|direct|-|none|-|1715040270769; wlfstk_smdl=q8dy1neeo4n8c13splrpvi1jqjebv0hl; TrackID=1Om9PKRkJXcu5P38Tk5Wul3EUMqfi2ecDMh1hJv_r7msipVbx8TfWqecMNZQ_M379NQoeTVGvgRLKfrkfDDMApQp3sET0qAwaTijHWasbpbIsPDnv2SO8YInQ1j-nUmdM; thor=A10332664F8193D1456D686D4FA52C8410BDDB9BD49561D3432CDE1DDF31F5F239116A94F084E8D8969B26C99FE91014C7FAE53CF3C585B2FFFECF67EEDDB6774639F6F49CC62857803B41D204E2CE043C9B342576BD5380F33F6D4390981298CFDC5FCCAE59A93A83678FCA926DEED8112A3BFC504B8A07B79FB8779E0C2629B64072CB12E4136890CDD434D2003D4BA98F80A1CAE1338FDCDCEA186D3743E8; flash=2_Qat6wTkvlJO3mSsGrtepy_hHz8Y69ABGc8v17Io00UVQjiN-6ARU_wJn46L6Yi76ZmO0_O4HjTRulRw6XA0Ud0NCrBBUYgzHD4tgnwRNT7Yv8vQITHmFvCnxY_w-uqSMhkE-sZ-6AXQzvl5iGw4ZEO5OJ1g-bwU2on6F3u4aUqN*; ceshi3.com=201; ipLoc-djd=27-2376-0-0; jsavif=1; shshshfpb=BApXc24xXU-pA0NEA5iPew4idki14Xw35BkbWNhd59xJ1Mu_ogoO2; __jda=143920055.17049731372361461162252.1704973137.1712624881.1715040271.6; __jdc=143920055; areaId=27; 3AB9D23F7A4B3CSS=jdd03JD5YWLIEMEQGGE4ZDRI73TY33K2OU34MP4GX6BQHHLNQGRAVIEVXMBDHQI4LCX3GPLK22EY7H23HUONJ2ETP5IUTOIAAAAMPKBP7VCIAAAAACQ5LLXPZZAZ4YAX; _gia_d=1; 3AB9D23F7A4B3C9B=JD5YWLIEMEQGGE4ZDRI73TY33K2OU34MP4GX6BQHHLNQGRAVIEVXMBDHQI4LCX3GPLK22EY7H23HUONJ2ETP5IUTOI; __jdb=143920055.6.17049731372361461162252|6.1715040271'
        }
        res = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(res)
        html = response.read().decode()
        with open('search.html', 'w+', encoding='utf-8') as fp:
            fp.write(html)
        return  html
    except Exception as err:
        print(err)
        return ""

def parsePage(goodsListInfo, html):# 2.通过正则，字符串等方法，提取商品的价格和商品名称
    try:
        '<img width="220" height="220" data-img="1" data-lazy-img="//img10.360buyimg.com/n7/jfs/t1/219374/22/38781/125985/66061d4cFd0239f90/a90cd7a9abc64a33.jpg" />'
        prices = re.findall(r'<em>￥</em><i data-price="\d+">(\d+.\d+)</i>',html)
        # print(prices)
        titles = re.findall(r'<em>(.+?)<font class="skcolor_ljg">(.+?)</font>(.+?)</em>',html)
        # print(titles)
        imgUrls = re.findall('<img width="220" height="220" data-img="1" data-lazy-img="(//.+.jpg).avif"',html)
        # print(imgUrls)
        for i in range(len(prices)):
            price = prices[i]
            titles2 = titles[i][2].replace('<font class="skcolor_ljg">','')
            titles2 = titles2.replace('</font>', '')
            title = titles[i][0] + titles[i][1] + titles2
            imgUrl = 'https:' + imgUrls[i]
            goodsListInfo.append([price , title, imgUrl])
    except:
        print("")

def printGoodsList(goodsListInfo):# 3.输出商品信息到控制台
    print("{:4}\t{:8}\t{:60}\t{:16}".format("序号", "价格", "商品名称", "图片地址"))
    count = 0
    # print(goodsListInfo)
    for g in goodsListInfo:
        print("{:4}\t{:8}\t{:60}".format(count+1, g[0], g[1]), g[2])
        count = count + 1

def saveGoodsInfoToCsvFile(goodsListInfo):# 4.保存商品信息到csv文件
    header = ["序号", "价格", "商品名称", "图片地址"]
    data = []
    for i, g in enumerate(goodsListInfo):
        data.append((i+1,g[0],g[1],g[2]))
    with open('searchlist.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(data)

def creadDir(desc):
    if not os.path.exists('searchPicture-{0}'.format(desc)):
        os.mkdir('searchPicture-{0}'.format(desc))
    else:
        shutil.rmtree('searchPicture-{0}'.format(desc))
        os.mkdir('searchPicture-{0}'.format(desc))

def saveImgsToDir(goodsListInfo, desc):
    creadDir('re')
    for g in goodsListInfo:  # 列表循环
        try:
            print('downloading：{}'.format(g[2]))
            res = urllib.request.urlopen(g[2])
            time.sleep(random.randint(1, 2))
            imgInfo = res.read()
            with open('./searchPicture-{0}/'.format(desc) + str(g[2]).split('/')[-1], 'wb') as fp:
                fp.write(imgInfo)
        except:
             continue
    print('all-{0}：'.format(desc), len(goodsListInfo))



def main():# 通过main函数把几个步骤串联起来，完成整个功能
    # 定义存放商品信息的列表
    goodsListInfo = []
    try:
        html = getHTMLText()
        parsePage(goodsListInfo, html)
        printGoodsList(goodsListInfo)
        saveGoodsInfoToCsvFile(goodsListInfo)
        saveImgsToDir(goodsListInfo, 're')
    except Exception as err:
        print(err)

#程序入口函数
main()