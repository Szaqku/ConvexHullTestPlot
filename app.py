import os

import matplotlib.pyplot as plt
import numpy as np
import sys


def annotate(xs, ys):
    for x, y in zip(xs, ys):
        label = "{:.3f},{:.3f}".format(x, y)

        plt.annotate(label,
                     (x, y),
                     textcoords="offset points",
                     xytext=(0, 10),
                     ha='center')


def main():
    if len(sys.argv) != 4:
        print("Expected 3 args, got %d" % (len(sys.argv)-1))
        exit(-1)

    dirPath = sys.argv[1]
    resultPath = sys.argv[2]
    outPath = sys.argv[3]

    if not os.path.exists(outPath):
        os.makedirs(outPath)

    dataFiles = zip(os.listdir(dirPath), os.listdir(resultPath))

    for inputFile, resultFile in dataFiles:
        dataFileName = F'{dirPath}/{inputFile}'
        resultsFileName = F'{resultPath}/{inputFile}'
        plotFileName = F'{outPath}/{resultFile[:-3]}png'

        data = np.loadtxt(dataFileName, skiprows=1)
        dataResult = np.loadtxt(resultsFileName)
        w, h = dataResult.shape
        dataResult = np.resize(dataResult, (w + 1, h))
        dataResult[w, :] = dataResult[0, :]

        plt.plot(data[:, 0], data[:, 1], 'k.',
                 dataResult[:, 0], dataResult[:, 1], 'r-')

        plt.plot(dataResult[0, 0], dataResult[0, 1], 'go', markersize=8.0)

        annotate(dataResult[:, 0], dataResult[:, 1])

        plt.savefig(plotFileName)
        print(F'Saved plot as {plotFileName}')
        plt.figure()


if __name__ == "__main__":
    main()
