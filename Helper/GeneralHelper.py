from pydoc import locate


def generate_classinstance(class_path: str, properties: dict = None) -> any:
    """
    Generates a class instance via dotted path and a dictionary for the properties.
    The class can be generated with properties or empty.

    :param class_path: Class name
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


def get_class(class_path: str) -> object:
    return locate(class_path)
