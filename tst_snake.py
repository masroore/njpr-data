import re

_UNDER_SCORE_1 = re.compile(r"([^_])([A-Z][a-z]+)")
_UNDER_SCORE_2 = re.compile("([a-z0-9])([A-Z])")


def cs(txt: str) -> str:
    subbed = _UNDER_SCORE_1.sub(r"\1_\2", txt)
    subbed = re.sub(r"(\W)", r"_\1", subbed)
    return _UNDER_SCORE_2.sub(r"\1_\2", subbed).lower()


def ss(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("__([A-Z])", r"_\1", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()


def us(word: str) -> str:
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", word)
    word = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", word)
    # word = word.replace("-", "_")
    # #word = re.sub(r'\s+', '_', word)
    return word.lower()


def cc(camel_input):
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", camel_input)
    return "_".join(map(str.lower, words))


test_strings = [
    "CamelCase",
    "camelCamelCase",
    "Camel1Camel2Case",
    "getHTTPResponseCode",
    "get200HTTPResponseCode",
    "getHTTP200ResponseCode",
    "HTTPResponseCode",
    "ResponseHTTP",
    "ResponseHTTP2",
    "Fun?!awesome",
    "Fun?!Awesome",
    "10CoolDudes",
    "20coolDudes",
    "TAX RATE",
    "tax-rates",
    "GLOBAL2-ITEMS(3)",
]
for test_string in test_strings:
    print(test_string)
    print(cs(test_string))
    print(ss(test_string))
    print(us(test_string))
    print(cc(test_string))
    print("---")
