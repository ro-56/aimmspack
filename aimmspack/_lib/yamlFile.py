from pathlib import Path
from yaml import safe_load

def get_file_extension(filename: str) -> str:
    """Returns the file extension"""

    fileExtension = filename[filename.rfind("."):len(filename)]
    return fileExtension

def ensure_yaml_file(filename: str, raiseError: bool=False) -> bool:
    """Verifies if the file has the '.yaml' or '.yml' extension. Raises an Error if raiseError is True"""

    fileExtension = get_file_extension(filename)
    if not ((fileExtension == '.yaml')
            or (fileExtension == '.yml')):
        if raiseError:
            raise Exception("File must have the extension '.yaml' or '.yml'")
        return False
    return True

def get_yaml_contents(yamlFile: str) -> dict:
    """Returns the contents of the yaml file as a dict"""

    with open(yamlFile, 'r') as stream:
        return safe_load(stream)

def get_contents(filename: str) -> dict:
    """Returns the contents of the yaml file as a dict after passing basic validation"""

    file = Path(filename)
    filePath = str(file.absolute())
    if not file.exists():
        raise Exception('The file specified does not exists')

    ensure_yaml_file(filePath, True)

    return get_yaml_contents(filePath)
