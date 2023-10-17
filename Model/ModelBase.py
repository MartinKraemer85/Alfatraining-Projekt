from dataclasses import dataclass, field, asdict


@dataclass()
class ModelBase:
    # TODO: Tu es!

    def generate_classinstance(self, name: str, properties: dict) -> any:
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

    def set_properties(self, properties: dict) -> None:
        """
        Set the properties of an instance via dictionary

        :param properties: Dictionary of properties
        :return: None
        """
        pass
