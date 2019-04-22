import numpy as np
import coremltools

for filename in ['ELFOpenGo_v2.mlmodel', 'ELFOpenGo_v2_fp16.mlmodel']:
    print("predict {}".format(filename))
    model =  coremltools.models.MLModel(filename)
    x = np.zeros((18,19,19))
    x[16,:,:] = 1.0
    print(model.predict({'x__0': x})[u'fc3__0'])

