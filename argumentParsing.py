import argparse 

parser=argparse.ArgumentParser(
    description='''This is a python script to generate help file''',
    epilog="""The help file is generated.Enjoy!""")

parser.add_argument('--firstArg',type=str,default='first',help='Defaults to first.Mandarory field to enter the reptype')

args=parser.parse_args()



