# -*- coding: utf-8 -*-
from __future__ import print_function

import base64
import hashlib
import hmac
import ssl
from datetime import datetime as pydatetime

try:
    from urllib import urlencode

    # from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


# def ToBase64(file):
#     with open(file, 'rb') as fileObj:
#         image_data = fileObj.read()
#         return base64.b64encode(image_data)


def analyze(file):
    # 云市场分配的密钥Id
    secretId = "AKID5Zt5dn9gc1Irrvzuxnk8I5Y8b6K7IIA6mTVd"
    # 云市场分配的密钥Key
    secretKey = "a0VnKOuEky9cl1VjV0HNcx58Q5H2281CuOJ6Sgqd"
    source = "market"

    # 签名
    datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    signStr = "x-date: %s\nx-source: %s" % (datetime, source)
    sign = base64.b64encode(hmac.new(secretKey.encode(
        'utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
    auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (
        secretId, sign.decode('utf-8'))

    # 请求方法
    method = 'POST'
    # 请求头
    headers = {
        'X-Source': source,
        'X-Date': datetime,
        'Authorization': auth,

    }
    # 查询参数
    queryParams = {
    }

    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64.b64encode(image_data)

    # body参数（POST方法下存在）
    bodyParams = {
        "number": "",
        "pri_id": "ne",
        "v_pic": base64.b64encode(image_data)}
    # url参数拼接
    url = 'http://service-98wvmcga-1256810135.ap-guangzhou.apigateway.myqcloud.com/release/yzm'
    if len(queryParams.keys()) > 0:
        url = url + '?' + urlencode(queryParams)

    request = Request(url, headers=headers)
    request.get_method = lambda: method
    if method in ('POST', 'PUT', 'PATCH'):
        request.data = urlencode(bodyParams).encode('utf-8')
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urlopen(request, context=ctx)
    content = response.read()
    if content:
        vcode = eval(content.decode('utf-8'))
        # print(vcode['v_code'])
        return vcode['v_code']

# analyze(r'tmp\verification_img.png')
