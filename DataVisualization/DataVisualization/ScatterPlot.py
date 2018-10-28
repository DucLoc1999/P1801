import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

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

def multiMatrixdef(dataFrame, rowsIndex, colsIndex_x, colsIndex_y, kind='reg', diag_kind='hist', hue=None):
	'''
		:param dataFrame: The DataFrame need ploting
		:param rowsIndex: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
		:param ColsIndex_x: cols you want to display in your chart by layber x_vars:
			+ The row of the figure
		:param ColsIndex_y: cols you want to display in your chart by layber y_vars:
			+ The colume of the figure
		:param Kind: Kind of plot for the non-identity relationships
			+ Can pass one of {‘scatter’ |‘reg’}, if pass 'reg' it will add a line represent for linear relationship
		:param Diag_kind: Kind of plot for the diagonal subplots
			+ Can pass one of {‘auto’ | ‘hist’ | ‘kde’}
		:param hue: Variable in data to map plot aspects to different colors.
			+ cols you want to distinguish by colors
		:return: seaborn.axisgrid
	'''

	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.pairplot(dataFrame.iloc[rowsIndex,:],hue=hue,x_vars=head[colsIndex_x],y_vars=head[colsIndex_y],kind=kind,diag_kind=diag_kind))
	return sb.pairplot(dataFrame.iloc[rowsIndex,:],hue=hue,x_vars=head[colsIndex_x],y_vars=head[colsIndex_y],kind=kind,diag_kind=diag_kind)


def jointplot(dataFrame, rowsIndex, colsIndex_x, colsIndex_y, kind="kde"):
	'''
	:param dataFrame: The DataFrame need ploting
	:param rowsIndex: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
	:param colsIndex_x: cols you want to display in your chart by layber x:
			+ The row of the figure
	:param colsIndex_y: cols you want to display in your chart by layber y:
			+ The colume of the figure
	:param kind: Kind of plot for the diagonal subplots
			+ Can pass one of { “scatter” | “reg” | “resid” | “kde” | “hex” }
			+  if pass "reg" it will add a line represent for linear relationship
	:return: seaborn.axisgrid
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.jointplot(x=head[colsIndex_x],y=head[colsIndex_y],data=dataFrame.iloc[rowsIndex,:],kind=kind))
	return sb.jointplot(x=head[colsIndex_x],y=head[colsIndex_y],data=dataFrame.iloc[rowsIndex,:],kind=kind)

def lmplot(dataFrame, rowsIndex, colsIndex_x, colsIndex_y, hue=None):
	'''
		:param dataFrame: The DataFrame need ploting
		:param rowsIndex: Rows you want to display in your chart:
			+ Pass a num: <row> to display one row
			+ Pass an array: <[num1, num2, num3, ...]> to display rows you want
			+ Pass: <range(start, end)>, for multiple rows
		:param ColsIndex_x: cols you want to display in your chart by layber x_vars:
			+ The row of the figure
		:param ColsIndex_y: cols you want to display in your chart by layber y_vars:
			+ The colume of the figure
		:param hue: Variable in data to map plot aspects to different colors.
			+ cols you want to distinguish by colors
		:return: seaborn.axisgrid
	'''
	head = dataFrame.columns.values
	sb.set()
	plt.show(sb.lmplot(x=head[colsIndex_x], y=head[colsIndex_y], data=dataFrame.iloc[rowsIndex,:], hue=hue, order=2))
	return sb.lmplot(x=head[colsIndex_x], y=head[colsIndex_y], data=dataFrame.iloc[rowsIndex,:], hue=hue, order=2)
