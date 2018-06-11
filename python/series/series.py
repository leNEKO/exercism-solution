def slices(series: str, length: int) -> list:
    ''' Ceci est un test '''

    mx = len(series)
    if 0 < length <= mx:
        sub = []
        sl = (mx+1) - length
        for k in range(0, sl):
            sub.append(series[k:k+length])
        return sub
    else:
        raise ValueError("Nope")
