"""This assignment is to demonstrate the ability to use AWS lambda"""

#imports
import json
import math

#functions
#lambda handler
def lambda_handler(event, context):
    """This function is to display the lambda information"""
    radius = event.get("radius")
    height = event.get("height")

    cone_area = area_of_cone(int(radius), int(height))

    return {
        'statusCode': 200,
        'body': json.dumps('The area of the cone is ' + str(cone_area) + '.')
    }
    
#area
def area_of_cone(radius, height):
    """This function is to calculate the area of the cone"""
    area = math.pi * radius * (radius + math.sqrt((height ** 2 + radius **2)))
    return area
