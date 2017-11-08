# scrapy-notes

I noticed that there are some bug since some website has changed its method to defence crawls. So I try to start some project from scratch. So use tutorial as begin. 

ps: tutorial is a init project in https://github.com/scrapy


Tutorial:

init the project use ` scrapy startproject tutorial [project_dir]` 

enter the project and I got a directory named tutorial and a cfg postfix file.

so I could both enther the tutorial directory or just use command line tool run spider in the outside directory. Noticed that once I enter ` -o output.json` or other output file format, I should check the directory where I was input command.


Command:

    Scrapy X.Y - no active project

    Usage:
    scrapy <command> [options] [args]

    Available commands:
    crawl         Run a spider
    fetch         Fetch a URL using the Scrapy downloader
    [...]


Global command:

    startproject
    genspider
    settings
    runspider
    shell
    fetch
    view
    version

    # project only command below:
    cralw
    check
    list
    edit
    parse
    bench


+ genspider

生成爬虫

    scrapy genspider [-t template] <name> <domain>

    # needed project, create a spider in current directory. and the domain aggr is use to generate allowed_domains and start_urls spider properties.

    # e.g.
    $ scrapy genspider -l
    Available templates:
    basic
    crawl
    csvfeed
    xmlfeed

    $ scrapy genspider example example.com
    Created spider 'example' using template 'basic'

    $ scrapy genspider -t crawl scrapyorg scrapy.org
    Created spider 'scrapyorg' using template 'crawl'


    # create a new spider
    scrapy gensipder mydomain mydomain.com

+ crawl
    
    scrapy crawl [quotes|author] -o output.jl [-a tag=humor]
    # start the crawl

+ check

    scrapy check [-l] <spider>

    # looks like this 
    $ scrapy check -l
    first_spider
    * parse
    * parse_item
    second_spider
    * parse
    * parse_item

    $ scrapy check
    [FAILED] first_spider:parse_item
    >>> 'RetailPricex' field is missing

    [FAILED] first_spider:parse
    >>> Returned 92 requests, expected 0..4

+ scrapy list 

show all the availiable spider in a list

+ `scrapy edit <spider>`

use default editor to edit the spdier 

+ `scrapy fetch <url>`

use scrapy default downloader fetch url, and output content as standard output.

This command can be used to USER_AGENT to set agent

so I could use fetch to check some specific pages.

--spider = SPIDER : use special spider not spider autocheck
--headers: print http header not body
- -no-redirect: not follow the HTTP 3XX redirection, while default is jsut follow them.

    $ scrapy fetch --nolog http://www.example.com/some/page.html
    [ ... html content here ... ]

    $ scrapy fetch --nolog --headers http://www.example.com/
    {'Accept-Ranges': ['bytes'],
    'Age': ['1263   '],
    'Connection': ['close     '],
    'Content-Length': ['596'],
    'Content-Type': ['text/html; charset=UTF-8'],
    'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
    'Etag': ['"573c1-254-48c9c87349680"'],
    'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
    'Server': ['Apache/2.2.3 (CentOS)']}

+ scrapy view <url>

+ scrapy shell [url]

--spider = SPIDER
-c code
--not-redirect 

    $ scrapy shell http://www.example.com/some/page.html
    [ ... scrapy shell starts ... ]

    $ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
    (200, 'http://www.example.com/')

    # shell follows HTTP redirects by default
    $ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
    (200, 'http://example.com/')

    # you can disable this with --no-redirect
    # (only for the URL passed as command line argument)
    $ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
    (302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')


爬虫流程：
+ 首先生成抓取第一个URL的初始 request，request 下载完成后生成 response ，然后指定对 response 要使用的回调函数。
+ 通过调用 start_requests() 方法（默认情况下）为 start_urls 中指定的URL生成初始的 Request 以及将 parse 方法作为请求的回调函数。
+ 在回调函数中，您将解析 Response（网页）并返回带有提取的数据的 dict，Item对象，Request 对象或这些对象的可迭代容器。这些请求还将包含回调（可能是相同的），然后由 Scrapy 下载，然后由指定的回调处理它们的响应。
+ 在回调函数中，您通常使用 选择器 来解析页面内容（但您也可以使用BeautifulSoup，lxml或您喜欢的任何解析器），并使用解析的数据生成 Item。
+ 最后，从爬虫返回的 Item 通常将持久存储到数据库（在某些 Item Pipeline 中）或使用 Feed导出 写入文件。