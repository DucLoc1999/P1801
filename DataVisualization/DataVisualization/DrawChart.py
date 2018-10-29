import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

def fileVisualizer(path):
    '''
        :param path: Path to your file
        :return: A Data Frame of your file
    '''
    df = pd.read_csv(path)

    print(df)
    print('-' * 50)
    print(df.describe())
    return df

def drawBar(dataFrame, rows, cols, stacked=False, horizontal=False, alpha=0.5, rot=0):
    '''
        :param dataFrame: The DataFrame of your file
        :param rows: Rows will be shown:
                           + pass a num to display one row
                           + pass an array [num1, num2, num3, ...] to display rows you want
                           + pass a range(start, end) for multiple rows
        :param cols: Cols will be shown:
                           + similar to the rows
        :param stacked: Your bar chart is stacked or not
        :param horizontal: Display horizontal bar
        :return: Void
    '''

    df = dataFrame.iloc[rows, cols]
    if horizontal:
        df.plot.barh(stacked=stacked, alpha=alpha, rot=rot)
    else:
        df.plot.bar(stacked=stacked, alpha=alpha, rot=rot)
    plt.show()

def drawLine(dataFrame, rows, cols, alpha=0.5, rot=0):
    '''
        :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    df.plot(alpha=alpha, rot=rot)
    plt.show()

def drawHistogram(dataFrame, cols, bins=50, alpha=0.5, rot=0):
    '''
        :param bins: Number of the bars in the histogram plot
        :return: Void
    '''
    df = dataFrame.iloc[:, cols]
    df.plot.hist(bins=bins, rot=rot, alpha=alpha)
    plt.show()

def drawPie(dataFrame, row, cols, rot=0):
    '''
    :param row: A int showing the row will be drawn
    :return: Void
    '''
    df = dataFrame.iloc[row, cols]
    df.plot.pie(rot=rot)
    plt.show()

def drawStem(dataFrame, rows, cols, linefmt='-.'):
    '''
    :param cols: A int or array showing the column will be drawn
    :param linefmt: A string defining the properties of the vertical lines
    :return: Void
    '''
    plt.stem(dataFrame.iloc[rows, cols], bottom=0, linefmt=linefmt)
    plt.show()

def drawBox(dataFrame, rows, cols, vert=False):
    '''
    :param vert: Horizontal or not
    :return: Void
    '''
    df = dataFrame.iloc[rows, cols]
    plt.boxplot(df, vert=False)
    plt.show()

def drawViolin(dataFrame, cols, vert=False):
    '''
    :return: Void
    '''
    df = dataFrame.iloc[:, cols]
    plt.violinplot(df, vert=vert, showmedians=True)
    plt.show()