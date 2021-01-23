import pandas as pd
from python_to_latex import export_data_to_latex

# Test example (to remove later)
data_t = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
export_data_to_latex(data_t, 'text.tex', row_names=['1', '2', '3'])