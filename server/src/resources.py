from enum import Enum
import os

class ResourceController():

    CT_TYPE_DICT = {".jpeg" : "image/jpeg", 
            ".jpg" : "image/jpeg",
            ".png" : "image/png",
            ".svg" : "image/svg+xml",
            ".html" : "text/html",
            ".css" : "text/css",
            ".js" : "application/javascript"}

    def file_exists(file_path):
        return os.path.exists(file_path)

    def ext_exists(file: str):
        base_name, file_ext = os.path.splitext(file)
        if file_ext in ResourceController.CT_TYPE_DICT:
            return True
        else:
            return False

    def get_ct_type(file: str):
        base_name, file_ext = os.path.splitext(file)
        if file_ext in ResourceController.CT_TYPE_DICT:
            return ResourceController.CT_TYPE_DICT[file_ext]
        else:
            return None
