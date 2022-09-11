Lempel ziv

This python project is to implement Lempel-Ziv compression algorithm as described in this video:
https://www.youtube.com/watch?v=RV5aUr8sZD0

The encoder algorithm works by iterating along a string of text and building a dictionary of previously unencountered words on the fly. 
If a previously encountered word appears in the input string, its value is looked up in the dictionary and a code is sent instead of the previously encountered word. 

The decompression process is the reverse of the compression process.

In this way, a text string with many repeating sequences would be effectively compressed and decompressed without the need to transmit the dictionary.

It doesn't work so well on noise or numerical data, unless long sequences of numbers repeat frequently.

This project is a collaboration - the encoder was written by Mike and the decoder was written by Anthony and modified by Mike to enable non-keyboard characters for signaling a new dictionary entry.

