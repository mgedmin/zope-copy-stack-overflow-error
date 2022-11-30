import argparse

import zope.copy
from zope.container.btree import BTreeContainer


def main():
    parser = argparse.ArgumentParser(description="reproduce a zope.copy bug")
    parser.add_argument("n", type=int, nargs='?', default=8000,
                        help="number of items (default: {default})")
    args = parser.parse_args()
    obj = BTreeContainer()
    for n in range(args.n):
        obj[str(n)] = None
    zope.copy.clone(obj)
    print(f"{len(obj)} items: success!")


if __name__ == "__main__":
    main()
