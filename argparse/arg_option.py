import argparse

if __name__ == '__main__':
    print("enter main")
    parser = argparse.ArgumentParser(description='demo for agrparse')
    parser.add_argument('--check', dest="check", action="store_const", const=True, default=False)
    args = parser.parse_args()
    if args.check:
        print("check is True")
    else:
        print("check is not False")
