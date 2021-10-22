import yaml

data = {
    1: [1, 2, 3],
    2: 255,
    3: '1024абвгд'
}

print(data)

with open('y_file.yaml', 'w') as f_n:
    yaml.dump(data, f_n, default_flow_style=True, allow_unicode=True)

with open('y_file.yaml') as f_n:
    print(f_n.read())
