#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
        return result
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        if len(tuple_a) == 1 and len(tuple_b) > 1:
            result = ((tuple_a[0] + tuple_b[0]), (0 + tuple_b[1]))
            return result
        elif len(tuple_a) > 1 and len(tuple_b) == 1:
            result = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
            return result
        elif len(tuple_a) == 0 and len(tuple_b) > 1:
            result = ((0 + tuple_b[0]), (0 + tuple_b[1]))
            return result
        elif len(tuple_a) > 1 and len(tuple_b) == 0:
            result = ((tuple_a[0] + 0), (tuple_a[1] + 0))
            return result
        elif len(tuple_a) == 0 and len(tuple_b) == 1:
            result = ((0 + tuple_b[0]), (0 + 0))
            return result
        elif len(tuple_a) == 1 and len(tuple_b) == 0:
            result = ((tuple_a[0] + 0), (0 + 0))
            return result
        elif len(tuple_a) == 0 and len(tuple_b) == 0:
            result = ((0), (0))
            return result
        else:
            result = ((tuple_a[0] + tuple_b[0]), (0 + 0))
            return result
