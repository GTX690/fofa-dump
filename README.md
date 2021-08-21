# fofa-dump
调用fofa api下载数据工具，将获取到的数据保存为csv文件。

支持批量查询，多个字段导出，以及控制每页导出的数量。

# 使用方法
1、在config.py中配置fofa邮箱和key。

2、在fofa_query.txt中输入需要查询的语句，一句一行。

config.py
```
# fofa email
FOFA_EMAIL = ''
# fofa key
FOFA_KEY = ''
# 可选参数】字段列表，默认为host，用逗号分隔多个参数，如(fields=ip,title)。可选的列表有：host title ip domain port country province city country_name header server protocol banner cert isp as_number as_organization latitude longitude structinfo  icp。注意：country是国家代码，例如CN, country_name是国家名称；structinfo仅限企业会员调用
FOFA_FIELDS = 'host,ip,title,port,city,country,server,isp,latitude,longitude'
# 每次查询返回记录数，默认为100条，最大可设置为10000条。注：body字段包含内容较多，建议每次获取≤100条
FOFA_SIZE = 10000
# 导出查询结果文件名
FOFA_OUTPUT_FILE = 'fofa_results.csv'
# 需要查询的fofa语句文件名
FOFA_READ_FILE = 'fofa_query.txt'

```
最终获取到的数据如下显示：
![image](https://user-images.githubusercontent.com/38800368/130309468-a6fb6c8e-e7a2-4e91-b509-ffbe552071c9.png)



注：高级会员只能查询前10000条，普通会员只能前100条。

例如你要查询如下内容：

fofa_query.txt
```
domain="qq.com"
title="腾讯"
```
如果你是高级会员就只能获取到domain="qq.com"的前一万条和title="腾讯"的前一万条。

如果你是普通会员就只能获取到domain="qq.com"的前100条和title="腾讯"的前100条。
