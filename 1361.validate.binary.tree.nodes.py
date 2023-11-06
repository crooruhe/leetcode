from collections import defaultdict

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        childs = set(leftChild) | set(rightChild)
        print(childs)
        if n == 1: return True
        res = True
        tree = defaultdict(list)
        children = set()

        print('^^^^^^^^^^^^^^^^^^^^^')
        for index, (l, r) in enumerate(zip(leftChild, rightChild)):
            tree[index].append(l if l >= 0 else None)
            tree[index].append(r if r >= 0 else None)
            if l in children or r in children:
                # print('children', children)
                # print('parent', index, 'L', l, 'R', r)
                print('False -- multiple parents')
                print('-------------------------')
                return False
            if l >= 0:
                children.add(l)
            if r >= 0:
                children.add(r)

        root = []
        for n in tree:
            if n not in children:
                root.append(n)

        # print('r: ', root, ' children: ', children)

        if len(root) == 1:
            if root[0] in children:
                print('False -- Pointing to a parent')
                print('-------------------------')
                return False

        if (len(leftChild) - 1) not in children and (leftChild[(len(leftChild) - 1)] == -1 and rightChild[(len(leftChild) - 1)]):
            print('False -- Parentless node')
            print('-------------------------')
            return False

        # print('debug root', root)
        if len(root) > 1:
            print('False -- Too many roots')
            print('-------------------------')
            return False
        elif len(root) == 0:
            print('False -- No root')
            print('-------------------------')
            return False

        for index, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l == -1:
                l = None
            if r == -1:
                r = None
            if l != None and (leftChild[l] == index or rightChild[l] == index):
                print('False -- Pointing to parent lc')
                print('-------------------------')
                return False
            elif r != None and (leftChild[r] == index or rightChild[r] == index):
                print('False -- Pointing to parent rc')
                print('-------------------------')
                return False
        rt_len = 0
        def tRoot(rt):
            nonlocal rt_len
            if rt != -1:
                rt_len += 1
                tRoot(leftChild[rt])
                tRoot(rightChild[rt])
            return

        tRoot(root[0])
        
        if rt_len < len(leftChild):
            print('False -- Pointing to a parent')
            print('-------------------------')
            return False


        # while True:
        #     tortoise1 = leftChild[tortoise1]
        #     hare1 = leftChild[leftChild[hare1]]
        #     tortoise2 = rightChild[tortoise2]
        #     hare2 = rightChild[rightChild[hare2]]

        #     if tortoise == hare:
        #         print('False -- Pointing to a parent')
        #         print('-------------------------')
        #         return False



        


        print(True)
        print('-------------------------')
        return res

if __name__ == "__main__":
    x = Solution()
    n = 6
    l = [1,-1,-1,4,-1,-1]
    r = [2,-1,-1,5,-1,-1] # false
    n1 = 3
    l1 = [-1,2,-1]
    r1 = [2,-1,-1] # false
    n2 = 4
    l2 = [1,-1,3,-1]
    r2 = [2,3,-1,-1] # false
    n3 = 4
    l3 = [3,-1,1,-1]
    r3 = [-1,-1,0,-1] # true
    n4 = 10
    l4 = [1,6,3,4,7,-1,-1,-1,-1,-1]
    r4 = [5,2,9,-1,8,-1,-1,-1,-1,-1]  # true
    n5 = 2
    l5 = [-1,0]
    r5 = [-1,-1] # true
    n6 = 3
    l6 = [1,-1,0]
    r6 = [-1,-1,-1] # true
    n7 = 2
    l7 = [1,0]
    r7 = [-1,-1] # false
    n8 = 4
    l8 = [1,0,3,-1]
    r8 = [-1,-1,-1,-1] # false
    n9 = 4
    l9 = [1,2,0,-1]
    r9 = [-1,-1,-1,-1] # false
    n10 = 6
    l10 = [1,2,0,4,-1,-1]
    r10 = [-1,-1,-1,5,-1,-1] # false
    x.validateBinaryTreeNodes(n, l, r)
    x.validateBinaryTreeNodes(n1, l1, r1)
    x.validateBinaryTreeNodes(n2, l2, r2)
    x.validateBinaryTreeNodes(n3, l3, r3)
    x.validateBinaryTreeNodes(n4, l4, r4)
    x.validateBinaryTreeNodes(n5, l5, r5)
    x.validateBinaryTreeNodes(n6, l6, r6)
    x.validateBinaryTreeNodes(n7, l7, r7)
    x.validateBinaryTreeNodes(n8, l8, r8)
    x.validateBinaryTreeNodes(n9, l9, r9)
    x.validateBinaryTreeNodes(n10, l10, r10)


    # print('0')

    # # print('1')

    # # print('2')

    # # print('3')

    # # print('4')

    # # print('5')

    # # print('6')

    # # print('7')

    # # print('8')

    # # print('9')














