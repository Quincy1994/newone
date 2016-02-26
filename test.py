#coding=utf-8
import jieba

q = jieba.cut('good')
li =list(q)
print li
print li.count('good')
print li +[1,2,2]
print list(set(li +[1,2,2])).index('good')
