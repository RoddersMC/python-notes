def depth_first_search(root: any, target: any, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        node_found = depth_first_search(child, target, path)

    if node_found is not None:
        return node_found

    return None