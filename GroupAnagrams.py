from collections import Counter


class Solution(object):

    def groups(self, strs):
        words_group = {}
        for word in strs:
            group_key = "".join(sorted(word))
            if group_key not in words_group:
                words_group[group_key] = [word]
            else:
                words_group[group_key].extend([word])
        return words_group.values()


if __name__ == "__main__":
    str = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groups(str))
