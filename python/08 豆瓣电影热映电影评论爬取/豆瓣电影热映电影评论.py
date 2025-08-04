import os
import random
import shutil
import time
import requests
from bs4 import BeautifulSoup

# 1.获取主页网页源代码
def getHomePageHTMLText():
    try:
        url = 'https://movie.douban.com/'
        # 构造请求头，进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        with open('豆瓣主页.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
        return response.text
    except Exception as err:
        return ""
# 2.解析网页主页源代码,获取目标数据
def parseHomePage(movieListInfo, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        ############BeautifulSoup-select###############
        aTags = soup.select('.ui-slide-item .poster a')
        imgTags = soup.select('.ui-slide-item .poster a img')
        movieName = []
        hrefs = []
        for tag in aTags:
            if tag['href']:
                # print(tag['href'])
                hrefs.append(tag['href'])
        for img in imgTags:
            if img['alt']:
                # print(img['alt'])
                movieName.append(img['alt'])
        movieListInfo = list(zip(movieName, hrefs))
        # print('BeautifulSoup-select', len(movieListInfo))
        #############BeautifulSoup-find_all############
        # aTags = soup.find_all('li',class_='poster')
        # movieListInfo = []
        # movieName = []
        # hrefs = []
        # for tag in aTags:
        #     # print(tag.contents)
        #     hrefs.append(tag.contents[1].get('href',''))
        #     movieName.append(tag.contents[1].img.get('alt',''))
        # # print(hrefs)
        # movieListInfo = list(zip(movieName, hrefs))
        # # for i in movieListInfo:
        # #     print(i)
        # # print('BeautifulSoup-find_all',len(movieListInfo))
        # #####################end########################
        return movieListInfo
    except:
        return movieListInfo
# 3.获取电影详情页网页源代码
def getDetailPageHTMLText(url):
    try:
        # 构造请求头，进行UA伪装
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        'https://movie.douban.com/subject/36151692/?from=showing'
        'https://movie.douban.com/subject/36151692/comments?start=0&limit=100&status=P&sort=new_score'
        url = '/'.join((url.split('/')[:-1])) + '/comments?start=0&limit=100&status=P&sort=new_score'
        # print(url)
        response = requests.get(url, headers=headers)
        time.sleep(random.randint(1,2))
        return response.text
    except Exception as err:
        return ""
# 4.解析详情页网页源代码,获取目标数据
def parseDetailPage(detailHtml):
    soup = BeautifulSoup(detailHtml, 'html.parser')
    tags = soup.find_all('span', class_='short')
    comment = []
    for tag in tags:
        if tag.string:
            comment.append(tag.string)
    return comment
# 5.保存评论信息到txt文件
def saveCommentsToTxtFile(csvFileName, comments,indexMovie):
    try:
        with open(f'豆瓣电影评论/{csvFileName}.txt','a+',encoding='utf-8') as fp:
            for index, comment in enumerate(comments):
                fp.write(str(index + 1)+'. ')
                fp.write(str(comment))
                fp.write('\n')
            print(f'{indexMovie+1}. 正在写《{csvFileName}》的评论！')
    except Exception as err:
        print(err)
# 6.保存评论到对应电影文件中
def saveMoviesComments(movieListInfo):
    comment = []
    try:
        for indexMovie, movie in enumerate(movieListInfo):
            detailHtml = getDetailPageHTMLText(movie[1])
            comments = parseDetailPage(detailHtml)
            saveCommentsToTxtFile(movie[0],comments, indexMovie)
        print('------over评论保存完毕,热映电影{}个------'.format(len(movieListInfo)))
    except Exception as err:
        return comment


# 5.创建本地文件夹
def creadDir():
    saveDir = '豆瓣电影评论'
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    else:
        shutil.rmtree(saveDir)
        os.mkdir(saveDir)
    return saveDir

# 通过main函数把几个步骤串联起来，完成整个功能
def main():
    # 定义存放电影和评论的列表
    movieListInfo = []
    try:
        creadDir()
        html = getHomePageHTMLText()
        movieListInfo = parseHomePage(movieListInfo, html)
        saveMoviesComments(movieListInfo)
    except Exception as err:
        print(err)

#程序入口函数
main()