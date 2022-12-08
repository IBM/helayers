### HE4Cloud Demo Dataset

A dataset is build from two files: CSV file, and Json file.

The CSV file contains the data. Only numerical data is supported. The demo example contains the following columns: height, weight, and salary.
The json file describes metadata of each column with number of bins requierd when calculating the histogram. 

For example: 

```json

{
    "columns": {
        "salary": {
            "bins": 5
        },
        "height": {
            "bins": 4
        },
        "weight": {
            "bins": 5
        }
    }
}

``` 

The requested number of histogram bins for salary column is 5.

**NOTE: at this time Chrome browser doesn't support uploading datasets.**
