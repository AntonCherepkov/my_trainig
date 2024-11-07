from __future__ import annotations
from node_class import Node
from typing import Optional, Union, Iterator
from linkedlistiterator_class import LinkedListIteration


class LinkedList:
    """Implementation class of a singly linked list"""
    def __init__(self) -> None:
        self.__first_node = None
        # self.__iter_node = None
    
    def get_first_node(self) -> Union[Node, None]:
        """A function that returne a hidden head element"""     
        return self.__first_node
    
    def set_first_node(self, node_cls: Node) -> None:
        """
        A method that sets the hidden head element

        :param node_cls: the first element of the linked list (the head)
        :type node_cls: Node
        """
        self.__first_node = node_cls

    def append(self, user_num: Optional[Union[int, float]] = None) -> None:
        """
        A method for adding an item to a linked list

        :param user_num: user values to embed in a linked list
        :type user_num: Union[int, float]
        """
        new_node = Node(user_num)
        if self.get_first_node() is None:
            self.set_first_node(new_node)
        else:
            cur_node = self.get_first_node()
            while cur_node.next_id:
                cur_node = cur_node.next_id    
            cur_node.next_id = new_node
    
    def show_linklist(self) -> None:
        """A method for displaying the entire linked list"""
        cur_node = self.get_first_node()
        
        print('[', end='')
        while True:
            print(f'{cur_node.data}', end=' ')
            cur_node = cur_node.next_id
            if cur_node.next_id is None:
                print(f'{cur_node.data}', end='')
                break
        print(']')
    
    def get(self, num_elem: int) -> Union[int, float, None]:
        """
        Method for returning an item from a linked list

        :param num_elem: index of the returned element
        :type num_elem: Union[int, float]
        :return: the value embedded in the specified object (by index)
        :rtype: Union[int, float, None]
        """
        count_iter = 0
        cur_node = self.get_first_node()

        while count_iter <= num_elem:
            if count_iter == num_elem:
                return cur_node.data
            elif cur_node.next_id is None:
                return None                
            else:
                cur_node = cur_node.next_id
                count_iter += 1

    def remove(self, num_elem: int) -> Union[int, float, None]:
        """
        Method for deleted an element by index

        :param num_elem: the position of the item in the list
        :type num_elem: int
        :return: the value that was saved in the deleted object
        :rtype: Union[int, float, None]
        """
        count_iter = 0
        del_elem = None
        cur_node = self.get_first_node()

        while True:
            if cur_node.next_id is not None:
                sup_node = cur_node.next_id
                if count_iter == 0 and count_iter == num_elem:
                    del_elem = cur_node.data
                    self.set_first_node(sup_node)
                elif count_iter == num_elem - 1:
                    if sup_node.next_id is not None:
                        del_elem = sup_node.data
                        cur_node.next_id = sup_node.next_id
                    else:
                        del_elem = sup_node.data
                        cur_node.next_id = None
                else:
                    cur_node = cur_node.next_id
                count_iter += 1
            else:
                break

        return del_elem

    # def __iter__(self) -> Iterator:
    #     """Linked list iterator"""
    #     self.__iter_node = self.get_first_node()
    #     return self

    # def __next__(self) -> Union[int, float]:
    #     if self.__iter_node is None:
    #         raise StopIteration
    #     else:
    #         data = self.__iter_node.data
    #         self.__iter_node = self.__iter_node.next_id
    #         return data

    def __iter__(self):
        return LinkedListIteration(self.get_first_node())
