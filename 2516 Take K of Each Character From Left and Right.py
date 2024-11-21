class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # count frequency
        freq = {"a": 0, "b": 0, "c": 0}
        for i in s:
            freq[i] += 1
        # check if possible
        if freq["a"] < k or freq["b"] < k or freq["c"] < k:
            return -1

        n = len(s)
        window = {"a": 0, "b": 0, "c": 0}
        l, max_window = 0, 0

        for r in range(n):
            window[s[r]] += 1
            while l <= r and (
                    freq["a"] - window["a"] < k or
                    freq["b"] - window["b"] < k or
                    freq["c"] - window["c"] < k
            ):
                window[s[l]] -= 1
                l += 1
            max_window = max(max_window, r - l + 1)
        return n - max_window