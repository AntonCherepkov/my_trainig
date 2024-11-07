from __future__ import annotations
from typing import Union
from node_class import Node


class LinkedListIteration:
    """Linked list iterator class"""
    def __init__(self, node_cls: Node) -> None:
        self.__first_node = node_cls

    def __iter__(self):
        return self

    def __next__(self):
        if self.__first_node is None:
            raise StopIteration
        else:
            data = self.__first_node.data
            self.__first_node = self.__first_node.next_id
            return data
