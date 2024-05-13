import os
os.chdir("./FilesA11")

def lc_task_a() -> list:
    return [f for dfs in [files for root, dirs, files in os.walk(".", topdown=False)] for f in dfs if f.endswith(".tex") and "aufg" in f]

def lc_task_b() -> list:
    return [file for file in [os.path.join(dfs[0], f) for dfs in [(root, files) for root, dirs, files in os.walk(".", topdown=False)] for f in dfs[1]]]


if __name__ == "__main__":
    print("Hello World!")
    print(lc_task_a())
    print(lc_task_b())