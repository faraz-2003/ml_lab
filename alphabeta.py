class TreeNode:
    def __init__(self,value,children=[]):
        self.value = value
        self.children = children
        self.alpha = float('-inf')
        self.beta = float('inf')

def alphabeta(node, depth,alpha,beta, maximizing_player):
    global pruned_count
    if depth == 0 or not node.children:
        return node.value,[node.value] 
    
    if maximizing_player:
        max_val = float('-inf')
        max_path = []
        for child in node.children:
            child_val,child_path = alphabeta(child,depth-1,alpha,beta,False)
            if child_val > max_val:
                max_val = child_val
                max_path = [node.value] + child_path
            alpha = max(alpha,max_val)
            if alpha >= beta:
                pruned_count+=len(child.children) +1
                break   
        return max_val,max_path
    else:
        min_val = float('inf')
        min_path = []
        for child in node.children:
            child_val,child_path = alphabeta(child,depth-1,alpha,beta,True)
            if child_val < min_val:
                min_val = child_val
                min_path = [node.value] + child_path
            beta = min(beta,min_val)
            if alpha >= beta:
                pruned_count+=len(child.children) +1
                break    
        return min_val,min_path     

tree = TreeNode(0 ,[
    TreeNode(1,[TreeNode(3),TreeNode(12)]),
    TreeNode(4,[TreeNode(8),TreeNode(2)])
])

'''tree = TreeNode(0, [
    TreeNode(0, [
        TreeNode(0,[
            TreeNode(3), TreeNode(5)
            ]),
        TreeNode(0,[
            TreeNode(6), TreeNode(9)
            ])
        ]),
    TreeNode(0, [
        TreeNode(0,[
            TreeNode(1), TreeNode(2)
            ]),
        TreeNode(0,[
            TreeNode(0), TreeNode(-1)
            ])
        ])
])'''

pruned_count = 0
path_value, path = alphabeta(tree,3,float('-inf'),float('inf'),True)
print(" with value: ",path_value)
print("The pruned count is : ",pruned_count)