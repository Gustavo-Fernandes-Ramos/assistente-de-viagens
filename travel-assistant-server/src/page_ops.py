import os

class PageOperations():

    def page_exists(resource):
        return os.path.exists('../resources' + resource)

    def get_page(resource):
        try:
            file = open('../resources' + resource)
            content = file.read().encode('utf-8')
            file.close()
            return content
        except IOError:
            return None