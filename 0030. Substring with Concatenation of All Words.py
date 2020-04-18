from typing import List


from collections import Counter
class Solution:
    def match(self, s, words, word_len):
        used = Counter()
        for index in range(len(s))[::word_len]:
            token = s[index:index+word_len]
            if used[token] < words[token]:
                used[token] += 1
            else:
                return False
        return all(used[word] == words[word] for word in words)


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []

        indexes = []
        word_count = len(words)
        word_len = len(words[0])
        matched_len = word_count * word_len
        words = Counter(words)

        for index in range(len(s)):
            if self.match(s[index:index+matched_len], words, word_len):
                indexes.append(index)
        return indexes


def test(*args):
    s = Solution()
    ans = s.findSubstring(*args)
    print(args, "ans=", ans)


if __name__ == "__main__":
    test("barfoothefoobarman", ["foo", "bar"])
    test("wordgoodgoodgoodbestword", ["word","good","best","word"])
