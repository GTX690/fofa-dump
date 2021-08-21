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
