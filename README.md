## 说明

```
1. 支持动态更新 从服务端 向 客户端实时下发 然后替换
    1. 不在承接 crawlapi安排车任务  
    2. crawlapi仅承接 crawlet和scrapy的爬虫任务
    3. crawl-agent是一个三位一体的全方位AI爬虫框架
2. 一个客户端只有一个爬虫
3. 承接 windows-agent android-aegnt chrome-agent
4. 进接收 执行 上报状态  不在客户端进行任何锁操作  所有的操作均在 crawl-agent进行
5. 插件管理
6. 整合AI能力
```