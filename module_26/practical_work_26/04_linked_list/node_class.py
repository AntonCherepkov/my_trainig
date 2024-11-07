from typing import Union, Optional


class Node:
    """The class of the object for storing variables under the specified identifier."""
    
    def __init__(self, data: Optional[Union[int, float]] = None) -> None:
        self.next_id = None
        self.data = data
