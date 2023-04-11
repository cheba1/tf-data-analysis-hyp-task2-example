import pandas as pd
import numpy as np


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    return anderson_ksamp([x, y]).pvalue < 0.06 # Ваш ответ, True или False
