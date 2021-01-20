import sys
import pathlib

# Run the configuration script when the user runs 
# python3 -m project [init, config, or configure]

here = pathlib.Path(__file__).parent.resolve()


if (len(sys.argv) > 1) and (sys.argv[1] in ['init', 'initialize', 'config', 'configure']):
    print('Running the configuration script.')
    # Mission data dir
    s = (f'What is the mission data directory?')
    DATA_DIR = input(s)
    
    # Check that the DATA_DIR directory exists
    if not pathlib.Path(DATA_DIR).exists():
        raise OSError(f'The "{DATA_DIR}" directory does not exist. Exiting.')
    
    with open(pathlib.Path(here, 'config.py'), 'w') as f:
        f.write('import pathlib\n\n')
        f.write(f'DATA_DIR = pathlib.Path("{DATA_DIR}")\n')
        f.write(f'PROJECT_DIR = pathlib.Path("{here}")')

else:
    print('This is a configuration script to set up config.py file. The config '
        'file will contain the DATA_DIR data directory, and the base project '
        'directory (here). To get the prompt after this package is installed, run '
        'python3 -m project init')
