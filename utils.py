import math
import pickle


def log2(x):
    if float(x) != 0.0:
        return math.log(x, 2)
    else:
        return 0.0

def save_dict(filenm, dct):
    with open(filenm, "wb") as file:
        pickle.dump(dct, file)


# Loading from a pickle file
def load_dict(filenm, dct):
    with open(filenm, "rb") as file:
        loaded_data = pickle.load(file)
        return loaded_data
    
def purity(class_nums, method="entropy", probabilistic=False):
    '''
    Inputs:
    - class_nums: list of integers, where each integer represents the number of instances of a classc
    - method: string, either "entropy" or "gini"
    - probabilistic: boolean, whether class_nums are probabilities or counts
    Outputs:
    - float, the purity of the class_nums
    '''
    if not probabilistic:
        total = sum(class_nums)
        probs = [val / total for val in class_nums] if total > 0 else [0] * len(class_nums)
    else:
        probs = class_nums  # Assuming class_nums are already probabilities
    
    if method == "entropy":
        return -sum(prob * log2(prob) for prob in probs if prob > 0)  # Ensure no log2(0)
    elif method == "gini":
        return 1 - sum(prob**2 for prob in probs)
    else:
        raise ValueError("Purity method not recognized")
    
def split_purity(splits_class_amounts, method="entropy", probabilistic=False, split_sizes=None):
    '''
    Calculates the weighted purity (either entropy or Gini) for a given split.

    Inputs:
    - splits_class_amounts: list of lists of integers or floats, where each sublist represents the counts (or probabilities if probabilistic=True) of each class for a specific split
    - method: string, either "entropy" or "gini", to specify the method used for calculating purity
    - probabilistic: boolean, indicating whether splits_class_amounts are given as probabilities (True) or counts (False)
    - split_sizes: list of floats, representing the relative size of each split (required if probabilistic=True)

    Outputs:
    - float, the weighted purity (entropy or Gini) of the given split
    '''
    if not probabilistic or split_sizes is None:
        total_instances = sum([sum(split) for split in splits_class_amounts])
    else:
        total_instances = sum(split_sizes)
    
    weighted_purity = 0
    for idx, split in enumerate(splits_class_amounts):
        split_purity_value = purity(split, method, probabilistic)
        if not probabilistic or split_sizes is None:
            weight = sum(split) / total_instances
        else:
            weight = split_sizes[idx] / total_instances
        weighted_purity += weight * split_purity_value
    return weighted_purity




def information_gain(original_class_amounts, splits_class_amounts, method="entropy", probabilistic=False, split_sizes=None):
    '''
    Calculates the information gain of a split, using either entropy or Gini index as the purity measure.

    Inputs:
    - original_class_amounts: list of integers or floats, representing the counts (or probabilities if probabilistic=True) of each class before the split
    - splits_class_amounts: list of lists of integers or floats, where each sublist represents the counts (or probabilities) of each class for a specific split
    - method: string, either "entropy" or "gini", to specify the method used for calculating purity
    - probabilistic: boolean, indicating whether class_nums are given as probabilities (True) or counts (False)
    - split_sizes: list of floats, representing the relative size of each split (required if probabilistic=True)

    Outputs:
    - float, the information gain from splitting the original dataset into the provided splits
    '''
    original_purity = purity(original_class_amounts, method, probabilistic)
    splits_purity = split_purity(splits_class_amounts, method, probabilistic, split_sizes)
    return original_purity - splits_purity


def gain_ratio(original_class_amounts, splits_class_amounts, method="entropy", probabilistic=False, split_sizes=None):
    '''
    Calculates the gain ratio of a split.

    Inputs:
    - original_class_amounts: list of integers or floats, representing the counts (or probabilities if probabilistic=True) of each class before the split
    - splits_class_amounts: list of lists of integers or floats, where each sublist represents the counts (or probabilities) of each class for a specific split
    - method: string, either "entropy" or "gini", to specify the method used for calculating purity
    - probabilistic: boolean, indicating whether class_nums are given as probabilities (True) or counts (False)

    Outputs:
    - float, the gain ratio, calculated as the information gain divided by the split information of the dataset split
    '''
    # Calculate information gain
    info_gain = information_gain(original_class_amounts, splits_class_amounts, method, probabilistic, split_sizes)
    
    # Calculate SplitInfo, ensuring compatibility with probabilistic inputs
    total_instances = sum([sum(split) for split in splits_class_amounts])
    split_info = 0
    for split in splits_class_amounts:
        split_proportion = sum(split) / total_instances
        if split_proportion > 0:
            split_info -= split_proportion * log2(split_proportion)

    # Avoid division by zero in case split_info is 0
    if split_info == 0:
        return 0
    
    return info_gain / split_info

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
            return self.left
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node
            return new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
            return self.right
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node
            return new_node

    def __repr__(self):
        return f"BinaryTree({self.value})"

    def __str__(self, level=0):
        ret = "\t" * level + repr(self) + "\n"
        if self.left is not None:
            ret += self.left.__str__(level + 1)
        if self.right is not None:
            ret += self.right.__str__(level + 1)
        return ret

    def print_tree(self):
        print(self.__str__())


# Example on how to create a binary tree
# A has two children: B and C
# B has two children: D and E
# C has two children: F and G
# Construct the binary tree:
def construct_binary_tree():
    root = BinaryTree("A")
    root.insert_left("B")
    root.insert_right("C")
    root.left.insert_left("D")
    root.left.insert_right("E")
    root.right.insert_left("F")
    root.right.insert_right("G")
    return root
