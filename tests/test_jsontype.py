import pytest

type Primitive = str | int | float | bool | None
type Json = Primitive | list[Json] | dict[str, Json]
type JsonObject = dict[str, Json]
type JsonArray = list[Json]


@pytest.mark.filterwarnings("error:.*")
def test_jsontype() -> None:
    obj: Json = {
        "my": "object",
        "deep": {
            "nested": "object",
            "A": [1, 2, 3]
        }
    }
    assert obj["my"] == "object"
