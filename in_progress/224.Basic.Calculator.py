class Solution:
    def calculate(self, s: str) -> int:
        total = -1
        mathstack = []
        # def evalfunc(pexpress):
        #     nonlocal total
        #     num_list = []
        #     temp_num = ''
        #     for char in pexpress:
        #         if char.isdigit():
        #             temp_num += char
        #         elif char == ' ':
        #             continue
        #         elif char == '+' or char == '-':
        #             num_list.append(temp_num)
        #             temp_num = ''
        #             temp_num = char
        #             num_list.append(temp_num)
        #             temp_num = ''

        #     for el in num_list:
        #         temp_total = 0
        #         sub = False
        #         if el.isdigit():
        #             if sub == True:
        #                 temp_total -= int(el)
        #                 sub = False
        #             else:
        #                 temp_total += int(el)
        #         elif el == '-':
        #             sub = True

        #         total += temp_total

        for idx, char in enumerate(s):
            if char == ')':
                if idx != 0:
                    if s[idx - 1] == '-':
                        neg = True

        return total


if __name__ == "__main__":
    # t = "(1+(4+5+2)-3)+(6+8)"
    w = " 2-1 + 2 "
    x = Solution()

    x.calculate(w)