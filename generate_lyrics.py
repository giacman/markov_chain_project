from markov_python.cc_markov import MarkovChain


if __name__ == '__main__':

    mc = MarkovChain()

    mc.add_file('lyrics.txt')

    lyric = mc.generate_text()
    lyric = ' '.join(lyric)

    lyric = ''.join([i for i in lyric if not i.isdigit()])
    print '---------------------------'
    print '---------------------------'
    print lyric
    print '---------------------------'
    print '---------------------------'