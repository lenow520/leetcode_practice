from sys import stdin, setrecursionlimit
 
setrecursionlimit(10**6)

class Tree():
    def __init__(self, num):
        self.num = num+1
        self.parents = [-1]*self.num
        self.subtreesize = [1]*self.num
        

    def findroot(self, nodeid):
        if self.parents[nodeid] == -1:
            # print(nodeid,"'s root:",nodeid)
            return nodeid
        else:
            self.parents[nodeid] = self.findroot(self.parents[nodeid])
            rootid = self.parents[nodeid]
            # print(nodeid,"'s root:",rootid)
            return rootid

    def connectsubtree(self, uroot, vroot):
        # uroot = self.findroot(u)
        # vroot = self.findroot(v)
        if uroot != vroot:
            if self.subtreesize[uroot] < self.subtreesize[vroot]:
                uroot, vroot = vroot, uroot
 
            self.subtreesize[uroot] += self.subtreesize[vroot]
            self.parents[vroot] = uroot


def MaxSumWeight(node_num, edges):
    ans = 0
    tree = Tree(node_num)
    edges.sort(key=lambda tuple: tuple[2])
    for u, v, w in edges:
        uroot = tree.findroot(u)
        vroot = tree.findroot(v)
        # print(tree.subtreesize)
        ans += w * tree.subtreesize[uroot] * tree.subtreesize[vroot]
        tree.connectsubtree(uroot,vroot)
        
    return ans
