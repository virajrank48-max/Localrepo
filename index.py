print("This is the index.py file in the LocalRepo directory.")

# Econometric Dummy dependent Variable regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import logit

import os
if os.path.exists(r'C:\Users\dell\OneDrive\Documents\practice data\MLE.csv'):
    print("File exists")
else:
    print("File not found")