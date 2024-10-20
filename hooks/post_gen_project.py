import fs
from fs import open_fs
from fs.errors import ResourceNotFound

CURRENT_DIR = open_fs(".")
print(CURRENT_DIR)
PYSPARK_DIR = CURRENT_DIR.getsyspath("notebooks/PySpark")
print(PYSPARK_DIR)

project_packages = "{{ cookiecutter.project_packages }}"


if project_packages != "BigData":
    try:
        CURRENT_DIR.removetree(PYSPARK_DIR)
    except ResourceNotFound:
        print("Fail to remove directory")