def EditDistance(x,y):
addDistance    = editDistance(x, y[:-1]) + 1
removeDistance = editDistance(x[:-1], y) + 1
changeDistance = editDistance(
                              x[:-1],
                              y[:-1],
                              )
      return min(min(addDistance, removeDistance), changeDistance)

x = 