from invoke import task # pylint: disable=import-error

@task
def test(ctx):
    "Run pytests"
    ctx.run("pytest src")

@task
def coverage(ctx):
    "Run tests with coverage"
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    "Generate coverage report"
    ctx.run("coverage html")

@task
def lint(ctx):
    "Run pylint"
    ctx.run("pylint src")