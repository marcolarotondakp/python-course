from _7_polymorphism import Reader
from abc import abstractmethod, ABC
from typing_extensions import Dict, Any, Sequence, override


class Validator(ABC):
    @abstractmethod
    def validate(self, data: Dict[str, Any]) -> bool:
        pass


class RequiredFieldsValidator(Validator):
    def __init__(self, required_fields: list[str]):
        self.required_fields = required_fields

    @override
    def validate(self, data: Dict[str, Any]) -> bool:
        missing = [field for field in self.required_fields if field not in data]
        if missing:
            raise ValueError(f"Missing following fields: {missing}")
        return True


class MinLengthValidator(Validator):
    def __init__(self, min_keys: int = 1):
        self.min_keys = min_keys

    @override
    def validate(self, data: Dict[str, Any]) -> bool:
        if len(data) < self.min_keys:
            raise ValueError(
                f"Found {len(data)} keys, but at least {self.min_keys} are required"
            )
        return True


class NoEmptyValidator(Validator):
    @override
    def validate(self, data: Dict[str, Any]) -> bool:
        empty_keys = [k for k, v in data.items() if not v]
        if empty_keys:
            raise ValueError(f"Empty value for: {empty_keys}")
        return True


class DataPipeline:
    def __init__(self, reader: Reader, validators: Sequence[Validator]) -> None:
        self.reader: Reader = reader
        self.validators: Sequence[Validator] = validators

    def load(self) -> Dict[str, Any]:
        data = self.reader.read()
        for v in self.validators:
            v.validate(data)
        return data


if __name__ == "__main__":
    base_path = "/Users/marcolarotonda/Development/kube-academy/python-course/resources/pythoncourse/classes/"
    for f in ["data.json", "data.xml", "data.yaml"]:
        v: list[Validator] = [
            MinLengthValidator(min_keys=2),
            NoEmptyValidator(),
        ]
        if f.endswith(".json"):
            v.append(
                RequiredFieldsValidator(["key1", "key2"]),
            )
        pipeline = DataPipeline(Reader.from_file_name(base_path + f), v)
        d = pipeline.load()
        print(d)
