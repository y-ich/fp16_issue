import coremltools

# Load the model
model =  coremltools.models.MLModel('ELFOpenGo_v2.mlmodel')

# Visualize the model
model.visualize_spec()