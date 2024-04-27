def get_dict_from_dataclass_recursively(object) -> dict:
    from dataclasses import is_dataclass

    object_type = type(object)
    if is_dataclass(object):
        return {
            key: get_dict_from_dataclass_recursively(value)
            for key, value in object.__dict__.items()
        }
    elif object_type is list or object_type is tuple:
        return [
            get_dict_from_dataclass_recursively(value)
            for value in object
        ]
    else:
        return object
