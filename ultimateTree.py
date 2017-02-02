observedObjects = set()


def ultimateTree(objectIn, depth=float('inf')):
    global observedObjects
    tree = {}

    if depth == 0:
        return None

    for element in dir(objectIn):
        if depth <= 0:
            return None

        if element in observedObjects:
            tree[element] = None

        else:
            observedObjects.add(element)
            tree[element] = ultimateTree(getattr(objectIn, element), depth-1)

    return tree

