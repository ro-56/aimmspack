from aimmspack._lib.config import ModelConfig
from pathlib import Path

def get_cmd(model: ModelConfig) -> list[list[str]]:
    """Returns a list of bash commands for app creation"""

    cmd: list[list[str]] = []
    
    for app in model.apps:
        cmd.append([
                f'{Path.home()}\\AppData\\Local\\AIMMS\\IFA\\Aimms\\{model.aimmsVersion}-{model.arch}\\Bin\\aimms.exe',
                f'{model.get_aimms_model_path()}',
                f'--hidden',
                f'--export-to',
                f'{Path.cwd()}\\{app.get_export_name()}'
            ])
    
    return cmd
