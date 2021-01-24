# Export data to LaTeX
## Requirments
The module required for this functions is `pandas` (1.2.1).

## Usage
Given a pandas DataFrame object, the function exports the data to a tex file data can be included in a 
LaTeX table environment.   
```python
import pandas as pd
from python_to_latex import export_data_to_latex

data = pd.DataFrame({'a': [1.25, 2, -3], 'b': ['Hello', 'there', 'world']})
export_data_to_latex(data, 'example.tex', row_names=['1', '2', '3'], round_precision=1)
```
The exported data can then be included in LaTeX table environment:
```latex
\begin{table}
    \begin{tabular}
        a & b \\
        \cline
        \input{"example.tex"}
    \end{tabular}
\end{table}
```

## Options
The following options are available:
* `round_precison`: integer defining the rounding precision of the numeric columns; default=`None`
* `row_names`: list of row names (same length as number of rows in `data`); default=`None` 

Note that, when round precision is an integer number, all numbers are exported with the same decimal precision, e.g.
"5" if exported as "5.00" if `round_precison=2`.