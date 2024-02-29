from pathlib import Path
import json
import os
import sys


# Get the absolute path of the main module
main_module_path = os.path.abspath(sys.argv[0])
base_path = Path(os.path.dirname(main_module_path))

file_name = base_path / "config.xprjson"
json_data = ""
has_file_saved = False
file_list = {}

def load_file(state):
    from taipy.gui import get_module_context
    m = get_module_context(state)
    print(m)    
    fn = state.file_name
    jd = Path(fn).read_text()
    state.json_data = jd

def save_file(state, name, payload):
    if "data" not in payload:
        return
    with open(state.file_name, "w") as f:
        f.write(payload["data"])
        state.has_file_saved = True

# file should only be within base path
def select_file(state, name, payload):
    if "file_name" not in payload:
        return
    potential_file_path = base_path / payload['file_name']
    if potential_file_path.exists():
        state.file_name = str(potential_file_path)
        
def get_file_list(state, name):
    # Use glob to find .xprjson files directly within the base directory.
    file_names = [file.name for file in base_path.glob('*.xprjson')]
    file_list_obj = {
        'file_names': file_names,
        'base_path': str(base_path)
    }
    state.file_list = json.dumps(file_list_obj)

#FunctionJsonAdapter().register()

# Create a Page instance with the resource handler
#page = Page(PureHTMLResourceHandler())