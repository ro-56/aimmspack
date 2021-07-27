from aimmspack._lib.yamlFile import get_contents
from aimmspack._lib.config import process_config
from aimmspack._lib.bash import get_cmd


def test(filepath: str) -> None:

    config = get_contents(filepath)

    model = process_config(config)

    cmd = get_cmd(model)

    print(cmd)