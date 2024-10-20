import fs

CURRENT_DIR = fs.open_fs(".")
PYSPARK_DIR = CURRENT_DIR.getsyspath("notebooks/PySpark")
PYSPARK_DIR = "notebooks/PySpark"

project_packages = "{{ cookiecutter.project_packages }}"

if project_packages != "BigData":
    try:
        CURRENT_DIR.removetree(PYSPARK_DIR)
    except Exception as e: 
        print("Fail to remove directory", e)