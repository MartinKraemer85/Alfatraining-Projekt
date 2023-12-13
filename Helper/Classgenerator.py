import os
import re
from Helper.GeneralHelper import get_class
from settings import engine


def create_js() -> None:
    """
    Create the js classes for all model classes.

    :return: None
    """
    root_dir = "Model"
    file_list = []

    # iterate the model directories recursive, extract all model files while ignoring the cashed stuff
    for dir_path, dir_name, files in os.walk('Model'):
        for file_name in files:
            if "__init__" in file_name or "ModelBase" in file_name or file_name.endswith(".pyc"):
                continue
            rel_dir = os.path.relpath(dir_path, root_dir)
            rel_file = os.path.join("Model", rel_dir, file_name.replace(".py", ""), file_name.replace(".py", ""))
            file_list.append(rel_file)

    file_list = [re.sub('\\\\', '.', file) for file in file_list]
    for file in file_list:
        # finally emmit the ddl for every model class
        get_class(file).metadata.create_all(engine)




