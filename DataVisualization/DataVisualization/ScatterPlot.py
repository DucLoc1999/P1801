import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sb
from pandas.plotting import scatter_matrix

import matplotlib
from matplotlib import pyplot as plt

def Scatter_2D(dataFrame, _1st_index, _2nd_index):
    '''
    :param dataFrame: All the data you want to visualize
    :param _1st_index: The first attribute signed as Ox line
    :param _2nd_index: The second attribute signed as Oy line
    '''

    area = 10 ** 2
    Ox = dataFrame.iloc[:,0:_1st_index+1]
    Oy = dataFrame.iloc[:,1:_2nd_index+1]
    plt.scatter(Ox, Oy, s=area, marker='x', color = 'r', alpha=0.5)

    # Get names of attributes
    attributeName = list(dataFrame)

    plt.xlabel(attributeName[_1st_index])
    plt.ylabel(attributeName[_2nd_index])
    plt.show()

def Scatter_3D(dataFrame, _1st_index, _2nd_index, _3rd_index):

    '''
    :param dataFrame: all the data you want to visualize
    :param _1st_index: the first attribute signed as Ox line
    :param _2nd_index: the second attribute signed as Oy line
    :param _3rd_index: the third attribute signed as Oz line
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    area = 10 ** 2
    Ox = dataFrame.iloc[:, 0:_1st_index+1]
    Oy = dataFrame.iloc[:, 1:_2nd_index+1]
    Oz = dataFrame.iloc[:, 2:_3rd_index+1]

    ax.scatter(Ox, Oy, Oz,
               s=area, marker='x', alpha=0.5, color='r')

    # Get names of attributes
    attributeName = list(dataFrame)

    ax.set_xlabel(attributeName[_1st_index])
    ax.set_ylabel(attributeName[_2nd_index])
    ax.set_zlabel(attributeName[_3rd_index])
    plt.show()

def multiMatrix(dataFrame, rowsIndex, colsIndex_x, colsIndex_y, kind='reg', diag_kind='hist'):
	'''
		:param dataFrame: the DataFrame need ploting
		:param rowsIndex: rows you want to display in your chart:
			+ pass a num: <row> to display one row
			+ pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ pass: <range(start, end)>, for multiple rows
			+ default = arange(0,50), The first 50 rows from 0 to 49
		:param colsIndex_x: cols you want to display in your chart by layber x_vars:
			+ the row of the figure
			+ default = all the cols in dataframe
		:param colsIndex_y: cols you want to display in your chart by layber x_vars:
			+ the row of the figure
			+ default = all the cols in dataframe
		:param kind: Kind of plot for the non-identity relationships
			+ can pass one of {‘scatter’, ‘reg’}, if pass 'reg' it will add a line represent for linear relationship
		:param diag_kind : Kind of plot for the diagonal subplots
						+ can pass one of {‘auto’, ‘hist’, ‘kde’}, 'auto' and 'hist' is the same
		:return: void
	'''

	head = dataFrame.columns.values
	sb.set()
	sb.despine()
	plt.show(sb.pairplot(dataFrame.iloc[rowsIndex,:],x_vars=head[colsIndex_x], y_vars=head[colsIndex_y],kind=kind,diag_kind=diag_kind))


