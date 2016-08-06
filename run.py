from markov_python.cc_markov import MarkovChain
mc = MarkovChain()

mc.add_file('lyrics.txt')

print mc.generate_text()