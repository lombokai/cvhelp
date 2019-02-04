def tocenter(bbox, pad={'r':100, 'l':50, 't':50, 'b':100}, ratio=1):
    x,y,w,h=bbox
    ratio_real = h/w
    if w>h:
        hn = int(w * ratio)
        wn = w
    else:
        hn = h
        wn = int(h * ratio)
    
    yn=(y + (h//2)) - (hn//2)
    xn=(x + (w//2)) - (wn//2)
    xn = xn - pad['l']
    yn = yn - pad['t']
    hn = hn + pad['b']
    wn = wn + pad['r']
    
    return (xn, yn, wn, hn)
