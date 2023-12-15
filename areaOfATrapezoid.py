"""This assignment is to demonstrate the ability to use AWS lambda"""

#imports
import json
import math

#functions
#lambda handler
def lambda_handler(event, context):
    """This function is to display the lambda information"""
    height = event.get("height")
    base_one = event.get("base_one")
    base_two = event.get("base_two")
    
    trapezoid_area = area_of_trapezoid(int(base_one), int(base_two), int(height))
  
    return {
        'statusCode': 200,
        'body': json.dumps('The area of the trapezoid is ' + str(trapezoid_area) + '.')
    }

#area    
def area_of_trapezoid(a, b, height):
    """This function is to calculate the area of the trapezoid"""
    area = ((a + b) / 2) * height
    return area
