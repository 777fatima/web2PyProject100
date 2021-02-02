from mako.compat import pypy

from pyspark import SparkConf, SparkContext
# PYSPARK_PYTHON=python3.4 bin/pyspark
PYSPARK_PYTHON=/opt/pypy-2.5/bin/pypy bin/spark-submit examples/src/main/python/pi.py
sc = SparkContext(master="local", appName="Spark Demo")
# print(sc.textFile("C:\\deckofcards.txt").first())


# print(sc.textFile("C:\\deckofcards.txt").first())
sc = SparkContext(conf=conf)