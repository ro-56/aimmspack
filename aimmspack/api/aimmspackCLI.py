from aimmspack._lib.yamlFile import get_contents
from aimmspack._lib.config import process_config
from aimmspack._lib.bash import get_cmd
from aimmspack._lib.aimmspack import create_aimmspack


def aimmspack(filepath: str) -> None:

    config = get_contents(filepath)

    model = process_config(config)

    cmd = get_cmd(model)

    out, err = create_aimmspack(cmd)

    if err:
        print(err)
        return
    
# todo:
# check if file exists



