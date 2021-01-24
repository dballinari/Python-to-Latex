# todo: add 'phantom' characters such that each entry in a column has the same length
import pandas as pd


def export_data_to_latex(data, path, row_names=None, round_precision=None):
    """
    Function that exports a pandas DataFrame into a tex-file that can be included be in a LaTeX table environment.

    Args:
        data: pandas DataFrame
        path: string defining path and name of the destination file (should end with '.tex')
        row_names: list of row names (same length as number of rows in 'data'); default=None
        round_precision: integer defining the rounding precision of the numeric columns; default=None

    Returns: nothing

    """
    # check that the data is a pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        print('Data must be an instance of pandas DataFrame!')
    # if the round precision is an integer, apply the rounding to all numeric columns
    if isinstance(round_precision, int):
        data.update(data.select_dtypes(include='number').
                    apply(lambda x: ['{:.{}f}'.format(x_i, round_precision) for x_i in x]))
    # get the dimension of the data frame
    dim_data = data.shape
    # convert all entries into strings
    data = data.astype(str)

    # check that the row names are appropriate: one name for each row save in a list
    if dim_data[0] != len(row_names):
        row_names = None
        print('row_names has not the same length as the number of rows!')
    if not isinstance(row_names, list):
        row_names = None
        print('row_names is not of type list!')
    # ensure that the row names are strings
    if row_names is not None:
        row_names = [str(x) for x in row_names]

    with open(path, 'w') as f:
        # export row by row
        for r in range(dim_data[0]):
            row = ' & '.join(data.loc[r].to_list())
            # if the table has row names, add them a the beginning of each row
            if row_names is not None:
                row = row_names[r] + ' & ' + row
            # at the end of each row, we add the new-line command of latex
            row += r'\\'
            f.write("%s\n" % row)

