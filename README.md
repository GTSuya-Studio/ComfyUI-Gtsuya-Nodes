# ComfyUI-GTSuya-Nodes

ComfyUI-GTSuya-Nodes is a ComyUI extension designed to add several wildcards supports into [ComfyUI](https://github.com/comfyanonymous/ComfyUI). Wildcards allow you to use \_\_name__ syntax in your prompt to get a random line from a file named name.txt in a wildcards directory.

# Installation
To install ComfyUI-GTSuya-Nodes in addition to an existing installation of ComfyUI, you can follow the following steps:

1. cd custom_nodes
1. git clone https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes.git
1. Restart ComfyUI

# How to Use
## Wildcards / Wildcards
This node allows to manage wildcards lists and values directly from ComfyUI workflows. It is not dependent anymore of external text files. This node must work in conjunction with **Ramdom Line** nodes from [Hakkun-ComfyUI-nodes](https://github.com/tudal/Hakkun-ComfyUI-nodes) which return a ramdom string from a list. To add **Wildcards** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Wildcards.

![Wildcards](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/3ff04623-c4ed-470a-b923-469c1d899991)

Enter your prompt into the text box. Wildcard entries (srt#) must be indicated with double underscore around them and must correspond to the **Ramdom Line** nodes linked to this entry. For example, if a **Ramdom Line** nodes is linked to **str3**, the corresponding wildcard word must be **\_\_str3__**. You can actually use a maxiumum of 5 wildcards as the same time.

## Wildcards / Simple wildcards
Create a directory named **wildcards** into the Comfyui root folder and put all your wildcards text files into it. Add a **Simple wildcards** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Simple wildcards.

![Simple wildcards](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/6f319087-3efb-4f63-8489-216909e64085)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcard as you want.

## Wildcards / Simple wildcards (Dir.)
This node is pretty similar to **Simple wildcards**. The only difference is that you can choose any directory on your hard drive containing your wildcards files. Those wildcards files don't need to be specificaly into the Comfyui root directory. To add **Simple wildcards (Dir.)** node: Right-click > Add Node > GtsuyaStudio > Wildcards > Simple wildcards (Dir.).

![Simple wildcards (Dir.)](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/e9bb74e7-4496-4bba-8477-44dad4639f58)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcard as you want. Then indicate the path of the directory where are stored your wildcards files.
## Dowmloads / Danbooru (Random)

This node allows to automaticaly get image url and tags list from a random post hosted on [Danbooru](https://danbooru.donmai.us/) website. It is also possible to restrict obtained results to a specific tag query. This node could work in conjunction with **Load Image From URL** node from [comfyui-art-venture]([https://github.com/tudal/Hakkun-ComfyUI-nodes](https://github.com/sipherxyz/comfyui-art-venture)) to import the corresponding image directly into ComfyUI. The tags list could be directly used as a prompt, or part of a prompt. To add **Danbooru (Random)** node: Right-click > Add Node > GtsuyaStudio > Downloads > Danbooru (Random).

![Capture d’écran 2023-11-26 163744](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/d6d8fc8a-da16-4403-ab56-1343d00a56e5)

To use this node, you need a valid API key from [Danbooru](https://danbooru.donmai.us/) website. To obtain such API key, you need first to have an [Danbooru account](https://danbooru.donmai.us/users/new), then ask for an unique API key, and then give permission to use **posts:random** data. Once it is done, finaly indicate your Danbooru login and API key number. TYhe node is ready. The node can be used directly with the default settings. If you want to restrict results and obtain a tags list containing a specific tag, indicate this tag into the **tag_query** field. This tag must be a valid [Danbooru tag]([https://danbooru.donmai.us/](https://danbooru.donmai.us/tags)https://danbooru.donmai.us/tags) website 
