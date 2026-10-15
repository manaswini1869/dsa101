# In the Kingdom of Lanqiao, two magical envoys, Xiaolan and Xiaoqiao, 
# are responsible for maintaining order across space and time. 
# Each holds N rune stones, with each stone bearing an integer between 1 and 10^9. 
# Xiaolan’s stones are labeled s1, s2, …, sN, and Xiaoqiao’s stones are 
# labeled t1, t2, …, tN.
# The two envoys travel between nodes in space and time by using their rune stones. 
# Each journey follows this rule: after Xiaolan uses stone si, Xiaoqiao must use a stone tj 
# with a strictly larger index, meaning j > i. Similarly, 
# after Xiaoqiao uses stone ti, Xiaolan must use a stone sj with j > i.
# For a journey to succeed, the numbers on two consecutively used stones must share at 
# least one digit from the set {0, 2, 4}. These digits represent Starfire (0), Waterwave (2), and Windwhisper (4).
# For example, 126, 552, 24, 4 is a valid sequence: 
# every pair of adjacent numbers shares at least one digit from {0, 2, 4}. 
# However, 15, 51, 5 is invalid because adjacent numbers do not share any of these digits.

# Xiaolan always goes first, using one of his stones to begin the journey.
# Your task is to determine the maximum possible length of a valid journey sequence. Such a sequence has the form

# $$ s_{i_1},\ t_{i_2},\ s_{i_3},\ t_{i_4},\ \ldots, $$

# where
# $$ i_1 < i_2 < i_3 < i_4 < \cdots, $$
# and every pair of adjacent numbers shares at least one digit from {0, 2, 4}.

def solve(N, s, t) -> int:
  