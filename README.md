# Block-Model-Compression-Algorithm by Team-Lucky-Seven-Blocks7

### --- Software Engineering Project 2021, Semester 2 ---

- The Process Presentation: https://youtu.be/8KREdUwu0-8
- The Final Presentation: https://youtu.be/UnH8W6-WjKw
- Final report >> [click here](https://github.com/boyleerock/Block-Model-Compression-Algorithm/blob/main/assignment/final-report_BLOCKSPG7_1806297.pdf)
- retrospective1 >> [click here](https://github.com/boyleerock/Block-Model-Compression-Algorithm/blob/main/assignment/retrospective1_BLOCKS7PG_1806297.pdf)
- retrospective2 >> [click here](https://github.com/boyleerock/Block-Model-Compression-Algorithm/blob/main/assignment/retrospective2_BLOCKS7PG_1806297.pdf)
- retrospective3 >> [click here](https://github.com/boyleerock/Block-Model-Compression-Algorithm/blob/main/assignment/retrospective3_BLOCKS7PG_1806297.pdf)
- retrospective4 >> [click here](https://github.com/boyleerock/Block-Model-Compression-Algorithm/blob/main/assignment/retrospective4_BLOCKS7PG_1806297.pdf)

The document `software_architecture.pdf` in the Documentation directory contains an overview of the software architecture and the algorithms developed.

### Fast CPU / GPU Implementation

A fast CPU and GPU implementation was underway when this project stopped. The Numba package was used. You can find all the changes in the `port-to-numba` branch


### This project is presented as a gamified design and implementation challenge...

1. We are required to develop the program which can take uncompressed input data on standard input and produce compressed output data on standard output with no loss.

2. And submit either an .exe file or a Python script to a verification service: [MAPTEK TITAN](https://titan.maptek.net/).

3. The verification service will execute our code and score it compared to all the other entries received on **processing speed** and **compression performance**.


* More description of this project: [Click Here](https://github.cs.adelaide.edu.au/Block-Model-Compression/Blocks7/blob/master/Documentation/2021%20SEP%20-%20Block%20Model%20Compression%20Algorithm%20(1).pdf) and [💾 Google Drive](https://drive.google.com/drive/folders/1QyvOGO9eaNAR_qqZ4VGoYZEHiHzBkROb?usp=sharing) from tutor     
* Agile (Scrum) Project Management: [Click Here](https://github.cs.adelaide.edu.au/Block-Model-Compression/Blocks7/projects).
* The two datasets and validator to test and validate our compression tool (the_intro_one & the_fast_one)
* And the other two datasets released on 7th Sep (the_stratal_one_42000000_14x10x12 & the_big_one_987417600_8x8x5)
* Command->>    `python runner.py -s -v < path to your python or executable file > < test data file path >`

## Development Environment

If using a version of Anaconda that matches what is used on Titan, then no
extra steps are needed. If you are not using that installation of Python, then
keep reading.

Python Virtual Environments are used to keep all the dependencies of this project
self contained and not mixed up with the system python libraries.

First make sure you are in the `Code` directory.

Then set up the Python Virtual environment:
```
python3 -m venv .venv
```

Then activate the environment:

For Linux/Mac:
```
$ source .venv/bin/activate
```

For Windows:
```
$ .venv\Scripts\activate
```

The first time you start the virtual environment, install all the development
dependencies

```
$ pip install -r requirements.txt
```

When you are finished developing, deactivate the environment

```
$ deactivate
```

### Static Analysis

Static analysis tools should be run on the code before committing and especially
before merging. First the `flake8` command should be used to check coding style.

```
$ flake8 directory/with/code
```

Once all those issues are resolved, run the type checker `pytype` 

```
$ pytype directory/with/code
```

This will infer and check that the types of variables are passed around
correctly. If possible try to eliminate these errors. However if the code runs
correctly, you don't need to make large changes to accomodate this tool.

### Members in Team Lucky Seven (Blocks7):
| Name | Student ID | School E-mail |Snapshot drafting |
| ------------- | ------------- |------------- |------------- |
| Po-Yi Lee	| a1806297 | a1806297@student.adelaide.edu.au | 1.1 & 5.2 |       
| Hechen Wang	| a1786785 | a1786785@student.adelaide.edu.au | 1.2 |           
| Yang Lu	| a1782685 | a1782685@student.adelaide.edu.au | 2.1 |            
| Yuanpeng Liu | a1784375 | a1784375@student.adelaide.edu.au | 2.2 |              
| Kaiyang Xue | a1784184 | a1784184@student.adelaide.edu.au | 3.1 |       
| Xiaoman Li | a1804817 | a1804817@student.adelaide.edu.au | 3.2 |        
| Liuyang Yun	| a1811518 | a1811518@student.adelaide.edu.au | 4.1 |     
| Jiaping Qi | a1797683 | a1797683@student.adelaide.edu.au | 4.2 |        
| Karl Asenstorfer | a1162576 | a1162576@student.adelaide.edu.au | 5.1 |               

### Secheduled Scrum Masters:
| Sprint | Name | Student ID |
| ------------- | ------------- |------------- |
|  1 | Po-Yi Lee | a1806297 |          
|  2 | Yuanpeng Liu | a1784375 |           
|  3 | Karl Asenstorfer | a1162576 |             
|  4 | Xiaoman Li | a1804817 |               
|  5 | Kaiyang Xue | a1784184 |

### Shared Assignment File:
| WEEK | Snapshot | Drafting |
| ------------- | ------------- | ------------- |
| Week 2 | [Snapshot0 & Initial report](https://docs.google.com/document/d/1qK1QGABUQcw26S0sthkT3W2lq3NyCU_t05oJHKM05Lg/edit) | Team |         
| Week 3 | [Snapshot1.1](https://docs.google.com/document/d/1-mBykOOeE39EyrWUM8MEhsvELT3iMaJsD1fKq_8m8d8/edit#heading=h.5xqd1vz0nfd9) | Po-Yi Lee |
| Week 4 | [Snapshot1.2](https://docs.google.com/document/d/1ZWMcmtDk80Algg_bGJ3O6KYYwPeG-0L1UCa4EpFIq2E/edit?usp=sharing) | Hechen Wang | 
| Week 5 | [Snapshot2.1](https://docs.google.com/document/d/1R_HPHPyojO8tXQ79DnMCNHlCSi4JB0RrvFY60DHXNfI/edit?usp=sharing) | Yang Lu |
| Week 6 | [Snapshot2.2](https://docs.google.com/document/d/1x00OMshJCH4CeJaxoLuiYO7xgGjyXYhw/edit) | Yuanpeng Liu |
| Week 7 | [Snapshot3.1](https://docs.google.com/document/d/1ZQGYLTYRCukQ0kIFcPV6VQl9wz3HWIQ8DY7H0SlatIE/edit#heading=h.30j0zll) | Kaiyang Xue |
| Week 8 | [Snapshot3.2](https://docs.google.com/document/d/1zPbiI4gZ7TaS1KB0ISp9rCXb9mhoX8G3eIvLdhxYf_8/edit#) | Xiaoman Li |
| Week 9 | [Snapshot4.1](https://docs.google.com/document/d/1R0AZQgpXWo9WECZAdpBZST6PrAJqNeegHU--f07J0Ek/edit) | Liuyang Yun |  
| Week 10 | [Snapshot4.2](https://docs.google.com/document/d/1T__6mXokh-2oI_lGO1RkI2Rnl3aHtzkdQMiFwR5tC34/edit?usp=sharing) | Jiaping Qi |    
| Week 11 | [Snapshot5.1](https://docs.google.com/document/d/1KmOJ624EAMJ6o7vA9kgwzmTeDannrKPmUrgNeT4XXJk/edit?usp=sharing) | Karl Asenstorfer |   
| Week 12 | [Snapshot5.2]() | Po-Yi Lee |      


### Keep in touch Via:                    
:sparkles:Slack Channel: blocks7
