
def snake_to_camel(text1: str) -> str:
    """Converts a snake_case string to camelCase."""
    words = text1.lower().split("_")
    result = []
    for word in words:
        if word == "":
            continue
        result.append(word)
            
    return result[0] + "".join(res.capitalize() for res in result[1:])

def camel_to_snake(text2: str) -> str:
    """Converts a camelCase string to snake_case."""
    converted = []
    for word in text2:
        if word.isupper():
            converted.append("_")
            converted.append(word.lower())
        else:
            converted.append(word)
    return "".join(converted)

def snake_to_pascal(text3: str) -> str:
    """Converts a snake_case string to PascalCase."""
    words = text3.lower().split("_")
    convert = []
    for word in words:
        if word == "":
            continue
        convert.append(word.capitalize())
    
    return "".join(convert)

def to_kebab(text4: str) -> str:
    """Converts a string to kebab-case."""
    return text4.lower().replace(" ", "-")

def to_title_case(text5: str) -> str:
    """Converts a string to Title Case."""
    words = text5.split()
    return " ".join(word.capitalize() for word in words)


text1 = snake_to_camel("hello_world_foo")
text2 = camel_to_snake("helloWorldFoo")
text3 = snake_to_pascal("hello_world")
text4 = to_kebab("Hello World Foo")
text5 = to_title_case("the quick brown fox")

print(f"Snake to Camel: {text1}")
print(f"Camel to Snake: {text2}")
print(f"Snake to Pascal: {text3}")
print(f"To Kebab: {text4}")
print(f"To Title Case: {text5}")



