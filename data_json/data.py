import json
part_nums = ['ECA-1EHG102','CL05B103KB5NNNC','CC0402KRX5R8BB104']

def json_list(list):
    lst = []
    d = {}
    for pn in list:
        d['data']=pn

        lst.append(d)
    return json.dumps(lst, separators=(',',':'))

print json_list(part_nums)
