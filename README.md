Lempel ziv test

This python project is to implement Lempel-Ziv compression algorithm as per this video:
https://www.youtube.com/watch?v=RV5aUr8sZD0

This branch (pipes_bufferend) uses pipes to implement the compression of text from any source.

from linux terminal use
cat test.txt | ./compress.py > comp.txt

cat comp.txt | ./decompress.py > test2.txt
