import streamlit as st 
st.title("Havel Hakimi Algorithm App")
st.text("This app will help you to check whether the degree sequence is graphical or not")
st.text("if yes it will show you the graph of it")
user_input = st.text_input("enter degree sequence seperated by comma")
user_str = user_input.replace(',', '')
user_str = user_str.split()
seq = []
for i in user_str:
    seq.append(user_str)

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

if st.button("Apply"):
  plot_graph(seq)



