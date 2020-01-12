[![Build status](https://camo.githubusercontent.com/cc790c12ed8699e6e9fdb9a37e297fb9afde5c3b/68747470733a2f2f7472617669732d63692e6f72672f616e67756c61722f616e67756c61722e6a732e7376673f6272616e63683d6d6173746572)](https://github.com/Szaqku/ConvexHullTestPlot/releases/download/1.0/BestPyPlotTest_1.0.exe)

## How to use ?
### Data format
- START DATA FORMAT
    ```
    n 
    x0 y0
    x1 y1
    x2 y2
    x3 y3
    ```
  **n** can be anything
- RESULT DATA FORMAT
    ```
    z0 k0
    z1 k1
    z2 k2
    z3 k3
    ```
##### Example:
```
0.666 0.123
0.542 0.777
0.432 0.786
```
### Run
- with python already installed
    ##### Command line
    ```
    $ py app.py [start_data_dir_path] [result_data_dir_path] [output_plot_dir_path]
    ```
    \* number of files and their names in **start_data_dir_path** should be same in **result_data_dir_path** \
    \* example data can be found in directory **test/**
    ##### Example
    ```
    $ py app.py test/data test/results test/plots
    ```
- on windows without python 
    #####  Download file using link below: 
    - [Download Link](https://github.com/Szaqku/ConvexHullTestPlot/releases/download/1.0/BestPyPlotTest_1.0.exe)
    - Install
    - Open console: `WIN+R > cmd`
    - Run commands
    ```
    > cd path_to_just_installed_app
    > Python\python.exe "BestPyPlotTest.launch.py" [start_data_dir_path] [result_data_dir_path] [output_plot_dir_path]
    ``` 
    ##### Example
    ```
    > cd path_to_just_installed_app
    > Python\python.exe BestPyPlotTest.launch.py test/data test/results test/plots
    ``` 
    
