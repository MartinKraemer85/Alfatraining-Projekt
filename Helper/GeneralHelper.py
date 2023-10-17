from Model.Vinyl.Record import Record
from Model.Vinyl.Track import Track


def generate_classinstance(name: str, properties: dict) -> any:
    """
    Generates a class instance via name and dictionary for the values.

    :param name: Class name
    :param properties: Properties
    :return:
    """
    reference = globals()[name]
    instance = reference()
    instance.set_properties(properties)
    return instance
