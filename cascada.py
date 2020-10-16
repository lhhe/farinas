import pandas as pd
import numpy as np

# montar la matrix de especies, y usar "Species" como ind
data = pd.read_csv("example_matrix.csv", index_col="Species")
print(data.index)
