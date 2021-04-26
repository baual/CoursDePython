import argparse

parser = argparse.ArgumentParser(description='Is the worl flat ? true or false')
parser.add_argument('Param',
                    help='a string to know if the world is flat or not : true or false')


args = parser.parse_args()

the_world_is_flat = args.Param
if the_world_is_flat=='true':
    print("Be careful not to fall off!")
else:
    print("good guy :-)")
