from pydoc import locate
import string
import random


def generate_classinstance(class_path: str, properties: dict = None) -> any:
    """
    | Generates a class instance via dotted path and a dictionary for the properties.
    | The class can be generated with properties or empty.

    :param class_path: Class path, i.e. Model.Vinyl.Record.Record
    :param properties: Properties
    :return: any
    """
    class_ = locate(class_path)
    try:
        class_instance = class_()
    except TypeError:
        return object()

    if properties:
        class_instance.set_properties(properties)

    return class_instance


def get_class(class_path: str) -> any:
    """
    Get the class by path.

    :param class_path: Class path, i.e. Model.Vinyl.Record.Record
    :return: The class
    """
    return locate(class_path)


def create_pwd() -> str:
    """
    | Generates a pwd with the length of 12.
    | Contains 3 letter / upper letter, digits and punctuations.

    :return: pwd string
    """
    pwd = []
    for i in range(0, 3):
        pwd.append(random.choice(string.digits))
        pwd.append(random.choice(string.ascii_letters.lower()))
        pwd.append(random.choice(string.ascii_letters.upper()))
        pwd.append(random.choice(string.punctuation))
    random.shuffle(pwd)
    return "".join(pwd)
