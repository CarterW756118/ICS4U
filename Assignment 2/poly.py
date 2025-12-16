"""
Author : Carter Wells
Student Number : 756118
Course : ICS4U
Revision Date : 15 December 2025
Program : Polygon Linked List
Description : Defines classes to represent points and polygons using
              a circular linked list structure.
VARIABLE DICTIONARY :
    __x : float - X coordinate of a point
    __y : float - Y coordinate of a point
    next : point - Reference to the next point in the linked list
    __sides : int - Number of sides in the polygon
    __vertices : int - Number of vertices in the polygon
    __head : point - Head node for the circular linked list
"""

# Class to represent a single point
class point:
    """
    Constructor for a point
    Parameters:
        x (float): X coordinate
        y (float): Y coordinate
    """
    def __init__(self, x: float = None, y: float = None):
        self.__x = x
        self.__y = y
        # Pointer to the next point in the linked list
        self.next = None

    """
    Function to validate that the point has numeric coordinates
    Returns:
        bool: True if x and y are numeric, otherwise False
    Variables:
        val : bool - Validation result
    """
    def valid(self):
        val = False

        # Check that both coordinates are integers or floats
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            val = True

        return val

    """
    Function to return a string representation of the point
    Returns:
        str: Point formatted as (x, y)
    """
    def __str__(self):
        # Format the point for printing
        return "({0}, {1})".format(self.__x, self.__y)


# Class to represent a polygon using a circular linked list
class Polygon:
    """
    Constructor for the Polygon class
    Initializes an empty polygon
    """
    def __init__(self):
        self.__sides = 0
        self.__vertices = 0
        # Head node for the linked list
        self.__head = point()

    """
    Function to add a point to the polygon
    Parameters:
        x (float): X coordinate of the point
        y (float): Y coordinate of the point
    Variables:
        new_point : point - New point object to add
        curr_point : point - Current point in traversal
    """
    def add_point(self, x: float, y: float):
        # Create a new point object
        new_point = point(x, y)

        # Validate the new point before adding
        if not new_point.valid():
            return

        # Head points to the new point if this is the first vertex in the polygon
        if self.__vertices == 0:
            self.__head.next = new_point

            # New point points to itself
            new_point.next = new_point
        else:
            # Start traversal at the first point
            curr_point = self.__head.next

            # Move to the last point in the circular linked list
            while curr_point.next != self.__head.next:
                curr_point = curr_point.next

            # Insert the new point at the end
            curr_point.next = new_point

            # New point loops back to the first point
            new_point.next = self.__head.next

        # Increase the vertex and side counters
        self.__vertices += 1
        self.__sides += 1

    """
    Function to return a string representation of the polygon
    Returns:
        str: List of points connected by arrows
    Variables:
        text : str - String being built
        curr_point : point - Current point in traversal
        first_point : point - Reference to first point in linked list
    """
    def __str__(self):
        # Handle case where polygon has no vertices/points
        if self.__vertices == 0:
            return "Empty polygon"

        text = ""

        # Start at the first point
        curr_point = self.__head.next
        first_point = curr_point

        # Add the first point to the output string
        text += str(curr_point)

        # Move to the next point
        curr_point = curr_point.next

        # Traverse the circular list until returning to the start
        while curr_point != first_point:
            text += " -> " + str(curr_point)
            curr_point = curr_point.next

        # Return the completed string
        return text
