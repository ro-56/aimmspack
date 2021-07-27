from aimmspack.api import debugCLI, aimmspackCLI, example
from argparse import ArgumentParser

def main():    
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest='mode')
    
    parser_build = subparsers.add_parser('build', help='Builds the application defined in a configuration file')
    parser_build.add_argument('filepath', help='The filepath of the configuration file')
    parser_build.add_argument('-d', '--debug', action='store_true')
    group_opt = parser_build.add_mutually_exclusive_group()
    group_opt.add_argument('-v', '--verbose', action='store_true')
    group_opt.add_argument('-q', '--quiet', action='store_true')

    parser_example = subparsers.add_parser('example', help='Returns an example of the .yaml configuration file')

    args = parser.parse_args()


    if args.mode == 'example':
        example.print_example_file()
        return

    if args.mode == 'build':
        if args.filepath:
            if args.debug:
                debugCLI.test(args.filepath)
                return

            aimmspackCLI.aimmspack(args.filepath)
    
    print('ERROR')
