import nodes
import os
import shutil
import glob
import re
import random

"""

    A set of custom nodes for ComfyUI - focused on wildcards utilities
    By GTSuya Studio

    Copyright (c) 2023  

"""

MANIFEST = {
    "name": "GTSuyaNodes",
    "version": (0,0,1),
    "author": "GTSuya Studio",
    "project": "",
    "description": " A set of custom nodes for ComfyUI - focused on wildcards utilities",
}

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class SimpleWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_text"
    CATEGORY = "gtsuya/wildcards"
  
    def get_text(self, text, seed):
        wildcards_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'\\wildcards'
        wildcards = re.findall('__(.*?)__', text)
        for wildcard in wildcards :
            if os.path.isfile(wildcards_path+'\\'+wildcard+'.txt'):
                lines = open(wildcards_path+'\\'+wildcard+'.txt').read().splitlines()
                print(lines)
                if not lines:
                    myline = ""
                else:
                    myline = random.choice(lines).lower()
                print(myline)
                text = text.replace('__'+wildcard+'__',myline)

        return (text,seed)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWildcards": "Simple Wildcards",
}
