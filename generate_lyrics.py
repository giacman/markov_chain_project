from markov_python.cc_markov import MarkovChain


if __name__ == '__main__':

    mc = MarkovChain()
    mc.add_file('lyrics.txt')
    print mc.generate_text()