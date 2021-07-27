from aimmspack.api import debugCLI, aimmspackCLI, example
from argparse import ArgumentParser
import aimmspack

def main():    
    parser = ArgumentParser()
    parser.add_argument('filepath', help='The filepath of the .yaml configuration file')
    parser.add_argument('-ex', '--example', help='Returns an example of the .yaml configuration file')
    # parser.add_argument('-v', '--verbose', action='count', default=0, help='foo help')
    parser.add_argument('-d', '--debug', action='count', default=0, help='debug')

    args = parser.parse_args()

    if args.example:
        example.print_example_file()
        return

    if args.filepath:
        if args.debug:
            debugCLI.test(args.filepath)
            return

        aimmspackCLI.aimmspack(args.filepath)
    else:
        print('ERROR')


