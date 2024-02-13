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
    raise "load_dict:: Error loading data"

def entropy2d(nb_y, nb_n)->float:
    ntot = nb_y + nb_n
    E = -(nb_y/ntot * log2(nb_y/ntot) + nb_n/ntot * log2(nb_n/ntot))
    return E

def entropy_probs_3d(prob_a, prob_b, prob_c)->float:
    E = -(prob_a * log2(prob_a) + prob_b * log2(prob_b) + prob_c * log2(prob_c))
    return E

def gini(nb_y, nb_n)->float:
    ntot = nb_y + nb_n
    G = 1 - (nb_y/ntot)**2 - (nb_n/ntot)**2
    return G

def information_gain_split(nb_y, nb_n, nb_y_left, nb_n_left, nb_y_right, nb_n_right, method)->float:
    if method == "entropy":
        E = entropy2d(nb_y, nb_n)
        E_left = entropy2d(nb_y_left, nb_n_left)
        E_right = entropy2d(nb_y_right, nb_n_right)
        E_tot = E - (nb_y_left + nb_n_left)/(nb_y + nb_n) * E_left - (nb_y_right + nb_n_right)/(nb_y + nb_n) * E_right
        return E_tot
    elif method == "gini":
        G = gini(nb_y, nb_n)
        G_left = gini(nb_y_left, nb_n_left)
        G_right = gini(nb_y_right, nb_n_right)
        G_tot = G - (nb_y_left + nb_n_left)/(nb_y + nb_n) * G_left - (nb_y_right + nb_n_right)/(nb_y + nb_n) * G_right
        return G_tot
    else:
        raise "Information Gain: method not recognized"

def information_gain_probs_3d(size_left,size_right,prob_a, prob_b, prob_c, prob_a_left, prob_b_left, prob_c_left, prob_a_right, prob_b_right, prob_c_right)->float:
    # Calculate the total entropy before the split
    E = entropy_probs_3d(prob_a, prob_b, prob_c)
    
    # Calculate the entropy of the left and right partitions
    E_left = entropy_probs_3d(prob_a_left, prob_b_left, prob_c_left)
    E_right = entropy_probs_3d(prob_a_right, prob_b_right, prob_c_right)
        
    # Calculate the weighted average of the entropies after the split
    weighted_entropy_after = (size_left * E_left) + (size_right * E_right)
    
    # Calculate the information gain
    gain = E - weighted_entropy_after
    return gain




def gain_ratio(nb_y, nb_n, nb_y_left, nb_n_left, nb_y_right, nb_n_right, method)->float:
    if method == "entropy":
        gain_split = information_gain_split(nb_y, nb_n, nb_y_left, nb_n_left, nb_y_right, nb_n_right, method)
        split_info = -((nb_y_left + nb_n_left)/(nb_y + nb_n) * log2((nb_y_left + nb_n_left)/(nb_y + nb_n)) + (nb_y_right + nb_n_right)/(nb_y + nb_n) * log2((nb_y_right + nb_n_right)/(nb_y + nb_n)))
        gain_ratio = gain_split/split_info
        return gain_ratio
    else:
        raise "Information Gain: method not recognized"


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
