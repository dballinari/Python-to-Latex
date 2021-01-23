import pandas as pd


def export_data_to_latex(data, path, row_names=None):
    dim_data = data.shape
    data = data.astype(str)

    if dim_data[0] != len(row_names):
        row_names = None
        print('row_names has not the same length as the number of rows!')
    if not isinstance(row_names, list) and not isinstance(row_names, set):
        row_names = None
        print('row_names is not of type list or set!')

    if row_names is not None:
        row_names = [str(x) for x in row_names]

    with open(path, 'w') as f:
        for r in range(dim_data[0]):
            row = ' & '.join(data.loc[r].to_list())
            if row_names is not None:
                row = row_names[r] + ' & ' + row
            row += r'\\'
            f.write("%s\n" % row)