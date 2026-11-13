import os
import sys
import json

# sys и json не используются в модуле

# Изменяемые аргументы по умолчанию в функциях
def process_items(items=[]):
    processed_data = []
    
    # неиспользуемая функция
    # unused_variable = 42 
    
    for item in items:
        try:
            result = int(item) * 2
            processed_data.append(result)
        except ValueError:
            # необработанное исключение, лучше указать конкретный тип исключения
            pass
            
    return processed_data