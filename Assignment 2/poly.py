class point:
    def __init__(self, x: float=None, y: float=None):
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        # Validator to check if point has valid numeric coordinates
        val = False
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            val = True
        return val

    def __str__(self):
        # Point (x, y) expressed as string
        return "({0}, {1})".format(self.__x, self.__y)

class Polygon:
    def __init__(self):
        # Initialize polygon with default values and head node
        self.__sides = 0
        self.__vertices = 0
        self.__head = point()  # Head node for linked list

    def add_point(self, x: float, y: float):
        # Add a point to the polygon using circular linked list
        new_point = point(x, y)
        if not new_point.valid():
            return
        
        if self.__vertices == 0:
            # First point
            self.__head.next = new_point
            new_point.next = new_point
        else:
            # Find the last point in the linked list
            curr_point = self.__head.next
            while curr_point.next != self.__head.next:
                curr_point = curr_point.next
            
            # Insert new point
            curr_point.next = new_point
            # Point back to first node
            new_point.next = self.__head.next  
        
        self.__vertices += 1
        self.__sides += 1

    def __str__(self):
        if self.__vertices == 0:
            return "Empty polygon"
        
        text = ""
        # Start from first point
        curr_point = self.__head.next 
        first_point = curr_point
        
        # Traverse the circular list once
        text += str(curr_point)
        curr_point = curr_point.next
        while curr_point != first_point:
            text += " -> " + str(curr_point)
            curr_point = curr_point.next
        
        return text
