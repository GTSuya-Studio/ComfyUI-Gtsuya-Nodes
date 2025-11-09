import os
import re
import random
import json
from pathlib import Path
from urllib.request import urlopen
from typing import Tuple, Optional

"""
A set of small custom nodes for ComfyUI, focused on automatic prompt generation and wildcards utilities
By GTSuya Studio

Copyright (c) 2025
"""

MANIFEST = {
    "name": "GTSuyaNodes",
    "version": (1, 2, 2),
    "author": "GTSuya Studio",
    "project": "",
    "description": "A set of small custom nodes for ComfyUI, focused on automatic prompt generation and wildcards utilities",
}

# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class SimpleWildcards:
    """Process wildcards with default directory"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "wildcard_depth": ("INT", {"default": 50, "min": 2, "max": 256}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_text"
    CATEGORY = "GtsuyaStudio/Wildcards"

    def get_text(self, text: str, seed: int, wildcard_depth: int) -> Tuple[str]:
        default_directory = Path(__file__).parent.parent.parent / "wildcards"
        
        wildcard_dir = SimpleWildcardsDir()
        return wildcard_dir.get_text(text, str(default_directory), seed, wildcard_depth)


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class SimpleWildcardsDir:
    """Process wildcards with custom directory"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "directory": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "wildcard_depth": ("INT", {"default": 50, "min": 2, "max": 256}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_text"
    CATEGORY = "GtsuyaStudio/Wildcards"

    def get_text(self, text: str, directory: str, seed: int, wildcard_depth: int) -> Tuple[str]:
        random.seed(seed)
        wildcards_path = Path(directory)

        if not wildcards_path.exists():
            print(f"Warning: Wildcards directory not found: {directory}")
            return (text,)

        iteration = 0
        processed_wildcards = set()

        while iteration < wildcard_depth:
            wildcards = re.findall(r'__(.*?)__', text)
            
            wildcards = [w for w in wildcards if w not in processed_wildcards]
            
            if not wildcards:
                break

            found_any = False
            
            for wildcard in wildcards:
                wildcard_file = wildcards_path / f"{wildcard}.txt"
                
                if wildcard_file.is_file():
                    try:
                        with open(wildcard_file, 'r', encoding='utf-8') as f:
                            lines = f.read().splitlines()
                        
                        lines = [line for line in lines if line.strip() and not line.strip().startswith("#")]

                        if lines:
                            chosen_line = random.choice(lines)
                            text = text.replace(f'__{wildcard}__', chosen_line, 1)
                            found_any = True
                        else:
                            text = text.replace(f'__{wildcard}__', '', 1)
                            processed_wildcards.add(wildcard)
                            
                    except Exception as e:
                        print(f"Error reading wildcard file {wildcard}.txt: {e}")
                        processed_wildcards.add(wildcard)
                else:
                    processed_wildcards.add(wildcard)
                    print(f"Warning: Wildcard file not found: {wildcard}.txt")

            if not found_any:
                break

            iteration += 1

        if iteration >= wildcard_depth:
            remaining_wildcards = re.findall(r'__(.*?)__', text)
            if remaining_wildcards:
                print(f"Warning: Wildcard depth limit reached ({wildcard_depth}). "
                      f"Possible infinite loop or deeply nested wildcards. "
                      f"Remaining: {remaining_wildcards}")

        return (text,)


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class WildcardsNodes:
    """Replace custom wildcard placeholders with provided strings"""
    
    @classmethod
    def INPUT_TYPES(cls):
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

    def get_value(self, text: str, str1: Optional[str] = None, str2: Optional[str] = None,
                  str3: Optional[str] = None, str4: Optional[str] = None,
                  str5: Optional[str] = None) -> Tuple[str]:
        
        replacements = {
            '__str1__': str1,
            '__str2__': str2,
            '__str3__': str3,
            '__str4__': str4,
            '__str5__': str5,
        }

        for placeholder, value in replacements.items():
            if value is not None:
                text = text.replace(placeholder, value)

        return (text,)


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class DanbooruRandom:
    """Fetch random image and tags from Danbooru"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "query_tag": ("STRING", {"default": ""}),
                "login": ("STRING", {"default": ""}),
                "api_key": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("tags", "img_url",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Downloads"

    def get_value(self, seed: int, query_tag: str, login: str, api_key: str) -> Tuple[str, str]:
        url = f"https://danbooru.donmai.us/posts/random.json?login={login}&api_key={api_key}"
        
        if query_tag.strip():
            url += f"&tags={query_tag}"

        max_retries = 10
        retry_count = 0

        while retry_count < max_retries:
            try:
                with urlopen(url, timeout=30) as response:
                    body = response.read()
                    items = json.loads(body)
                    
                    tags = items.get('tag_string')
                    img_url = items.get('file_url')
                    
                    if tags and img_url:
                        return (tags, img_url)
                    
            except Exception as e:
                print(f"Error fetching from Danbooru (attempt {retry_count + 1}): {e}")
            
            retry_count += 1

        raise RuntimeError(f"Failed to fetch valid data from Danbooru after {max_retries} attempts")


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class DanbooruID:
    """Fetch specific image and tags from Danbooru by post ID"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "post_id": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("tags", "img_url",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Downloads"

    def get_value(self, post_id: str) -> Tuple[str, str]:
        if not post_id.strip():
            raise ValueError("Post ID cannot be empty")

        url = f"https://danbooru.donmai.us/posts/{post_id}.json"

        try:
            with urlopen(url, timeout=30) as response:
                body = response.read()
                items = json.loads(body)
                
                tags = items.get('tag_string')
                img_url = items.get('file_url')
                
                if tags and img_url:
                    return (tags, img_url)
                else:
                    raise ValueError(f"Post {post_id} does not have valid tags or image URL")
                    
        except Exception as e:
            raise RuntimeError(f"Error fetching Danbooru post {post_id}: {e}")


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class ReplaceStrings:
    """Replace strings based on a replacement list"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": ""}),
                "replace_list": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Tools"

    def get_value(self, text: str, replace_list: str) -> Tuple[str]:
        for line in replace_list.splitlines():
            line = line.strip()
            if not line:
                continue
                
            parts = line.split("|", 1)
            if len(parts) == 2:
                old_str, new_str = parts
                text = text.replace(old_str, new_str)
            else:
                print(f"Warning: Invalid replacement format (expected 'old|new'): {line}")

        text = ' '.join(text.split())
        
        return (text,)


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class RandomFileFromPath:
    """Select a random file from a directory"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "directory": ("STRING", {"default": ""}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "get_value"
    CATEGORY = "GtsuyaStudio/Tools"

    def get_value(self, seed: int, directory: str) -> Tuple[str]:
        random.seed(seed)
        
        directory_path = Path(directory)
        
        if not directory_path.exists():
            raise ValueError(f"Directory does not exist: {directory}")
        
        if not directory_path.is_dir():
            raise ValueError(f"Path is not a directory: {directory}")

        files = [f for f in directory_path.iterdir() if f.is_file()]
        
        if not files:
            raise ValueError(f"No files found in directory: {directory}")

        chosen_file = random.choice(files)
        
        return (str(chosen_file),)


# ---------------------------------------------------------------------------------------------------------------------------------------------------#
# Node display names mapping


NODE_CLASS_MAPPINGS = {
    "SimpleWildcards": SimpleWildcards,
    "SimpleWildcardsDir": SimpleWildcardsDir,
    "WildcardsNodes": WildcardsNodes,
    "DanbooruRandom": DanbooruRandom,
    "DanbooruID": DanbooruID,
    "ReplaceStrings": ReplaceStrings,
    "RandomFileFromPath": RandomFileFromPath,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleWildcards": "Simple Wildcards",
    "SimpleWildcardsDir": "Simple Wildcards (Dir.)",
    "WildcardsNodes": "Wildcards Nodes",
    "DanbooruRandom": "Danbooru (Random)",
    "DanbooruID": "Danbooru (ID)",
    "ReplaceStrings": "Replace Strings",
    "RandomFileFromPath": "Random File From Path",
}
