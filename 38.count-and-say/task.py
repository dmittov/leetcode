class Solution:

    def __apply(self, x: str):
        state = x[0]
        cnt = 1
        result = []
        for next_x in x[1:]:
            if next_x == state:
                cnt += 1
            else:
                result.append((state, cnt))
                state = next_x
                cnt = 1
        result.append((state, cnt))
        return result

    def __encode(self, result):
        return "".join(f"{cnt}{state}" for state, cnt in result)

    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = self.__encode(self.__apply(result))
        return result
