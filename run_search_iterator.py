from  run_search import *
import os
import sys

problem_list =[1,2,3]
search_list = [1,3,4,5,6,7,8,9,10]
for problem in problem_list:
    for search in search_list:
        arg1 = str(problem)
        arg2 = str(search)
        python_exe = "python run_search.py -p " +arg1+ " -s " + arg2
        print(python_exe)
        os.system(python_exe)
