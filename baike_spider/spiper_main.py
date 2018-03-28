# coding:utf8
import url_manager, html_downloader, html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloder()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    
    def craw(self, root_url):
        count = 1 #记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()#取一个出来
                print 'craw %d : %s' %(count, new_url)
                html_cont = self.downloader.download(new_url)#下载对应的页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)#页面解析
                self.urls.add_new_urls(new_urls) #添加了变量的new_url上面是set new——url
                self.outputer.collect_data(new_data)#收集数据
                
                if count >= 1000:
                    break
                count += 1
            except Exception as e:
                print(str(e))
                print 'craw failed'
            
            self.outputer.output_html()


if __name__ == "__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
    