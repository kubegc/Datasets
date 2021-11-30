import sys
import os
import json

def merge(source_file1: str,source_file2: str,aim_file="dataset.json",split_str="__"):
    source_data1={}
    if not os.path.exists(source_file1):
        source_data1 = {}
    elif source_file1 == aim_file:
        with open(source_file1,'r') as f:
            source_data1 = json.load(f)
    else:
        with open(source_file1,'r') as f:
            name_list1 = [s for s in source_file1.split("/")[-1][:-5].split(split_str) if s != ""]
            source_data1 = {str(name_list1[0]):{str(name_list1[1]): json.load(f)}}
    
    if not (os.path.exists(source_file2) and source_file2.endswith(".json")):
        print("file: <" + source_file2 + "> is not one exist json file.")
        return

    name_list2 = [s for s in source_file2.split("/")[-1][:-5].split(split_str) if s != ""]
    if str(name_list2[0]) not in source_data1.keys():
        source_data1[str(name_list2[0])] = {}
    
    if str(name_list2[1]) not in source_data1[str(name_list2[0])].keys():
        source_data1[str(name_list2[0])][str(name_list2[1])] = {}

    source_data2={}
    with open(source_file2,'r') as f:
        source_data2 = json.load(f)

    source_data1[str(name_list2[0])][str(name_list2[1])].update(source_data2)
    with open(aim_file,"w") as f:
        json.dump(source_data1,fp=f,indent=4,separators=(',', ': '),sort_keys=True)

merge(sys.argv[1],sys.argv[2],sys.argv[1])