import numpy as np
import itertools
import time

# funcrions return 4 elements: max value, result list, execution time and time complexity

# KNAPSACK PROBLEM ALGORITHMS
def knapsackDynamic(val, wt, W):
    n = min(len(wt), len(val))
    start_time = time.time()

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    included = [[False for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                included[i][w] = False
            elif wt[i - 1] <= w:
                if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                    K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                    included[i][w] = True
                else:
                    K[i][w] = K[i - 1][w]
                    included[i][w] = False
            else:
                K[i][w] = K[i - 1][w]
                included[i][w] = False

    # Backtrack to retrieve the selected items
    selected_items = []
    current_capacity = W
    current_item_index = n

    while current_item_index > 0:
        if included[current_item_index][current_capacity]:
            selected_items.append(current_item_index - 1)
            current_capacity -= wt[current_item_index - 1]
        current_item_index -= 1

    end_time = time.time()
    exec_time = end_time - start_time
    selected_items = sorted(selected_items)
    return int(K[n][W]), selected_items, exec_time, "O(n*W)"


def knapsack_brute_force(val, wt, W):
   n = min(len(wt), len(val))
   best_value = 0
   best_combination = []

   start_time = time.time()

   for r in range(1, n + 1):
       for combination in itertools.combinations(range(n), r): # combinations function from Python's built-in itertools module generates all possible combinations of items.
           total_weight = sum(wt[i] for i in combination)
           total_value = sum(val[i] for i in combination)
           if total_weight <= W and total_value > best_value:
               best_value = total_value
               best_combination = list(combination)

   end_time = time.time()
   execution_time = end_time - start_time
   time_complexity = "O(2^n)"
   best_combination = sorted(best_combination)
   return best_value, best_combination, execution_time, time_complexity

class Priority_Queue:
    def __init__(self):
        self.pqueue = []
        self.length = 0

    def insert(self, node, val, wt, W, maxprofit):
        node.bound = get_bound(node, val, wt, W)
        if node.bound > maxprofit:  # Only insert if potential for better solution
            i = 0
            while i < len(self.pqueue):
                if self.pqueue[i].bound > node.bound:
                    break
                i += 1
            self.pqueue.insert(i, node)
            self.length += 1

    def remove(self):
        try:
            result = self.pqueue.pop()
            self.length -= 1
        except:
            print("Priority queue is empty, cannot pop from empty list.")
        else:
            return result


class Node:
    def __init__(self, level, profit, weight):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.items = []


def get_bound(node, val, wt, W):
    if node.weight >= W:
        return 0
    else:
        result = node.profit
        j = node.level + 1
        totweight = node.weight
        while j <= len(val) - 1 and totweight + wt[j] <= W:
            totweight = totweight + wt[j]
            result = result + val[j]
            j += 1
        k = j
        if k <= len(val) - 1:
            result = result + (W - totweight) * (val[k] / wt[k])
        return result


def knapsackBnB(val, wt, W):
 start_time = time.time()
 nodes_generated = 0
 pq = Priority_Queue()

 v = Node(-1, 0, 0) # v initialized to be the root with level = 0, profit = $0, weight = 0
 nodes_generated+=1
 maxprofit = 0 # maxprofit initialized to $0
 v.bound = get_bound(v, val, wt, W)

 pq.insert(v, val, wt, W, maxprofit)

 while pq.length != 0:
     v = pq.remove() #remove node with best bound

     if v.bound > maxprofit: #check if node is still promising
         #set u to the child that includes the next item
         u = Node(0, 0, 0)
         nodes_generated+=1
         u.level = v.level + 1
         u.profit = v.profit + val[u.level]
         u.weight = v.weight + wt[u.level]
         #take v's list and add u's list
         u.items = v.items.copy()
         u.items.append(u.level) # adds next item
         if u.weight <= W and u.profit > maxprofit:
             #update maxprofit
             maxprofit = u.profit
             bestitems = u.items
         u.bound = get_bound(u, val, wt, W)
         if u.bound > maxprofit:
             pq.insert(u, val, wt, W, maxprofit)
     #set u to the child that does not include the next item
     u2 = Node(u.level, v.profit, v.weight)
     nodes_generated+=1
     u2.bound = get_bound(u2, val, wt, W)
     u2.items = v.items.copy()
     if u2.bound > maxprofit:
         pq.insert(u2, val, wt, W, maxprofit)
     end_time = time.time()
     exec_time = end_time - start_time
    
 return maxprofit, bestitems, exec_time, "Od O(N) do O(2^N)"

def knapsackBnB_sorted(val, wt, W):
    # This function helps in optimizing the execution time of the BnB algorithm
    combined = list(zip(range(len(val)), val, wt, [v / w for v, w in zip(val, wt)], [0] * len(val)))
    print(f"combined: {combined}")
    # Sort the list of tuples in descending order based on the value/weight ratio
    sorted_combined = sorted(combined, key=lambda x: x[3], reverse=True)


    # Update the last element of each tuple to be its index in the sorted list
    for i, tup in enumerate(sorted_combined):
        sorted_combined[i] = tup[:-1] + (i,)
    print(f"sorted_combined: {sorted_combined}")
    new_val = [tup[1] for tup in sorted_combined]
    new_wt = [tup[2] for tup in sorted_combined]

    maxprofit, indexes, exec_time, message = knapsackBnB(new_val, new_wt, W)
    first_elements = sorted([sorted_combined[i][0] for i in indexes])
    return maxprofit, first_elements, exec_time, message


# ASSIGNMENT PROBLEM ALGORITHMS


def min_zero_row(zero_mat, mark_zero):
    '''
    The function can be splitted into two steps:
    #1 The function is used to find the row which containing the fewest 0.
    #2 Select the zero number on the row, and then marked the element corresponding row and column as False
    '''

    # Find the row
    min_row = [99999, -1]

    for row_num in range(zero_mat.shape[0]):
        if np.sum(zero_mat[row_num] == True) > 0 and min_row[0] > np.sum(zero_mat[row_num] == True):
            min_row = [np.sum(zero_mat[row_num] == True), row_num]

    # Marked the specific row and column as False
    zero_index = np.where(zero_mat[min_row[1]] == True)[0][0]
    mark_zero.append((min_row[1], zero_index))
    zero_mat[min_row[1], :] = False
    zero_mat[:, zero_index] = False


def mark_matrix(mat):
    '''
    Finding the returning possible solutions for LAP problem.
    '''

    # Transform the matrix to boolean matrix(0 = True, others = False)
    cur_mat = mat
    zero_bool_mat = (cur_mat == 0)
    zero_bool_mat_copy = zero_bool_mat.copy()

    # Recording possible answer positions by marked_zero
    marked_zero = []
    while (True in zero_bool_mat_copy):
        min_zero_row(zero_bool_mat_copy, marked_zero)

    # Recording the row and column positions seperately.
    marked_zero_row = []
    marked_zero_col = []
    for i in range(len(marked_zero)):
        marked_zero_row.append(marked_zero[i][0])
        marked_zero_col.append(marked_zero[i][1])

    # Step 2-2-1
    non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))

    marked_cols = []
    check_switch = True
    while check_switch:
        check_switch = False
        for i in range(len(non_marked_row)):
            row_array = zero_bool_mat[non_marked_row[i], :]
            for j in range(row_array.shape[0]):
                # Step 2-2-2
                if row_array[j] == True and j not in marked_cols:
                    # Step 2-2-3
                    marked_cols.append(j)
                    check_switch = True

        for row_num, col_num in marked_zero:
            # Step 2-2-4
            if row_num not in non_marked_row and col_num in marked_cols:
                # Step 2-2-5
                non_marked_row.append(row_num)
                check_switch = True
    # Step 2-2-6
    marked_rows = list(set(range(mat.shape[0])) - set(non_marked_row))

    return (marked_zero, marked_rows, marked_cols)


def adjust_matrix(mat, cover_rows, cover_cols):
    cur_mat = mat
    non_zero_element = []

    # Step 4-1
    for row in range(len(cur_mat)):
        if row not in cover_rows:
            for i in range(len(cur_mat[row])):
                if i not in cover_cols:
                    non_zero_element.append(cur_mat[row][i])
    min_num = min(non_zero_element)

    # Step 4-2
    for row in range(len(cur_mat)):
        if row not in cover_rows:
            for i in range(len(cur_mat[row])):
                if i not in cover_cols:
                    cur_mat[row, i] = cur_mat[row, i] - min_num
    # Step 4-3
    for row in range(len(cover_rows)):
        for col in range(len(cover_cols)):
            cur_mat[cover_rows[row], cover_cols[col]] = cur_mat[cover_rows[row], cover_cols[col]] + min_num
    return cur_mat


def hungarian_algorithm_supp(profit_matrix):
    max_value = np.max(profit_matrix)
    mat = max_value - profit_matrix

    dim = mat.shape[0]
    cur_mat = mat

    # Step 1 - Every column and every row subtract its internal minimum
    for row_num in range(mat.shape[0]):
        cur_mat[row_num] = cur_mat[row_num] - np.min(cur_mat[row_num])

    for col_num in range(mat.shape[1]):
        cur_mat[:, col_num] = cur_mat[:, col_num] - np.min(cur_mat[:, col_num])
    zero_count = 0
    while zero_count < dim:
        # Step 2 & 3
        ans_pos, marked_rows, marked_cols = mark_matrix(cur_mat)
        zero_count = len(marked_rows) + len(marked_cols)

        if zero_count < dim:
            cur_mat = adjust_matrix(cur_mat, marked_rows, marked_cols)

    return ans_pos


def assignment_hungarian_algorithm(mat):
    start_time = time.time()
    pos = hungarian_algorithm_supp(mat)
    total = 0
    ans_mat = np.zeros((mat.shape[0], mat.shape[1]))
    for i in range(len(pos)):
        total += mat[pos[i][0], pos[i][1]]
        ans_mat[pos[i][0], pos[i][1]] = 1 if mat[pos[i][0], pos[i][1]] != 0 else 0
    end_time = time.time()
    exec_time = end_time - start_time
    return int(total), ans_mat.tolist(), exec_time, "O(n^3)"


def assignment_brute_force(cost_matrix):
    start_time = time.time()
    n = len(cost_matrix)
    all_assignments = np.array(list(itertools.permutations(range(n))))

    best_assignment = None
    best_result = float('-inf')

    for assignment in all_assignments:
        result = 0
        for i, j in enumerate(assignment):
            result += cost_matrix[i, j]

        if result > best_result:
            best_result = result
            best_assignment = assignment

    assignment_matrix = np.zeros((n, n))
    for i, j in enumerate(best_assignment):
        assignment_matrix[i, j] = 1

    end_time = time.time()
    exec_time = end_time - start_time

    return int(best_result), assignment_matrix.tolist(), exec_time, "O(n!)"