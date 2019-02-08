import monocle
from monocle import _o
from monocle.script_util import run
from monocle.util import sleep


@_o
def print_every_second():
    for i in range(5):
        print("1")
        yield sleep(1)


@_o
def print_every_two_seconds():
    for i in range(5):
        print("2")
        yield sleep(2)


@_o
def example():
    monocle.launch(print_every_second)
    monocle.launch(print_every_two_seconds)


run(example)
