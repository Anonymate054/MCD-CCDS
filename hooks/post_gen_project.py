import fs
from fs import open_fs
from fs.errors import ResourceNotFound

CURRENT_DIR = open_fs(".")
PYSPARK_DIR = "{{ cookiecutter.project_name }}/PySpark"

project_packages = "{{ cookiecutter.project_packages }}"

if project_packages != "BigData":
    try:
        CURRENT_DIR.removetree(PYSPARK_DIR)
    except ResourceNotFound:
        print("Fail to remove directory")