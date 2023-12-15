"""This assignment is to demonstrate the ability to use AWS lambda"""

#imports
import json
import math

#functions
#lambda handler
def lambda_handler(event, context):
    """This function is to display the lambda information"""
    radius = event.get("radius")

    circle_circumference = circumference_of_circle(int(radius))
    
    return {
        'statusCode': 200,
        'body': json.dumps('The circle circumference is ' + str(circle_circumference) + '.')
    }
  
#circumference  
def circumference_of_circle(radius):
    """This function is to calculate the circumference of a circle"""
    perimeter = 2 * math.pi * radius
    return perimeter