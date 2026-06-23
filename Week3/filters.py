
def volume_sma(volumes,window):
    sma = [None] * len(volumes)
    for i in range(window-1, len(volumes)):
        sma[i] = sum(volumes[i-window+1:i+1])/window
    return sma
def volume_filter(volumes):
    volume_avg = volume_sma(volumes,20)
    c = 1.5
    volume_ok = []
    for i in range(len(volume_avg)):
        vol = volume_avg[i] is not None and (volumes[i] > 1.5*volume_avg[i])
        volume_ok.append(vol)
    return volume_ok
