from .modules.lich_nodes import NothingNode, ToLichPipe, FromLichPipe

NODE_CLASS_MAPPINGS = {
    "NothingNode": NothingNode,
    "ToLichPipe": ToLichPipe,
    "FromLichPipe": FromLichPipe,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "NothingNode": "Nothing Node",
    "ToLichPipe": "To Lich Pipe",
    "FromLichPipe": "From Lich Pipe",
}


print("\033[35m")
print("💀  Hello world!  💀")
print("\033[0m")
