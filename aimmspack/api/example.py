
def print_example_file() -> None:
    print(
'''
apiVersion: v1
model:
  name: project             # Project name without the .aimms extension
  path: C:\\...              # Projects full path
  aimmsVersion: 4.79.3.10   # Aimms Version
  arch: x64-VS2017          # [Optional]
  apps:                     # App list
  - name: test              # App Name
    version: 1.0.0          # [Optional] used as app name sufix
    infix: web              # [O]ptional]
  - name: test
    version: 1.0.0
    infix: win
'''
    )