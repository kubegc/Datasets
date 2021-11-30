import sys
import os
import json
import ast

def simple_list_to_str(data_list:list)->dict:
    result={}
    for value in data_list:
        if str(value) not in result.keys():
            result[str(value)] = 1
        else:
            result[str(value)] += 1

    return result

def simple_json_dict(data_dict:dict): 
    for batch_size in data_dict.keys():
        for op in data_dict[batch_size].keys():
            if "args" not in data_dict[batch_size][op].keys() or "params" not in data_dict[batch_size][op].keys():
                print("contain:",str(data_dict[batch_size][op]))
                print("args or params lost: batch_size=%s, op=%s"%(batch_size,op))
                break
            inputs=[]

            args_list = list(data_dict[batch_size][op]["args"])
            params_list = list(data_dict[batch_size][op]["params"])

            for arg,param in zip(args_list,params_list):
                inputs.append([arg,param])

            data_dict[batch_size][op] = simple_list_to_str(inputs)

    return data_dict

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
            name_list1[1] = str(ast.literal_eval(name_list1[1]))
            source_data1 = {str(name_list1[0]):{str(name_list1[1]): json.load(f)}}
    
    if not (os.path.exists(source_file2) and source_file2.endswith(".json")):
        print("file: <" + source_file2 + "> is not one exist json file.")
        return

    name_list2 = [s for s in source_file2.split("/")[-1][:-5].split(split_str) if s != ""]
    if str(name_list2[0]) not in source_data1.keys():
        source_data1[str(name_list2[0])] = {}

    name_list2[1] = str(ast.literal_eval(name_list2[1]))
    
    if str(name_list2[1]) not in source_data1[str(name_list2[0])].keys():
        source_data1[str(name_list2[0])][name_list2[1]] = {}

    source_data2={}
    with open(source_file2,'r') as f:
        source_data2 = json.load(f)

    source_data1[str(name_list2[0])][str(name_list2[1])].update(simple_json_dict(source_data2))
    with open(aim_file,"w") as f:
        json.dump(source_data1,fp=f,indent=4,separators=(',', ': '),sort_keys=True)

merge(sys.argv[1],sys.argv[2],sys.argv[3])