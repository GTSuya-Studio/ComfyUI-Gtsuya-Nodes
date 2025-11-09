# ComfyUI-GTSuya-Nodes

ComfyUI-GTSuya-Nodes is a ComfyUI extension designed to add several wildcards supports into [ComfyUI](https://github.com/comfyanonymous/ComfyUI). Wildcards allow you to use \_\_name__ syntax in your prompt to get a random line from a file named name.txt in a wildcards directory.

# Installation
To install ComfyUI-GTSuya-Nodes in addition to an existing installation of ComfyUI, you can follow the following steps:

1. cd custom_nodes
1. git clone https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes.git
1. Restart ComfyUI

# How to Use
## Wildcards / Simple wildcards (Dir.)
This node allows you to choose any directory on your hard drive containing your wildcards files. Those wildcards files don't need to be specifically into the ComfyUI root directory. To add **Simple wildcards (Dir.)** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Simple wildcards (Dir.).

![Simple wildcards (Dir.)](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/e9bb74e7-4496-4bba-8477-44dad4639f58)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcards as you want. Then indicate the path of the directory where your wildcards files are stored.

### New Features:
- **Nested Wildcards Support**: Wildcards files can now contain other wildcards that will be resolved recursively.
- **Wildcard Depth Control**: Use the `wildcard_depth` parameter (default: 50, range: 2-256) to control the maximum recursion depth and prevent infinite loops.
- **Comment Support**: Lines starting with `#` in your wildcards files are now ignored as comments.
- **Reproducible Results**: The `seed` parameter now ensures consistent random selections across runs.
- **Empty Lines Handling**: Empty lines in wildcards files are automatically filtered out.
- **Missing Wildcards Detection**: Wildcards that don't have a corresponding file remain visible in the output (e.g., `__missing__`) and trigger a warning in the console. This makes it easier to identify and fix missing wildcard files during debugging.

### Example of Nested Wildcards:
If you have a file **weather.txt** containing:
```
sunny day
__temperature__ weather
rainy afternoon
```

And a file **temperature.txt** containing:
```
cold
warm
hot
```

Using **\_\_weather__** in your prompt might result in "warm weather" through nested wildcard resolution.

## Wildcards / Simple wildcards
This node provides the same functionality as **Simple wildcards (Dir.)** but automatically uses the **wildcards** directory in the ComfyUI root folder. This node is kept for backward compatibility with existing workflows. **For new workflows, we recommend using Simple wildcards (Dir.) for more flexibility.**

To use this node, create a directory named **wildcards** into the ComfyUI root folder and put all your wildcards text files into it. Add a **Simple wildcards** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Simple wildcards.

![Simple wildcards](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/6f319087-3efb-4f63-8489-216909e64085)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcards as you want.

This node supports all the features listed above for **Simple wildcards (Dir.)**: nested wildcards, wildcard depth control, comment support, reproducible results, and automatic filtering of empty lines.

## Wildcards / Wildcards Nodes
This node allows to manage wildcards lists and values directly from ComfyUI workflows. It is not dependent anymore on external text files. This node must work in conjunction with **Random Line** nodes from [Hakkun-ComfyUI-nodes](https://github.com/tudal/Hakkun-ComfyUI-nodes) which return a random string from a list. To add **Wildcards Nodes** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Wildcards Nodes.

![Wildcards](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/3ff04623-c4ed-470a-b923-469c1d899991)

Enter your prompt into the text box. Wildcard entries (str#) must be indicated with double underscore around them and must correspond to the **Random Line** nodes linked to this entry. For example, if a **Random Line** node is linked to **str3**, the corresponding wildcard word must be **\_\_str3__**. You can actually use a maximum of 5 wildcards at the same time.

## Downloads / Danbooru (ID)
This node allows to automatically get image url and tags list from a post hosted on [Danbooru](https://danbooru.donmai.us/) website. This node could work in conjunction with **Load Image From URL** node from [comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture) nodes to import the corresponding image directly into ComfyUI. The tags list could be directly used as a prompt, or part of a prompt. To add **Danbooru (ID)** node: Right-click > Add Node > GtsuyaStudio > Downloads > Danbooru (ID).

![Capture d'écran 2023-11-26 165820](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/d09a0d22-7d87-4d03-8302-4d305f149f12)

The node can be used by indicating the ID number of the [Danbooru post](https://danbooru.donmai.us/posts) website.

## Downloads / Danbooru (Random)
This node allows to automatically get image url and tags list from a random post hosted on [Danbooru](https://danbooru.donmai.us/) website. It is also possible to restrict obtained results to a specific tag query. This node could work in conjunction with **Load Image From URL** node from [comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture) nodes to import the corresponding image directly into ComfyUI. The tags list could be directly used as a prompt, or part of a prompt. To add **Danbooru (Random)** node: Right-click > Add Node > GtsuyaStudio > Downloads > Danbooru (Random).

![Capture d'écran 2023-11-26 163744](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/d6d8fc8a-da16-4403-ab56-1343d00a56e5)

To use this node, you need a valid API key from [Danbooru](https://danbooru.donmai.us/) website. To obtain such API key, you need first to have a [Danbooru account](https://danbooru.donmai.us/users/new), then ask for a unique API key, and then give permission to use **posts:random** data. Once it is done, finally indicate your Danbooru login and API key number. The node is ready. The node can be used directly with the default settings. If you want to restrict results and obtain a tags list containing a specific tag, indicate this tag into the **tag_query** field. This tag must be a valid [Danbooru tag](https://danbooru.donmai.us/tags) website.

## Tools / Replace Strings
This node allows to automatically delete or replace some specific strings into a text or a prompt. To add **Replace Strings** node: Right-click > Add Node > GtsuyaStudio > Tools > Replace Strings.

![Capture d'écran 2023-12-01 202225](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/dc9409bf-1b12-4571-9deb-755e31e16281)

To use this node, you need to link inputs to 2 text nodes: **text** entry corresponds to the text where you want to replace or delete strings, and **replace_list** entry corresponds to the list of words that would be replaced. You have to set one string replacement per line. String replacement line must be like this: **string1|string2**, where **string1** is the string that will be replaced, and **string2** is the replacement string. If **string2** is not specified, **string1** will be deleted from the text.
 
## Tools / Random File From Path
This is a simple node that returns a random file path from a directory. In case of images, this node could work in conjunction with **Load Image From URL** node from [comfyui-art-venture](https://github.com/sipherxyz/comfyui-art-venture) nodes to import the corresponding image directly into ComfyUI. To add **Random File From Path** node: Right-click > Add Node > GtsuyaStudio > Tools > Random File From Path.

![Capture d'écran 2023-12-09 201515](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/480820a9-5a24-4a90-9eda-0de4e2143561)

To use this node you just have to indicate a directory path where the files you want to randomly select are located.

---

## Changelog

### Version 1.2.0
- **Nested wildcards support**: Wildcards can now reference other wildcards recursively
- **Wildcard depth control**: New `wildcard_depth` parameter to prevent infinite loops (default: 50, range: 2-256)
- **Comment filtering**: Lines starting with `#` are now treated as comments and ignored
- **Reproducible results**: Seed parameter now properly applied for consistent random selections
- **Improved file handling**: Better UTF-8 encoding support and automatic closure of file handles
- **Missing wildcards detection**: Non-existent wildcards remain visible in the output with console warnings for easier debugging
- **Empty lines filtering**: Empty lines in wildcards files are automatically skipped