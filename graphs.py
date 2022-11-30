import pickle
import objgraph
from BTrees.OOBTree import OOBTree


def main():
    tree = OOBTree({str(n): None for n in range(100)})
    objgraph.show_refs(tree, filter=lambda x: not isinstance(x, (type, str, type(None))), too_many=100, filename='hundred-nodes.svg')
    tree = OOBTree({str(n): None for n in range(1000)})
    objgraph.show_refs(tree, filter=lambda x: not isinstance(x, (type, str, type(None))), too_many=100, filename='thousand-nodes.svg')
    tree = OOBTree({str(n): None for n in range(8000)})
    pickle.dumps(tree)  # this will raise


if __name__ == "__main__":
    main()
