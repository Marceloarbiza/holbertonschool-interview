#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Iterate over a list of boxes with keys inside.
    Each box may contain keys to other boxes, a key
    with the same number as the index of a box can
    open that box. Determine if all boxes can be opened.
    def canUnlockAll(boxes):

    if len(boxes) <= 1:
        return True

    listAux = boxes[0]
    for idx in listAux:
        if boxes[idx] == []:
            listAux.append(0)
        for b in boxes[idx]:

            if b not in listAux:
                listAux.append(b)

    liCompare = []
    for x in range(0, len(boxes)):
        liCompare.append(x)
    listAux.sort()
    if listAux == liCompare:
        return True
    return False
    """
    if len(boxes) <= 1:
        return True

    pending_boxes = [0]
    opened_boxes = set(pending_boxes)

    while pending_boxes:
        current = pending_boxes.pop()
        for key in boxes[current]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                pending_boxes.append(key)

    return len(opened_boxes) == len(boxes)
