import yaml, json

for i in range(4):
    print i

my_list = []
a = 0
b = 0
i = my_list

my_dict = {a: '1', b: '2'}
my_list.append(my_dict)

with open("some_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
    
with open("some_file2.yml", "w") as f2:
    f2.write(json.dumps(my_list))
