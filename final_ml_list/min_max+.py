class TreeNode:
    def __init__(self,value,children=[]):
        self.value = value
        self.children = children

def min_max(node, depth, maximizing_player):
    if depth == 0 or not node.children:
        return node.value,[node.value] 
    
    if maximizing_player:
        max_val = float('-inf')
        max_path = []
        for child in node.children:
            child_val,child_path = min_max(child,depth-1,False)
            if child_val > max_val:
                max_val = child_val
                max_path = [node.value] + child_path
        return max_val,max_path
    else:
        min_val = float('inf')
        min_path = []
        for child in node.children:
            child_val,child_path = min_max(child,depth-1,True)
            if child_val < min_val:
                min_val = child_val
                min_path = [node.value] + child_path
        return min_val,min_path     

tree = TreeNode(0 ,[
    TreeNode(1,[TreeNode(3),TreeNode(12)]),
    TreeNode(4,[TreeNode(8),TreeNode(2)])
])

path_value, path = min_max(tree,2,True)
print("The path is: ",path," with value: ",path_value)

#b) Heat Map

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("./ToyotaCorolla.csv")

sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet')
plt.show()