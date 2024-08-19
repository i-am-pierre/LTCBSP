y_child = int(input())
m_child = int(input())

def cal_old_age (y, m):
    o_child = m + ( m - y )
    return o_child

print(f"{cal_old_age(y_child, m_child)}")
