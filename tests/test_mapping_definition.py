import pytest
from library.transliterator.mapping import MappingDefinition

def test_initialization():
    source = {"key": "value"}
    definition = MappingDefinition(source)
    assert definition.source == source
    assert definition.name == ""
    
def test_invalid_name():
    with pytest.raises(ValueError) as exc:
        definition = MappingDefinition({})
        definition.parse()
    assert str(exc.value) == ": Missing mapping attribute name"
    
def test_empty_name():
    with pytest.raises(ValueError) as exc:
        definition = MappingDefinition({"name": ""})
        definition.parse()
    assert str(exc.value) == ": Mapping name should not be empty"

def test_invalid_mapping():
    with pytest.raises(ValueError) as exc:
        definition = MappingDefinition({"name": "invalid_data"})
        definition.parse()
    assert str(exc.value) == "invalid_data: Missing mapping attribute mapping"
    
def test_empty_mapping():
    definition = MappingDefinition({"name": "test", "mapping": {}})
    definition.parse()
    assert definition.mapping == {}

def test_parse_mapping():
    definition = MappingDefinition(
        {
            "name": "language_mapping",
            "mapping": {
                "ė": "é"
            },
            "orthography_rules": [
                "regex_string"
            ]
        }
    )
    definition.parse()
    assert definition.name == "language_mapping"
    assert definition.mapping == {"ė": "é"}
    assert definition.orthography_rules == ["regex_string"]





