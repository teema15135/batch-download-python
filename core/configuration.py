import json

ALLOWED_MIME_TYPE_KEY = "allowed_mimetype"
CONFIGURATION_FILENAME = "config.json"

DEFAULT_MIME_TYPES = ["image/png", "image/jpeg"]

CONFIGURATION_PROPERTY_KEY = "configuration"
module_property = {}


def get_property(key):
    return module_property[key]


def set_property(key, value):
    module_property[key] = value


def has_property(key):
    return key in module_property.keys()


def get_configuration():
    if not has_configuration():
        _load_configuration_file()
    return get_property(CONFIGURATION_PROPERTY_KEY)


def set_configuration(configuration):
    set_property(CONFIGURATION_PROPERTY_KEY, configuration)


def has_configuration():
    return has_property(CONFIGURATION_PROPERTY_KEY)


def _load_configuration_file():
    """Read config json file and return json configuration"""
    with open(CONFIGURATION_FILENAME) as json_file:
        set_configuration(json.load(json_file))


def get_allowed_mimetype():
    return get_configuration()[ALLOWED_MIME_TYPE_KEY]
