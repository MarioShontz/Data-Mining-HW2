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

    # Smoking attribute
    original_class_amounts = [5, 5]
    smoking_splits = [[4, 1], [1, 4]]
    level1["smoking"] = u.split_purity(smoking_splits)
    level1["smoking_info_gain"] = u.information_gain(original_class_amounts, smoking_splits)

    # Cough attribute
    cough_splits = [[4, 3], [1, 2]]
    level1["cough"] = u.split_purity(cough_splits)
    level1["cough_info_gain"] = u.information_gain(original_class_amounts, cough_splits)

    # Radon attribute
    radon_splits = [[2, 0], [3, 5]]
    level1["radon"] = u.split_purity(radon_splits)
    level1["radon_info_gain"] = u.information_gain(original_class_amounts, radon_splits)

    # Weight Loss attribute
    weight_loss_splits = [[3, 2], [2, 3]]
    level1["weight_loss"] = u.split_purity(weight_loss_splits)
    level1["weight_loss_info_gain"] = u.information_gain(original_class_amounts, weight_loss_splits)

    #use smoking splits for level 2
    left_class_amounts = [4, 1]
    right_class_amounts = [1, 4]
    # Level 2 Left - Smoking
    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.

    # Level 2 Right - Smoking
    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    # Assuming `u` refers to the utilities module with your defined functions

    # Level 2 Left - Radon
    radon_left_splits = [[1, 0], [3, 1]]
    level2_left["radon"] = u.split_purity(radon_left_splits)
    level2_left["radon_info_gain"] = u.information_gain(left_class_amounts, radon_left_splits)

    # Level 2 Left - Cough
    # Here, we need to define cough splits for the left side; assuming the placeholder `_splits` meant this:
    cough_left_splits = [[4, 0], [0, 1]]  # Assuming example values based on left_class_amounts
    level2_left["cough"] = u.split_purity(cough_left_splits)
    level2_left["cough_info_gain"] = u.information_gain(left_class_amounts, cough_left_splits)

    # Level 2 Left - Weight Loss
    # Assuming example values for weight loss splits on the left side
    weight_loss_left_splits = [[2, 0], [2, 1]]  # Assuming example values based on left_class_amounts
    level2_left["weight_loss"] = u.split_purity(weight_loss_left_splits)
    level2_left["weight_loss_info_gain"] = u.information_gain(left_class_amounts, weight_loss_left_splits)

    # Level 2 Right - Radon
    # Assuming radon splits for the right side need to be defined similarly:
    radon_right_splits = [[1, 0], [0, 4]]  # Example values for right_class_amounts
    level2_right["radon"] = u.split_purity(radon_right_splits)
    level2_right["radon_info_gain"] = u.information_gain(right_class_amounts, radon_right_splits)

    # Level 2 Right - Weight Loss
    # Assuming weight loss splits for the right side:
    weight_loss_right_splits = [[1, 2], [0, 2]]  # Example values for right_class_amounts
    level2_right["weight_loss"] = u.split_purity(weight_loss_right_splits)
    level2_right["weight_loss_info_gain"] = u.information_gain(right_class_amounts, weight_loss_right_splits)

    # Level 2 Right - Cough
    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = -1.
    
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
    answer["training_error"] = 0. # 100% accurate on training data

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    A = 0.41
    B = 0.46
    C = 0.13
    dataset_probs = [A, B, C]
    # Answers are floats
    answer["(a) entropy_entire_data"] = u.purity(dataset_probs, probabilistic=True)
    # Infogain
    # x <= 0.2
    split_sizes = [0.2, 0.8]
    splits = [[0., 0.8, 0.2], [0.5125, 0.375, 0.1125]]
    answer["(b) x <= 0.2"] = u.information_gain(dataset_probs, splits, probabilistic=True, split_sizes = split_sizes)
    # x <= 0.7
    split_sizes = [0.7, 0.3]
    splits = [[0.2857142857, 0.6571428571, 0.05714285714], [0.4, 0.3, 0.3]]
    answer["(b) x <= 0.7"] = u.information_gain(dataset_probs, splits, probabilistic=True, split_sizes = split_sizes)

    # y <= 0.6
    split_sizes = [0.6, 0.4]
    splits = [[.15, .7, .15], [.8, .1, .1]]
    answer["(b) y <= 0.6"] = u.information_gain(dataset_probs, splits, probabilistic=True, split_sizes = split_sizes)

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
    #   "B"  "y<=0.30.y<=0.80.A"
    #           / \   / \  
    #          /   \ /   \
    #        "A" "C" "C" "B"

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
    overall = [10,10]
    answer["(a) Gini, overall"] = u.purity(overall, method="gini")

    # float
    id_splits = [[1, 0]]*10 + [[0, 1]]*10
    answer["(b) Gini, ID"] = u.split_purity(id_splits, method="gini")
    
    gender_splits = [[6,4],[4,6]]
    answer["(c) Gini, Gender"] = u.split_purity(gender_splits, method="gini")

    car_type_splits = [[1,3],[8,0],[1,7]]
    answer["(d) Gini, Car type"] = u.split_purity(car_type_splits, method="gini")

    shirt_size_splits = [[3,2],[3,4],[2,2],[2,2]]
    answer["(e) Gini, Shirt type"] = u.split_purity(shirt_size_splits, method="gini")


    answer["(f) attr for splitting"] = "ID"

    # Explanatory text string
    answer["(f) explain choice"] = """While not really a great choice, if one
    is only interested in the choice the minimizes the gini, separating it
    by ID gets the job done the best. Of course, a more intelligent option would
    not just call every data point a cluster, i.e. to separate by Car Type."""

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

    answer["a"] = ["binary", "qualitative", "nominal"]
    answer["a: explain"] = "Time in AM or PM is binary (two distinct categories) and nominal without inherent order."

    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = "Brightness measured by a light meter can vary continuously and has a true zero, making it a ratio."

    answer["c"] = ["discrete", "qualitative", "ordinal"]
    answer["c: explain"] = "Peoples' judgments of brightness are subjective, ranked but not measured precisely, hence ordinal."

    answer["d"] = ["continuous", "quantitative", "interval"]
    answer["d: explain"] = "Angles in degrees have a meaningful scale but no true zero, making them interval."

    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = "Medals have a clear ordering (gold is higher than silver, and silver is higher than bronze) but are not numeric."

    answer["f"] = ["continuous", "quantitative", "ratio"]
    answer["f: explain"] = "Height above sea level can vary continuously and has a true zero point."

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = "Number of patients is a countable quantity with a true zero, making it a ratio."

    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = "ISBN numbers categorize books uniquely without a numeric value or order, making them nominal."

    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "The ability to pass light has a clear order (transparent > translucent > opaque) but is not numeric."

    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = "Military rank has a clear hierarchy (ordering) but is not measured quantitatively."

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "Distance can vary continuously and has a true zero, making it a ratio."

    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = "Density is a continuous measure with a true zero, categorized as a ratio."

    answer["m"] = ["discrete", "quantitative", "ordinal"]
    answer["m: explain"] = "Coat check numbers are unique identifiers but also follow an order; however, the number itself doesn't hold quantitative value beyond order."

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2 performs better on unseen data (Dataset B) \
    and also performs more similarly to the training data (Dataset A)."
    
    explain["b"] = "Model 1"
    explain["b explain"] = "Despite Model 2 having slightly less variance in performance between training and testing, " \
    "Model 1 shows higher overall accuracy when tested on the entire dataset (A+B), suggesting it may generalize better overall."

    # For part (c)
    explain["c similarity"] = "Both consider model complexity."
    explain["c similarity explain"] = "Both MDL and the pessimistic error estimate are methods that take into account " \
    "the complexity of the model when evaluating its performance, helping to avoid overfitting by penalizing overly complex models."

    explain["c difference"] = "MDL focuses on the total description length, while pessimistic error estimate adjusts the tree's error rate."
    explain["c difference explain"] = "MDL incorporates model complexity by considering the total description length " \
    "of the model and the data it describes, aiming for a balance between model simplicity and fit to the data. " \
    "In contrast, the pessimistic error estimate directly adjusts the error rate of the decision tree based on its complexity, " \
    "typically by adding a penalty for the number of leaves or nodes, which may lead to pruning of the tree."

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = 0.
    answer["a, level 2, right"] =0.
    answer["a, level 2, left"] = 0.
    answer["a, level 3, left"] = 0.
    answer["a, level 3, right"] = 0.

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
    answer["c, which attrib"] = 0.

    # answer is a float
    answer["d, gain ratio, ID"] = 0.
    answer["e, gain ratio, Handedness"] = 0.

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = 0.

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

