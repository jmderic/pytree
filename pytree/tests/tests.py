import os

from pytree.__main__ import main

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

if __name__=="__main__":
    main()
