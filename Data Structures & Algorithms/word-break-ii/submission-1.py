class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(i):
            # Reached the end
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            result = []

            # Try every possible next word
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word in word_set:
                    for sentence in dfs(j):
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[i] = result
            return result

        return dfs(0)