import math
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import json
import random




pn_array = []
pn_array.append(1) # p(0) = 1  


def jp(m):
    return int((m*(3*m+1))/2)
def jm(m):
    return int((m*(3*m-1))/2)



def Get_recursive_n_vals(n):
    sign_list  = []
    n_recursive_vals = []

    j = 0
    m_bool = True
    p_bool = True
    while True:
        #print("START", j)
        s = (-1)**(j+1)
        j_m = jm(j)
        j_p = jp(j)
        #print(j_m, j_p)
        n_m =  n - j_m
        if n_m >= 0:
            sign_list.append(s)
            n_recursive_vals.append(n_m)
        else:
            m_bool = False
        n_p = n - j_p
        if n_p >= 0:
            sign_list.append(s)
            n_recursive_vals.append(n_p)
        else:
            p_bool = False


        if m_bool == False and p_bool == False:
            break
        j+=1 

    sign_list = sign_list[::-1]
    n_recursive_vals = n_recursive_vals[::-1]
    sign_list = sign_list[:-2]
    n_recursive_vals = n_recursive_vals[:-2]

    return n_recursive_vals, sign_list


def p(n):
    for i in range(1, n+1):
        p_i = 0
        n_recursive_vals, sign_list = Get_recursive_n_vals(i)
       
        for c in range(0, len(n_recursive_vals)):
            p_i += sign_list[c] *  pn_array[n_recursive_vals[c]] 
        pn_array.append(p_i)
    return pn_array, pn_array[n]

def changeFunc(arr,  p):
    if p == 2:
        return 1.0
    n = len(arr)
    arr_norm = arr
    arr_norm.remove(max(arr))
    arr_norm.remove(min(arr))
    mean = sum(arr_norm)/(n-2)
    if mean == 0:
        return 1
    diff = [abs(v - mean) for v in arr]
    print(arr)
    print(mean)
    print("DIFF", diff)
    avg_diff = sum(diff)/n
    if avg_diff == 0:
        return 1
    print("------------------------------",p,max(diff)/avg_diff , avg_diff, max(diff))
    return max(diff)/avg_diff


N = 10000
arr, v = p(N)

random_elements = random.sample(arr, 1000)
#print(arr)

x_l = [x for x in range(N+1)]

# plt.bar(x_l, arr)
# plt.xlabel("n")
# plt.ylabel("p(n)")
# plt.title("p(n)")
# plt.show()

#primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

#primes_list = primes_list[:10]


with open("primes.json") as f:
    data = json.load(f)

primes_list = data['p_array']

primes_list = primes_list[:10]

spike_l = []

#for C in range(2, 18):
count = 1
for C in primes_list:
    v_C = [x for x in range(0, C)]

    arr_mod = [x % C for x in arr]

    #print("AAAAAAAAAAA", arr_mod)
    congr_class = []
    for i in range(0, C):
        congr_class.append(arr_mod.count(i))

    print("BBBBBBBBBBBBBBB", C, congr_class)
    plt.subplot(5, 2, count)
    plt.bar(v_C, congr_class)
    plt.xticks(v_C)
    plt.title("Congruence classes mod " + str(C))

    count += 1


    # spike = changeFunc(congr_class, C)
    # spike_l.append(spike)

    
# plt.title("Max deviation of congruence classes")
# primes_index_l = [x for x in range(0, len(primes_list))]
# plt.bar(primes_index_l, spike_l)
# plt.xlabel("primes")
# plt.ylabel("max deviation from mean")






plt.show()
