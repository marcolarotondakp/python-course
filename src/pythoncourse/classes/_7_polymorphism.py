import json
import yaml
import xmltodict
from abc import ABC, abstractmethod

from pathlib import Path
from typing_extensions import Any


class Reader(ABC):
    @abstractmethod
    def read(self) -> dict[str, Any]:
        pass

    @staticmethod
    def from_file_name(name: str):
        with open(name) as file:
            content = file.read()
        if name.endswith(".json"):
            return JsonReader(content)
        elif name.endswith(".yaml"):
            return YamlReader(content)
        elif name.endswith(".xml"):
            return XmlReader(content)
        else:
            raise Exception(f"unable to determine reader for file {name}")

    def __init__(self, content) -> None:
        self.content = content


class JsonReader(Reader):
    def read(self) -> dict[str, Any]:
        return json.loads(self.content)


class YamlReader(Reader):
    def read(self) -> dict[str, Any]:
        return yaml.safe_load(self.content)


class XmlReader(Reader):
    def read(self) -> dict[str, Any]:
        return xmltodict.parse(self.content)["root"]


if __name__ == "__main__":
    base_path = (
        Path.cwd()
        .joinpath("..")
        .joinpath("..")
        .joinpath("..")
        .joinpath("resources")
        .joinpath("pythoncourse")
        .joinpath("classes")
    )
    files = ["data.json", "data.yaml", "data.xml"]
    for f in files:
        path = base_path.joinpath(f)
        reader: Reader = Reader.from_file_name(str(path))
        d: dict[str, Any] = reader.read()
        print(type(reader))
        print(d)
