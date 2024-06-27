from .modules import lich_nodes as ln

NODE_CLASS_MAPPINGS = {
    "NothingNode": ln.NothingNode,
    "ToLichPipe": ln.ToLichPipe,
    "FromLichPipe": ln.FromLichPipe,
    "WidgetInputs": ln.WidgetInputs,
    "PrimitiveInputs": ln.PrimitiveInputs,
    "DreamLoader": ln.DreamLoader,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NothingNode": "Nothing Node",
    "ToLichPipe": "To Lich Pipe",
    "FromLichPipe": "From Lich Pipe",
    "WidgetInputs": "Widget Inputs",
    "PrimitiveInputs": "Primitive Inputs",
    "DreamLoader": "Dream Loader",
}


print("\033[35m")
print("💀  Hello world!  💀")
print("\033[0m")
