# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:04:16 2021.

Creating a Circle and a Point Class. The Circle has a Point.

@author: Tindi.Sommers
"""
class Point:
    """Class Point with x and y coordinates"""
    def __init__(self, x, y):
        """Initialize x and y coordinates"""
        self.x = x
        self.y = y
    
    @property
    def x(self):
        """Return the x coordinate of a point"""
        return self.__x
    
    @x.setter
    def x(self, x):
        """set the property __x to x"""
        self.__x = x

    @property
    def y(self):
        """Return the x coordinate of a point"""
        return self.__y
    
    @y.setter
    def y(self, y):
        """set the property __y to y"""
        self.__y = y
        
    
    def move(self, new_x, new_y):
        """Move the point to a new location"""
        self.x = new_x
        self.y = new_y
    
    def __repr__(self):
        """Return a string representation of a point"""
        return f'Point(x={self.x}, y={self.y})'
    
    def __str__(self):
        """Return a printable version  of the point"""
        return f'Point(x={self.x}, y={self.y})'
 
    
class Circle:
    """A class for representing a cirle with a Point"""
    def __init__(self, center=Point(0, 0), radius=1):
        """Initialize the radius and center point of the circle"""
        self.radius = radius
        self.center = center
    
    @property
    def center(self):
        """Return the center of the circle"""
        return self.__center
    
    @center.setter
    def center(self, point):
        """Set the center attribute of the circle"""
        self.__center = point
    
    @property
    def radius(self):
        """get the radius of the circle"""
        return self.__radius
    
    @radius.setter
    def radius(self, rad):
        """set the radius of the circle"""
        self.__radius = rad
        
    def move(self, x, y):
        """move the circle to a new location where the x and y are provided"""
        self.center.move(x, y)
        
        
    def move(self, point):
        """move the circle to the new provided point"""
        self.center = point
        
    def __repr__(self):
        """Return a string representation of a circle"""
        return f'Circle(center={self.center}, radius={self.radius})'
    
    def __str__(self):
        """Return a printable version  of the circle"""
        return f'Circle at {self.center}, wtih radius {self.radius}'