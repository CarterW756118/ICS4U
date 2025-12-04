class point:
    def __init__(self, x: float=None, y: float=None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    def valid(self):
        val = False
        if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
            val = True
        return val

    def __str__(self):
        # point (x, y) expressed this way as string
        return "({0}, {1})".format(self.__x, self.__y)

class Polygon:
    def __init__(self):
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = point() # a null point with a null Next field

    def add_point(self, x: float, y: float):
        new_point = point(x, y)
        if not new_point.valid():
            return
        curr_point = self.__head
        while curr_point.next != None:
            curr_point = curr_point.next
        curr_point.next = point(x, y)
        self.__vertices += 1
        self.__sides += 1
        

    def __str__(self):
        text = ""
        curr_point = self.__head
        while curr_point.next != None:
            text += str(curr_point.next)
            curr_point = curr_point.next
            if curr_point.next != None:
                text += " -> "
        return text
