import yaml

fname = 'config.yaml'

def mongodb_out(get_info):
    with open(fname, 'r') as f:
        yaml_return = yaml.load(f)
        return(yaml_return[get_info])
