import alfred


@alfred.command('docker.build', help='workflow to build docker container')
def docker_build():
    """
    construit l'image docker pour l'application

    >>> $ alfred docker:build
    """
    alfred.run('docker build .')
