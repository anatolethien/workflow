import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from util import *


df = pd.read_csv(
    filepath_or_buffer="data/data.csv",
    sep=",",
    decimal=".",
    encoding="utf-8",
)
