import os
import sys  
import json 

def process_items(items=[]):
    processed_data = []
    
    unused_variable = 42 
    
    for item in items:
        try:
            result = int(item) * 2
            processed_data.append(result)
        except:
            pass
            
    return processed_data