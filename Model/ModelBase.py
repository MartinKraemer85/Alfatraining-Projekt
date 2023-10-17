from dataclasses import dataclass, field, asdict
from Helper.GeneralHelper import generate_classinstance

@dataclass()
class ModelBase:
    # TODO: Tu es!

    def set_properties(self, properties: dict) -> None:
        """
        Set the properties of an instance via dictionary

        :param properties: Dictionary of properties
        :return: None
        """
        pass
