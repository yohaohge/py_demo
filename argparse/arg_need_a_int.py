import argparse

if __name__ == '__main__':
    print("enter main")
    parser = argparse.ArgumentParser(description='demo for agrparse')
    parser.add_argument('integer', type=int, help='a int arg')
    args = parser.parse_args()
    print("get a int arg {}".format(args.integer))
