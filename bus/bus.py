class Bus:
    """
    A class to represent a bus.
    """

    def __init__(self, bus_id, capacity, model):
        """
        Constructs all the necessary attributes for the bus object.

        Args:
            bus_id (str): The unique identifier for the bus.
            capacity (int): The seating capacity of the bus.
            model (str): The model of the bus.

        Raises
            ValueError: If bus_id is not a string, capacity is not an integer, or model is not a string.
        """
        if not isinstance(bus_id, str):
            raise ValueError("bus_id must be a string")
        if not isinstance(capacity, int):
            raise ValueError("capacity must be an integer")
        if not isinstance(model, str):
            raise ValueError("model must be a string")
        
        self.__bus_id = bus_id
        self.__capacity = capacity
        self.__model = model

    @property
    def bus_id(self):
        """
        To Do: Add a docstring.
        """
        return self.__bus_id

    @property
    def capacity(self):
        """
        Returns the capacity.
        Returns:
            int: the capacity of the bus instance.
        """
        return self.__capacity

    @property
    def model(self):
        """
        Returns the model.
        Returns:
            str: the model of the bus instance.
        """

        return self.__model

    def __str__(self):
        """
        To do: Add a docstring.
        """
        return f"Bus ID: {self.__bus_id}, Capacity: {self.__capacity}, Model: {self.__model}"
