import nodes
import os
import shutil
import glob
import re
import random
from urllib.request import urlopen
import json
import time

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
    CATEGORY = "GtsuyaStudio/Wildcards"
  
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
                    myline = random.choice(lines)
                print(myline)
                text = text.replace('__'+wildcard+'__',myline)

        return (text,seed)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class SimpleWildcardsDir:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "directory": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_text"
    CATEGORY = "GtsuyaStudio/Wildcards"
  
    def get_text(self, text, directory, seed):
        wildcards = re.findall('__(.*?)__', text)
        for wildcard in wildcards :
            if os.path.isfile(directory+'\\'+wildcard+'.txt'):
                lines = open(directory+'\\'+wildcard+'.txt').read().splitlines()
                print(lines)
                if not lines:
                    myline = ""
                else:
                    myline = random.choice(lines)
                print(myline)
                text = text.replace('__'+wildcard+'__',myline)

        return (text,seed)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class Wildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
            "optional": {
                "str1": ("STRING", {"forceInput": True}),
                "str2": ("STRING", {"forceInput": True}),      
                "str3": ("STRING", {"forceInput": True}),      
                "str4": ("STRING", {"forceInput": True}),      
                "str5": ("STRING", {"forceInput": True}),       
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Wildcards"

    def get_value(self, text, str1=None, str2=None, str3=None, str4=None, str5=None):

        if str1:
            text = text.replace('__str1__',str1)
        if str2:
            text = text.replace('__str2__',str2)
        if str3:
            text = text.replace('__str3__',str3)
        if str4:
            text = text.replace('__str4__',str4)
        if str5:
            text = text.replace('__str5__',str5)

        return (text,)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class GetFromDanbooru:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "query_tag": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }
        
    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("tags","img_url",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Get From"

    def get_value(self, seed, query_tag):
        login = "Gtsuya_Studio"
        api_key = "orhE6jtQE2mBNPUZeSNki2Dp"
        url = "https://danbooru.donmai.us/posts/random.json?login="+login+"&api_key="+api_key
        if query_tag != '':
            url = url+"&tags="+query_tag
        img_url = None
        while True:
            tags = None
            img_url = None
            with urlopen(url) as response :
                body = response.read()
                items = json.loads(body)
                try:
                    tags = items['tag_string']
                    img_url = items['file_url']
                except:
                    pass
                if tags and img_url :
                    break
        return (tags,img_url)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWildcards": "Simple Wildcards",
    "SimpleWildcardsDir": "Simple Wildcards (Dir.)",
    "Wildcards": "Wildcards",
    "GetFromDanbooru": "Get From Danbooru",
}
