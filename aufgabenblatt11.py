import os
import numpy

os.chdir("./FilesA11")

def lc_task_a() -> list:
    return [f for dfs in [files for root, dirs, files in os.walk(".", topdown=False)] for f in dfs if f.endswith(".tex") and "aufg" in f]

def lc_task_b() -> list:
    return [la for la in[fs for fs in [os.path.join(dfs[0], f) for dfs in [(root, files) for root, dirs, files in os.walk(".", topdown=False)] for f in dfs[1]] if fs.endswith(".tex")] if len([lc for lc in open(la, "r").readlines() if len(lc) < 2]) > 100]


def lc_task_c() -> list:
    return [la for la in[fs for fs in [os.path.join(dfs[0], f) for dfs in [(root, files) for root, dirs, files in os.walk(".", topdown=False)] for f in dfs[1]] if fs.endswith(".tex")] if any(lc for lc in open(la, "r").readlines() if len(lc) >= 30)]

def powZeroToHundred() -> list:
    return numpy.arange(101) ** 2

def zeroToTHousandWithoutModFive() -> list:
    numbers = numpy.arange(1001)
    numbers = numpy.delete(numbers, numpy.where(numbers % 11 == 0))
    numbers = numpy.delete(numbers, numpy.where(numbers % 13 == 0))
    
    return numbers

def createArray() -> list:
    return (numpy.arange(101) % 2)

if __name__ == "__main__":
    
    # print(lc_task_a())
    # print(lc_task_b())
    print(powZeroToHundred())
    print(zeroToTHousandWithoutModFive())
    print(createArray())