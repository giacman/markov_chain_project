# Markov Chain Jarvis Cocker project

The goal of this application is to use Markov Chains to generate new songs with lyrics in the style of Pulp singer Jarvis Cocker.

Description of the project:

1. Fetch original Jarvis Cocker lyrics using [musixmatch](musixmatch.com) API (free limited access) 
2. Generate and display *pseudo* Jarvis Cocker lyrics using a simple Markov chain model.

Set up:

- install virtualenv
- run `pip install -r requirements.txt`
- run `python prepare_data.py` and wait until the lyrics are dowloaded

Run `python generate_lyrics.py` and check out the results!

For information on Markov chain models look [here](https://en.wikipedia.org/wiki/Markov_chain):

For information on Jarvis Cocker look [here](https://en.wikipedia.org/wiki/Jarvis_Cocker), or for more info about
The Pulp look [here](https://en.wikipedia.org/wiki/Pulp_(band)):

Note: This my final Project for the [codeacademy Pro Python course](https://www.codecademy.com/final_project/python):
