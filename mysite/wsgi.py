"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# It's a simple application to test WSGI.
# def application(environ, start_response):
#     status = '200 OK'
#     output = '''
# <head>
# <meta charset="utf-8">
# <title>一个非常棒的网页</title>
# <link rel="shortcut icon" href="/static/favicon.ico">
# </head>

# <body>
# <h2>你好，妈妈。</h2>
# <br/>
# <p>如果你能完好地看见这个页面，说明我是一个编程天才。</p>
# <hr/>
# <p>请与网站的所有者核对密码:90814<p/>
# <br/> <br/>
# <p style="text-align:center">如果发现bug, 请<a href="mailto:howardqiuhao@qq.com">联系程序员</a>。</p>
# <body/>
# '''
#     output = bytes(output, 'utf-8')

#     response_headers = [('Content-type', 'text/html'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)

#     return [output]