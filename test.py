import pickle as pk

d = pk.dumps('knn_05.pkl')
print(type(d))
l = pk.loads(d)
print(type(l))
print(l)