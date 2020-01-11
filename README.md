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
```
$ py app.py [start_data_dir_path] [result_data_dir_path] [output_plot_dir_path]
```
\* number of files and their names in **start_data_dir_path** should be same in **result_data_dir_path** \
\* example data can be found in directory **text/**
##### Example
```
$ py app.py test/data test/results test/plots
```