"""
merge two array

"""


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        n1 = len(l1)
        n2 = len(l2)
        ls = []
        i = 0
        j = 0

        while i < n1 and j < n2:
            if l1[i] <= l2[j]:
                ls.append(l1[i])
                i += 1
            else:
                ls.append(l2[j])
                j += 1

        if i == n1:
            ls.extend(l2[j:])

        if j == n2:
            ls.extend(l1[i:])

        return ls

if __name__ == '__main__':
    s = Solution()
    r = s.mergeTwoLists([1,1,5, 45], [2,4,6, 9,23])
    print(r)

