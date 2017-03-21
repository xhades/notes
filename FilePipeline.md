# 模块说明
> 代码依赖`Python2.7` `Ubuntu16.04`环境，其他版本不保证兼容。以下是个人使用过程中的总结，也希望小伙伴在使用过程中可以在下方编辑区提出issues
## 基本配置
- 在`items.py`中添加`file_urls=Field()`用于存储附件下载链接列表
- 在`settings.py`中通过字段`FILES_STORE`自定义附件下载路径，比如`FILES_STORE = '/home/xhades/Desktop/tmp'`
- `spider.py`中启动下载附件`pipelines` ,指定`pipeline` 执行优先级

```python
class NoticeSpider(CrawlSpider):
    handle_httpstatus_list = [302]
    name = 'people'
    custom_settings = {'ITEM_PIPELINES': { 'huanggang_huanping.files.FilesPipeline': 200,
        'huanggang_huanping.pipelines.HuanggangHuanpingPipeline': 300
        }
        }
```
## 如何调用
- 把源码中`files.py`添加到项目中
- 修改`files.py`中的方法  
    - 自定义下载附件文件名
    - 重写`scrapy`方法`get_media_requests()`,`file_path()`
    ```python
    class FilesPipeline(FilesPipeline):
        """
        Override by xhades
        Date: 2017.3.21
        Version: 0.1
        """
        ### Overridable Interface        
        def get_media_requests(self, item, info):
            for file_urls in item['file_urls']:
                yield scrapy.Request(file_urls, meta={'item': item})
        
        def file_path(self, request, response=None, info=None):
            ## start of deprecation warning block (can be removed in the future)
            def _warn():
                from scrapy.exceptions import ScrapyDeprecationWarning
                import warnings
                warnings.warn('FilesPipeline.file_key(url) method is deprecated, please use '
                              'file_path(request, response=None, info=None) instead',
                              category=ScrapyDeprecationWarning, stacklevel=1)
    
            # check if called from file_key with url as first argument
            if not isinstance(request, Request):
                _warn()
                url = request
            else:
                url = request.url
    
            # detect if file_key() method has been overridden
            if not hasattr(self.file_key, '_base'):
                _warn()
                return self.file_key(url)
            ## end of deprecation warning block
    
            # def ur file name rule  title_projectname_media_guid
            # override by xhades
            try:
                item = request.meta['item']
            except Exception, e:
                item = ''
    
            if item:
                media_guid = request.url.split('/')[-1]
                new_filename = u"{}_{}".format(item['title'].replace("/", u"每"), media_guid)
            else:
                media_guid = hashlib.sha1(to_bytes(url)).hexdigest()
    
                new_filename = u"{}".format(media_guid)
            # change to request.url after deprecation
            return '%s/%s' % (item['module_type'], new_filename)
            
    ```
- 举个栗子在`spider.py`中的使用
```python
    def parse_construct_host(self, response):
        logging.info(u"=======开始采集数据==========")
        #
        bs_body = BeautifulSoup(response.body, 'html5lib').get_text()
        if response.xpath(self.fieldset_xpath).extract():
            item = HuanggangHuanpingItem()
            for a_item in item.fields:
                item[a_item] = ''
            file_urls_list = []
            for href in response.xpath("//fieldset//tr/td[2]/a/@href").extract():
                file_url = urljoin('http://www.hghb.gov.cn/', href)
                file_urls_list.append(file_url)
            item['title'] = ''.join(response.xpath(self.title_xpath).extract())
            item['release_time'] = re.findall('\d{4}-\d{2}-\d{2}', ''.join(response.xpath(self.release_time_xpath).xpath("string(.)").extract()))[0]
            item['secondary_url'] = response.url
            item['module_type'] = "attachments"
            item['file_urls'] = file_urls_list
            item['file_name'] = ''.join(response.xpath("//fieldset//tr/td[2]/a/@title").extract())

            # yield item

```
## 拓展
- `FilesPipeline`支持自定义文件过期时间，以及异常处理机制，这里只是简单处理一下附件名修改问题，之后在使用过程中希望大家能多提issues