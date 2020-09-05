"""Start situation for Not-Logged-Code."""
import random
import time


def main():
    """Do some instable magic indefinetly and hope nothing breaks."""
    cycle = 0
    while True:

        print(f"{time.time()} - Start cycle {cycle}")
        do_unstable_magick(cycle)
        print(f"{time.time()} -  Finished cycle {cycle}")
        time.sleep(5)


def do_unstable_magick(counter: int):

    x = random.random()
    print(x)
    x -= counter / 10000
    if x <0.0001:
        raise EnvironmentError("Something went wrong")
    elif x <0.5:
        print("Cycle {counter} was unsuccessful")
    else:
        print("Cycle {counter} was unsuccessful")


if __name__ == '__main__':
    main()
