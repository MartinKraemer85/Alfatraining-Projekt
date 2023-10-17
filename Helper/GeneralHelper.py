from pydoc import locate


def generate_classinstance(class_name: str, properties: dict) -> any:
    """
    Generates a class instance via dotted path and a dictionary for the properties.

    :param class_name: Class name
    :param properties: Properties
    :return:
    """
    class_ = locate(class_name)
    class_instance = class_()
    class_instance.set_properties(properties)
    return class_instance
