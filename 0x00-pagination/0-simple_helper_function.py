#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


def index_range(page: int, page_size: int) -> tuple:
    """method that retunm start index and end index of a list"""
    offset = (page - 1) * page_size
    dataset = offset + page_size

    return (offset, dataset)
