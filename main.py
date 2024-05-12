from webServer import web_server_cgi


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    web_server_cgi.start_httpd("0.0.0.0", "8888", app=)
