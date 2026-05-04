import alfred


@alfred.command('start', help='execute the application')
def start():
    """
    execute the application

    >>> $ alfred run
    """
    alfred.run('python src/app/main.py')
