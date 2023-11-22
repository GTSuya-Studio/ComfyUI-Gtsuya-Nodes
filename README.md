# ComfyUI-GTSuya-Nodes

ComfyUI-GTSuya-Nodes is a ComyUI extension designed to add several wildcards supports into [ComfyUI](https://github.com/comfyanonymous/ComfyUI). Wildcards allow you to use \_\_name__ syntax in your prompt to get a random line from a file named name.txt in a wildcards directory.

# Installation
To install ComfyUI-GTSuya-Nodes in addition to an existing installation of ComfyUI, you can follow the following steps:

1. cd custom_nodes
1. git clone https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes.git
1. Restart ComfyUI

# How to Use
## Simple wildcards
Create a directory named **wildcards** into the Comfyui root folder and put all your wildcards text files into it. Add a **Simple wildcards** node (Right-click > Add Node > GtsuyaStudio > wildcards > Simple wildcards).

![Capture d’écran 2023-11-19 192830](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/6f319087-3efb-4f63-8489-216909e64085)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcard as you want.

## Simple wildcards (Dir.)
This node is pretty similar to **Simple wildcards**. The only difference is that you can choose any directory on your hard drive containing your wildcards files. Those wildcards files don't need to be specificaly into the Comfyui root directory. To add **Simple wildcards (Dir.)** node (Right-click > Add Node > GtsuyaStudio > wildcards > Simple wildcards (Dir.)).

![Capture d’écran 2023-11-19 213659](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/e9bb74e7-4496-4bba-8477-44dad4639f58)

Enter your prompt into the text box. Wildcard words must be indicated with double underscore around them. For example, if your wildcards file is named **country.txt**, the corresponding wildcard word must be **\_\_country__**. You can add as many wildcard as you want. Then indicate the path of the directory where are stored your wildcards files.

## Wildcards
This node allows to manage wildcards lists and values directly from ComfyUI workflows. It is not dependent anymore of external text files. This node must work in conjunction with **Ramdom Line** nodes from [Hakkun-ComfyUI-nodes](https://github.com/tudal/Hakkun-ComfyUI-nodes) which return a ramdom string from a list. To add **Wildcards** node (Right-click > Add Node > GtsuyaStudio > wildcards > Wildcards).

![Capture d’écran 2023-11-19 231208](https://github.com/GTSuya-Studio/ComfyUI-Gtsuya-Nodes/assets/29682182/3ff04623-c4ed-470a-b923-469c1d899991)

Enter your prompt into the text box. Wildcard entries (srt#) must be indicated with double underscore around them and must correspond to the **Ramdom Line** nodes linked to this entry. For example, if a **Ramdom Line** nodes is linked to **str3**, the corresponding wildcard word must be **\_\_str3__**. You can actually use a maxiumum of 5 wildcards as the same time.
