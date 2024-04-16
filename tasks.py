from invoke import task
from subprocess import call
from sys import platform


@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python src/main.py")

@task
def test(ctx):
    ctx.run("poetry run pytest src/tests")

@task
def main(ctx):
    ctx.run("python src/test.py")


@task
def lorem_ipsum(ctx):
    print("Lorem ipsum")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
