def app(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    file_name = environ.get('PATH_INFO', '/')[1:] or 'index.html'
    HTML_ROOT_DIR = '../views/'
    print("file path:", HTML_ROOT_DIR + file_name)

    try:
        with open(HTML_ROOT_DIR + file_name, "rb") as file:
            file_data = file.read()
    except IOError:
        response = "The file is not found!"
    else:
        response = file_data.decode("utf-8")

    return [response.encode('utf-8')]