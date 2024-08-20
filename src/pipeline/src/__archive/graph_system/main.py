"""
BRAIN STORM

In this folder system we want to start to figure out the different interactions we have in our graph
from ending action to action, none action to action and vice versa, also important to figure out what type of videos
we want to automate. For example, of we want summaries we can focus on giving more weight to equal timming between clips,
or if we want to give clip that flow nicely together clips that have similar area of focus compared to other

Steps:
First first out how to implement a graph structure that supports time and action

Second figure out more creative ways to get data from video processing and a way to effect the weighing of these factors

Third we need to refactor a lot of the code to work better


#Aspects

Depending on the type of video content we should also use a different type of graph structure ie for storys where the timeline is important
such as a valorant match we may want to use a directed graph where we join edges heavy on the time while if we want pure content
we may use a undirected graph as it do not matter where we start but rather how strong the edges are related to each other


Type of graphs that seem to be a good, directed,  undirected, ego,

Attri.

Centrality of graph is important.

degree_centrality... how important said node based on the placement
eurlian path - might be better if we have the video filtered
find_clique - finds clusters/best subgraph


#if each clip is a node, connect the edges based on the weight/point system


RULES - basic assumptions we should make to make our graph logic based off of

STORY MODE------------------------- Probably better just to stick to a list data structure instead of a graph since we want something linear
We want clips to be ordered by time

TIMELESS MODE ---------------------
We want to use graphs (undirected)
Not all clip should make it to the end -> centrality best case?

Attributes for edges to connect  -
On_Unique Color -> how interesting a clip is, -> when not in dom color and not a shade, -> we should give points/ratio based on clip size
On_Target Color -> given a target color we can tell specific information based on game, -> mask and threshold target color range + percentage_of_white_pixels
Change_Dom_ Color -> change in environment/scene change up, save dom_colors then average change between clips -> greater change good for contrasting videos
ACTIVITY_AMOUNT threshold -> at a certain threshold, we can spot skills in valorant. Use threshold + percentage_of_white_pixels

"""


import networkx as nx

G = nx.Graph()

def load_clip_nodes(edges_list : list):
  pass






