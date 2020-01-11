## How to use ?
### Data format
```
{x} {y}
{x} {y}
{x} {y}
{x} {y}
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
\* number of files and their names in **start_data_dir_path** should be same in **result_data_dir_path**

##### Example
```
py app.py test/data test/results test/plots
```