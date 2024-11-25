from route.route import Route


class TransitSystem:
    """
    A class to represent a transit system.
    """

    def __init__(self, name):
        """
        Constructs all the necessary attributes for the transit system object.

        Args:
            name (str): The name of the transit system.

        Raises:
            ValueError: If name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        
        self.__name = name
        self.__routes = []

    @property
    def name(self):
        """
        Returns the value of the private `__name` attribute, 
        which represents the name of the object.

        Returns:
            str: The name of the object.
        """   
        
        return self.__name

    @property
    def routes(self):
        """
        Returns a list of routes in the transit system.
        Returns:
            str: list of routes in the transit system instance.
        """
        return self.__routes

    def add_route(self, route):
        """
        Adds a route to the transit system.

        Args:
            route (Route): The route to be added to the transit system.
        """
        if not isinstance(route, Route):
            raise ValueError("route must be an instance of Route")
        
        self.__routes.append(route)

    def __str__(self):
        """
        Returns a string representation of the transit system.

        Returns
            str: A string containing the transit system's details.
        """
        route_details = ', '.join(str(route) for route in self.__routes)
        return f"Transit System: {self.__name}, Routes: [{route_details}]"