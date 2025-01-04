import alfred

@alfred.command("lint", help="check type consistency on source code")
def lint():
    """
    check the code source

    >>> $ alfred lint
    """
    alfred.invoke_command('lint.ruff')
    alfred.invoke_command('lint.mypy')

@alfred.command("lint.mypy", help="check type consistency on source code")
def lint_mypy():
    """
    check the type consistency with mypy

    >>> $ alfred lint
    """
    alfred.run("mypy src tests")

@alfred.command("lint.ruff", help="check source code using ruff")
@alfred.option("--fix", help="apply fixes to resolve lint violations.", is_flag=True)
def lint_ruff(fix: bool):
    """
    check source code using ruff

    >>> $ alfred lint.ruff
    """
    if fix:
        alfred.run("ruff check --fix src tests")
    else:
        alfred.run("ruff check src tests")

