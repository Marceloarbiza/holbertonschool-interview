#!/usr/bin/python3
""" Lockboxes """

from hmac import compare_digest


def canUnlockAll(boxes):
    """
    Something here
    """
    listAux = boxes[0]
    for idx in listAux:
        for b in boxes[idx]:
            # if b not in listAux:
            if b not in listAux:
                listAux.append(b)

    liCompare = []
    for x in range(0, len(boxes)):
        liCompare.append(x)

    print(liCompare)
    listAux.sort()

    if listAux == liCompare:
        return True
    return False
