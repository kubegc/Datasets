import os
import json

save_json_path = "./dataset_simple.json"
json_path = "../dataset_auto.json"
program_path = os.path.dirname(os.path.abspath(__file__))

def simple_list_to_str(data_list:list)->dict:
    result={}
    for value in data_list:
        if str(value) not in result.keys():
            data_list[str(value)] = 1
        else:
            data_list[str(value)] += 1

    return result


def simple_json_dict(data_dict:dict): 
    for model_name in data_dict.keys():
        for shapes in data_dict[model_name].keys():
            for batch_size in data_dict[model_name][shapes].keys():
                for op in data_dict[model_name][shapes][batch_size].keys():
                    if data_dict[model_name][shapes][batch_size][op] is not dict or "args" not in data_dict[model_name][shapes][batch_size][op].keys() or "params" not in data_dict[model_name][shapes][batch_size][op].keys():
                        print("args or params lost: model_name=%s, shapes=%s, batch_size=%s, op=%s"%(model_name,shapes,batch_size,op))
                        break
                    inputs=[]

                    args_list = list(data_dict[model_name][shapes][batch_size][op]["args"])
                    params_list = list(data_dict[model_name][shapes][batch_size][op]["params"])

                    for arg,param in zip(args_list,params_list):
                        inputs.append([arg,param])

                    data_dict[model_name][shapes][batch_size][op] = inputs

    return data_dict

def main():
    datas = None
    with open(os.path.join(program_path,json_path),"r") as f:
        datas = json.load(f)
        datas = simple_json_dict(datas)

    
        datas = simple_list_to_str(datas)

    with open(os.path.join(program_path,save_json_path),"w") as f:
                json.dump(datas,fp=f,indent=4,separators=(',', ': '),sort_keys=True)
    
    
if __name__ == "__main__":
    main()