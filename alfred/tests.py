import alfred


@alfred.command('tests', help='workflow to execute all automatic tests')
def tests():
    """
    execute tests with unittests

    >>> $ alfred tests
    """
    alfred.run('pytest tests/units')
