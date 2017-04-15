from  run_search import *
import os
import sys
import glob


problem_list =[1,2,3]
search_list = [1,3,5,6,7,8,9,10] #[1,3,4,5,7,8,9,10]    
f = open('results.txt', 'w')
for problem in problem_list:
    for search in search_list:
        arg1 = str(problem)
        arg2 = str(search)
        arg3 = "result_"
        arg4 = ".txt"
        #python_exe = "python run_search.py  >" +arg3+ " -p " +arg1+ " -s " + arg2
        file = arg3+arg1+"_"+arg2+arg4
        print("writing results to ....."+file)
        python_exe = "python run_search.py -p " +arg1+ " -s " + arg2+  " >" +file
        print(python_exe)
        os.system(python_exe)

read_files = glob.glob("result*.txt")
with open("final_analysis.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
