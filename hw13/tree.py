import os

def get_paths():
    paths = []
    start = '.'
    for x,y,z in os.walk(start):
        path = str(x)
        paths.append(path)
    return paths

def get_all_depths(paths):
    depths = []
    for path in paths:
        parts = path.split('\\\\')
        if len(parts) == 1:
            parts = path.split('\\')
            if len(parts) == 1:
               parts = path.split('//')
               if len(parts) == 1:
                   parts = path.split('/')  
        res = len(parts)-1
        depths.append(res)
    return depths

def get_max_depth(depths):
    result = max(depths)
    print('Максимальная глубина папки в этом дереве:',result)

def _main_():
    get_max_depth(get_all_depths(get_paths()))

_main_()
    
    
    
