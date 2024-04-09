from invoke import task
from subprocess import call
from sys import platform


@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python src/index.py", pty=True)

@task
def main(ctx):
    ctx.run("python src/main.py")


@task
def lorem_ipsum(ctx):
    print("Lorem ipsum")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))
