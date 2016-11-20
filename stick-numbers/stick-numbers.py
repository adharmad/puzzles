# stick-numbers.py
import sys

# usage
def usage(argv):
    if len(argv) < 2:
        print("Usage: ./stick-numbers.py <NUMBER>")
        sys.exit(0)


# entry point
def main(argv):
    usage(argv)

    # check if the argument is a number
    try:
        num = float(argv[1])
    except ValueError:
        print("Input argument %s is not a number" % argv[0])
        sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
