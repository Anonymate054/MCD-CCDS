from fs import open_fs
from fs.errors import ResourceNotFound

project_packages = "{{ cookiecutter.project_packages }}"

pyspark_path = "{{ cookiecutter.project_name }}/PySpark"

with open_fs('.') as fs:
    if project_packages != "BigData":
        try:
            fs.remove_dir(pyspark_path)
        except ResourceNotFound:
            pass