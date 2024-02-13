# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = u.entropy2d(5,5)
    level1["smoking_info_gain"] = u.information_gain_split(5,5,4,1,1,4, "entropy")


    level1["cough"] = u.entropy2d(5,5)
    level1["cough_info_gain"] = u.information_gain_split(5,5,4,3,1,2, "entropy")

    level1["radon"] = u.entropy2d(5,5)
    level1["radon_info_gain"] = u.information_gain_split(5,5,2,0,3,5, "entropy")

    level1["weight_loss"] = u.entropy2d(5,5)
    level1["weight_loss_info_gain"] = u.information_gain_split(5,5,3,2,2,3, "entropy")

    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.

    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    level2_left["radon"] = u.entropy2d(4,1)
    level2_left["radon_info_gain"] = u.information_gain_split(4,1,1,0,3,1, "entropy")

    level2_left["cough"] = u.entropy2d(4,1)
    level2_left["cough_info_gain"] = u.information_gain_split(4,1,4,0,0,1, "entropy")

    level2_left["weight_loss"] = u.entropy2d(4,1)
    level2_left["weight_loss_info_gain"] = u.information_gain_split(4,1,2,0,2,1, "entropy")

    level2_right["radon"] = u.entropy2d(1,4)
    level2_right["radon_info_gain"] = u.information_gain_split(1,4,1,0,0,4, "entropy")

    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = -1.

    level2_right["weight_loss"] = u.entropy2d(1,4)
    level2_right["weight_loss_info_gain"] = u.information_gain_split(1,4,1,2,0,2, "entropy")

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    #
    #              Smoking
    #             /  \
    #            /    \  
    #           /      \
    #          /        \
    #       Cough      Radon
    #        / \        / \
    #       /   \      /   \
    #     "y"   "n"  "y"   "n"

    #where the left path implies "yes" and the right one is "no"
    tree = u.BinaryTree("smoking")
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    # Four leaves
    A.insert_left("y")
    A.insert_right("n")
    B.insert_left("y")
    B.insert_right("n")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0 # 100% accurate on training data

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    A = 0.41
    B = 0.46
    C = 0.13
    # Answers are floats
    answer["(a) entropy_entire_data"] = u.entropy_probs_3d(A, B, C)
    # Infogain
    answer["(b) x <= 0.2"] = u.information_gain_probs_3d(0.2,0.8,A,B,C, 0., .8, .2, .5125, .375, .1125)
    answer["(b) x <= 0.7"] = u.information_gain_probs_3d(0.7,0.3,A,B,C, .2857142857, .6571428571, 0.05714285714, .4, 0.3, 0.3)
    answer["(b) y <= 0.6"] = u.information_gain_probs_3d(0.6,0.4,A,B,C, .15, .7, .15, .8, .1, .1)
    print("layer 1")
    print(answer["(b) x <= 0.2"])
    print(answer["(b) x <= 0.7"])
    print(answer["(b) y <= 0.6"])
    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"



    #              y<=0.6
    #             /  \
    #            /    \
    #           /      \
    #          /        \
    #       x<=0.7     x<=0.2
    #        / \        / \
    #       /   \      /   \
    #      /     \    /     \
    #     /       \  /       \
    #   "B"  "y<=0.3""y<=0.8""A"
    #           / \   / \  
    #          /   \  /   \
    #        "A"  "C" "C"  "B"

    # Assume left means "true" and right means "false"
    # Leaves are always strings
    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y<=0.6")
    W = tree.insert_left("x<=0.7")
    W.insert_left("B")
    X = W.insert_right("y<=0.3")

    X.insert_left("A")
    X.insert_right("C")

    Y = tree.insert_right("x<=0.2")
    Y.insert_right("A")
    Z = Y.insert_left("y<=0.8")    

    Z.insert_left("C")
    Z.insert_right("B")

    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.
    answer["(d) Gini, Car type"] = 0.
    answer["(e) Gini, Shirt type"] = 0.

    answer["(f) attr for splitting"] = ""

    # Explanatory text string
    answer["(f) explain choice"] = ""

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = []

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = []
    answer["b: explain"] = ""

    answer["c"] = []
    answer["c: explain"] = ""

    answer["d"] = []
    answer["d: explain"] = ""

    answer["e"] = []
    answer["e: explain"] = ""

    answer["f"] = []
    answer["f: explain"] = ""

    answer["g"] = []
    answer["g: explain"] = ""

    answer["h"] = []
    answer["h: explain"] = ""

    answer["i"] = []
    answer["i: explain"] = ""

    answer["j"] = []
    answer["j: explain"] = ""

    answer["k"] = []
    answer["k: explain"] = ""

    answer["l"] = []
    answer["l: explain"] = ""

    answer["m"] = []
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = ""
    explain["a explain"] = ""

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = ""
    explain["b explain"] = ""

    explain["c similarity"] = ""
    explain["c similarity explain"] = ""

    explain["c difference"] = ""
    explain["c difference explain"] = ""

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 0.
    answer["b, info gain, Handedness"] = 0.

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = ""

    # answer is a float
    answer["d, gain ratio, ID"] = 0.
    answer["e, gain ratio, Handedness"] = 0.

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = ""

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

