#!/usr/bin/python3
""" pascal triangle module """


def pascal_triangle(n):
    """ pascal triangle function """
    ans = []
    for i in range(n):
        ans.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                ans[i].append(1)
            else:
                ans[i].append(ans[i-1][j-1] + ans[i-1][j])
    return ans
