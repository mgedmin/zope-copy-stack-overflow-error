import argparse

import zope.copy
from persistent import Persistent
from zope.container.btree import BTreeContainer
from zope.container.contained import Contained


class SimpleItem(Persistent, Contained):
    pass


def main():
    parser = argparse.ArgumentParser(description="reproduce a zope.copy bug")
    parser.add_argument("n", type=int, nargs='?', default=8000,
                        help="number of items (default: {default})")
    args = parser.parse_args()
    obj = BTreeContainer()
    for n in range(args.n):
        obj[str(n)] = SimpleItem(obj)
    zope.copy.clone(obj)
    print(f"{len(obj)} items: success!")


if __name__ == "__main__":
    main()
