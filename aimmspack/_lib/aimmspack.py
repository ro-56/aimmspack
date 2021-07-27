from subprocess import PIPE, Popen

def create_aimmspack(cmdList: list[list[str]], decoder: str='utf-8') -> tuple[str, str]:
    for cmd in cmdList:
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
    return output.decode(decoder), error.decode(decoder)