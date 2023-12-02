import os
import shutil

from .gtsuya_nodes import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique

NODE_CLASS_MAPPINGS = {
    "Simple Wildcards": SimpleWildcards,
    "Simple Wildcards (Dir.)": SimpleWildcardsDir,
    "Wildcards Nodes": WildcardsNodes,
    "Danbooru (Random)": DanbooruRandom,
    "Danbooru (ID)": DanbooruID,
    "Replace Strings": ReplaceStrings,
    }

__all__ = ['NODE_CLASS_MAPPINGS']

THIS_DIR=os.path.dirname(os.path.abspath(__file__))
DIR_PY=os.path.abspath(f'{THIS_DIR}/py')
DIR_WEB_JS=os.path.abspath(f'{THIS_DIR}/../../web/extensions/gtsuya_nodes')

print("gtsuya_nodes loading")
