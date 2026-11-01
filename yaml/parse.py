import yaml

my_file = "test.yaml"

with open(my_file, encoding="utf-8") as f:
    try:
        data = yaml.safe_load(f)
        for k, v in data.items():
            print(f"key: {k}, value: {v}")
    except yaml.YAMLError as e:
        print(e)
