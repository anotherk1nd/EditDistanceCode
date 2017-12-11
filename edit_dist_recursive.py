def EditDist_rec(x, m, y, n):
    if m == 0: return n
    if n == 0: return m
    if x[m-1] == y[n-1]:
        return EditDist_rec(x, m-1, y, n-1)
    else:
        return 1 + min(EditDist_rec(x, m-1, y, n-1),
                       EditDist_rec(x, m, y, n-1),
                       EditDist_rec(x, m-1, y, n))

def EditDist_recp(x, m, y, n, x_out, op, y_out):
    if m == 0:
        for i in range(0, n): #insert rest
            x_out.append("_")
            y_out.append(y[i-1])
            op.append(" ")
        return n
    if n == 0:
        for i in range(0, m): #delete rest
            x_out.append(x[i-1])
            y_out.append("_")
            op.append(" ")
        return m
    if x[m-1] == y[n-1]: #identical
        x_out.append(x[m-1])
        y_out.append(y[n-1])
        op.append("|")
        return EditDist_recp(x, m-1, y, n-1, x_out, op, y_out)
    else:
        dist_sub = EditDist_rec(x, m-1, y, n-1)
        dist_ins = EditDist_rec(x, m, y, n-1)
        dist_del = EditDist_rec(x, m-1, y, n)
        if dist_sub <= min(dist_ins, dist_del):
            x_out.append(x[m-1])
            y_out.append(y[n-1])
            op.append(" ")
            return 1 + min(dist_del, dist_ins,
                           EditDist_recp(x, m-1, y, n-1, x_out, op, y_out))

        if dist_ins <= min(dist_sub, dist_del):
            x_out.append("_")
            y_out.append(y[n-1])
            op.append(" ")
            return 1 + min(dist_sub, dist_del,
                           EditDist_recp(x, m, y, n-1, x_out, op, y_out))

        if dist_del <= min(dist_ins, dist_sub):
            x_out.append(x[m-1])
            y_out.append("_")
            op.append(" ")
            return 1 + min(dist_sub, dist_ins,
                           EditDist_recp(x, m-1, y, n, x_out, op, y_out))

print("EditDist_rec =", EditDist_rec("sunshine", 8, "sunrise", 7))

x_out = []
y_out = []
op    = []
print("EditDist_rec =", EditDist_recp("sunshine", 8, "sunrise", 7, x_out, op,
      y_out))
print("X=", x_out[::-1])
print("  ", op[::-1])
print("Y=", y_out[::-1])
