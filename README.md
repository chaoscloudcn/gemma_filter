# gemma_filter

最新的ComfyUI中使用 gemma4

使用ComfyUI-llama-cpp_vlm插件

下载gemma-4-E4B-it-GGUF模型

默认思考模型无法关闭，

为了更好的使用gemma4.所以制作这个

正则表达式，过滤

<|channel>thought....<channel|>思考的内容

=========================================================
下载gemma_filter.py 复制到 你的  custom_nodes 文件夹

重新ComfyUI，就可以使用这个最简单的插件了

=========================================================

只保留剩余的部分

![图片描述](https://github.com/chaoscloudcn/gemma_filter/blob/main/workflow(1).png?raw=true)

这个下载上面的工作流图片中带有ComfyUI工作流

==========================================================================================


