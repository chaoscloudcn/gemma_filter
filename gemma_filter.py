import re

class GemmaThoughtFilter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "remove_thought"
    CATEGORY = "文本处理 (Text)"

    def remove_thought(self, text):
        if not text:
            return ("",)
            
        # 终极暴力匹配：用 .*? 代替所有可能出现的竖杠、斜杠等符号
        # 只要是被尖括号包裹的 channel + thought，到下一个包裹 channel 的尖括号，全部删除
        pattern = r"<.*?channel.*?>thought.*?<.*?channel.*?>\s*"
        clean_text = re.sub(pattern, "", text, flags=re.DOTALL | re.IGNORECASE)
        
        return (clean_text.strip(),)

# 注册节点
NODE_CLASS_MAPPINGS = {
    "GemmaThoughtFilter": GemmaThoughtFilter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GemmaThoughtFilter": "✂️ 过滤 Gemma 思考过程"
}