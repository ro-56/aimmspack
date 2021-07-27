from typing import Optional
from pathlib import Path
from pydantic import BaseModel

class AppConfig(BaseModel):
    name: str
    version: Optional[str] = ''
    infix: Optional[str] = ''

    def get_export_name(self):
        """Returns the final compiled app name with the .aimmspack extension"""

        appName: str
        if self.version and self.infix:
            appName = f'{self.name}_{self.infix}_{self.version}'
        elif self.version:
            appName = f'{self.name}_{self.version}'
        elif self.infix:
            appName = f'{self.name}_{self.infix}'
        else:
            appName = f'{self.name}'
        return f'{appName}.aimmspack'

class ModelConfig(BaseModel):
    aimmsVersion: str
    arch: Optional[str] = 'x64-VS2017' 
    path: Path
    name: str
    apps: list[AppConfig]

    def get_aimms_model(self):
        """Returns the aimms model name with the .aimms extension"""
        return f'{self.name}.aimms'
    
    def get_aimms_model_path(self):
        """Returns the full aimms model path with model name"""

        return f'{self.path}\\{self.get_aimms_model()}'

def process_config(configDict: dict) -> ModelConfig:
    """Process the configuration for the model and returns a model object"""

    return ModelConfig(**configDict['model'])
