class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        arr = []
        for i in range(len(strs)):
            arr.append(str(len(strs[i])))
            arr.append(",")
        arr.append("#")
        for i in range(len(strs)):
            arr.append(str((strs[i])))
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        size = []
        curr_num = ""
        while s[i] != "#":
            if s[i] != ",":
                curr_num += s[i]
            else:
                size.append(int(curr_num))
                curr_num = ""
            i = i + 1
        i = i + 1
        out = []
        for k in range(len(size)):
            start = i
            end = i + size[k]
            word = s[start:end]
            out.append(word)
            i = end
        return out