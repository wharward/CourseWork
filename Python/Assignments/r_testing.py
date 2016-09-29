import pylab
def drawGraph(xData, yData):
    pylab.figure(1)
    pylab.plot(xData, yData)
    pylab.show()

ageBoys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
weightBoys = [7.16, 9.15, 10.91, 12.56, 14, 15.43, 16.53, 17.64, 18.74, 19.62, 20.28, 21.05, 22, 22.27, 22.82, 23.26, 23.7, 24.14, 24.58, 25.02, 25.35, 25.79, 26.12, 26.57, 28.4]

drawGraph (ageBoys, weightBoys)
