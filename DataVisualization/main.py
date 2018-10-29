import DataVisualization.DrawChart as vsl
import DataVisualization.ScatterPlot as sct

df = vsl.fileVisualizer('data\stcp-Rdataset-Diet.csv')

cols = [3, 4, 6]
rows = range(20)

'''Draw barh chart plot with cols=cols, rows=rows and stacked'''
#vsl.drawBar(df, rows, cols, True, True)

'''Draw line chart plot with cols=cols and rows=rows'''
#vsl.drawLine(df, rows, cols)

'''Draw histogram chart plot with cols[0] and rows[0:max]'''
#vsl.drawHistogram(df, cols, 50)

'''Draw pie plot with cols=cols and row[1]'''
#vsl.drawPie(df, 1, cols)

'''Draw stem plot with col[0] and rows=rows'''
#vsl.drawStem(df, rows, 0)

'''Draw box plot with col[0] and rows=rows'''
#vsl.drawBox(df, rows, 0)

'''Draw violin plot with col[0] and rows[0:max]'''
#vsl.drawViolin(df, 0)

'''Draw scatter plot with col[0] and col[3]'''
#vsl.drawScatter(df, 0, 3)