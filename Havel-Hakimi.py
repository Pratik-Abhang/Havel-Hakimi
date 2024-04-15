#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
import matplotlib.pyplot as plt

def HHA(deg_seq):
    if not deg_seq:
        print("Sequence is empty")
        return False
    deg_seq = sorted(deg_seq, reverse=True)
    s = sum(deg_seq)
    if s % 2 != 0:
        print("Given sequence is not graphical")
        return False
    while True:        
        if deg_seq[0] < 0 or deg_seq[0] >= len(deg_seq):
            print("Given sequence is not graphical")
            return False
        if all(d == 0 for d in deg_seq):
            print("Given sequence is graphical")
            #print(deg_seq)
            return True
        for i in range(1, deg_seq[0] + 1):
            deg_seq[i] -= 1
        deg_seq.pop(0)
        deg_seq = sorted(deg_seq, reverse=True)

def plot_graph(deg_seq):
    if HHA(deg_seq):
        G = nx.random_degree_sequence_graph(deg_seq)
        nx.draw(G, with_labels=True, node_color='purple', node_size=500, font_size=10)
        plt.show()

# Example usage
seq = [2,2,2,2,2]
plot_graph(seq)


# In[ ]:





#  
