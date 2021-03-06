import os
import json
import numpy

_script_path = os.path.dirname(os.path.abspath(__file__))


class NamedColors():
    '''
    Named colors from matplotlib
    '''

    def __init__(self, f_colors=None):

        if f_colors is None:
            f_colors = os.path.join(
                _script_path, 'named_colors', 'matplotlib.json')

        with open(f_colors) as FIN:
            raw = FIN.read()
            
        self.colors = json.loads(raw)

    def __call__(self, name):

        if name not in self.colors:
            msg = f"Color {name} not a known color."
            raise KeyError(msg)
        
        return self.colors[name]


    def __len__(self):
        return len(self.colors)



if __name__ == "__main__":
    print (P('g'))
    
