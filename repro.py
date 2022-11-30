import zope.copy
from zope.container.btree import BTreeContainer


N_ITEMS = 8000


def test_clone_large_btree_container():
    obj = BTreeContainer()
    for n in range(N_ITEMS):
        obj[str(n)] = None
    zope.copy.clone(obj)


if __name__ == "__main__":
    test_clone_large_btree_container()
