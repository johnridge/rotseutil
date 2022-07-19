def saveLightCurve(lightCurve, title):
    import numpy as np
    fileName = f'{title}.dat'
    print(f"You can find a copy of the light curve named {fileName} in the current working directory")
    np.savetxt(fileName, lightCurve, fmt = '%.11f')
    