"""
This problem was asked by Google.
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and
an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute
path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

import collections

def fn(filepath):

    # split by \n
    # make a graph, number of \t tells the level
    files = filepath.split('\n')
    num_tabs = {}
    adj = collections.defaultdict(list)
    names_to_node = {}
    node_to_names = {}
    index = 0
    for f in files:
        tab = 0
        i = 0
        while i <= len(f) and f[i] == "\t":
            tab += 1
            i += 1
        f = f[i:]
        names_to_node[f] = index
        node_to_names[index] = f
        num_tabs[tab] = f
        if tab-1 in num_tabs:
            parent = num_tabs[tab-1]
            adj[names_to_node[parent]].append(index)
            adj[index].append(names_to_node[parent])
        index += 1

    def dfs(i, char_depth):
        visited[i] = True
        char_depth += len(node_to_names[i])
        if '.' in node_to_names[i]:
            res.append(char_depth)

        for nei in adj[i]:
            if not visited[nei]:
                dfs(nei, char_depth + 1)    # add 1 for '/'

    visited = [False]*(len(adj))
    res = []
    dfs(0, 0)
    return max(res)


if __name__ == '__main__':
    res = fn("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(res)