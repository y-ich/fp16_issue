import sys
import coremltools

if __name__ == '__main__':
    # Load a model, lower its precision, and then save the smaller model.
    model_spec = coremltools.utils.load_spec("ELFOpenGo_v2.mlmodel")
    model_fp16_spec = coremltools.utils.convert_neural_network_spec_weights_to_fp16(model_spec)
    coremltools.utils.save_spec(model_fp16_spec, "ELFOpenGo_v2_fp16.mlmodel")
