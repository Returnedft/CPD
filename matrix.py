import time

def OnMult(m_ar : int, m_br : int) -> None:
    temp = 0

    pha = []
    phb = []
    phc = []

    for i in range(0, m_ar):
        for j in range(0, m_ar):
            pha.append(1.0)
    
    for i in range(0, m_br):
        for j in range(0, m_br):
            phb.append(i + 1)
    
    for i in range(0, m_ar):
        for j in range(0, m_ar):
            phc.append(0)
    
    time1 = time.time()

    for i in range(0, m_ar):
        for j in range(0, m_br):
            temp = 0
            for k in range(0, m_ar):
                temp += pha[i*m_ar + k] * phb[k*m_br + j]
            phc[i*m_ar + j] = temp
    
    time2 = time.time()

    final = time2 - time1

    print(f'Final Time is {final}')

    for i in range(0, min(10,m_br)):
        print(phc[i])
    

OnMult(1000, 1000)