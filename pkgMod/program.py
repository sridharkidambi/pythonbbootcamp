from file1 import myfuncprogram
from mainpkg import mainfile
from mainpkg.subpkg import subfile

myfuncprogram('Sridhar Kidambi')
subfile.subpack()

def progfunc():
    print('i am being run now on being called.')

if __name__ =='__main__':
    print('this is run directly')
else:
    print(' PROGRAM -> iam being called by someone')
