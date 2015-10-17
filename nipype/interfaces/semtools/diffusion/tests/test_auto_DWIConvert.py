# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..diffusion import DWIConvert

def test_DWIConvert_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    conversionMode=dict(argstr='--conversionMode %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fMRI=dict(argstr='--fMRI ',
    ),
    fslNIFTIFile=dict(argstr='--fslNIFTIFile %s',
    ),
    gradientVectorFile=dict(argstr='--gradientVectorFile %s',
    hash_files=False,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputBValues=dict(argstr='--inputBValues %s',
    ),
    inputBVectors=dict(argstr='--inputBVectors %s',
    ),
    inputDicomDirectory=dict(argstr='--inputDicomDirectory %s',
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    outputBValues=dict(argstr='--outputBValues %s',
    hash_files=False,
    ),
    outputBVectors=dict(argstr='--outputBVectors %s',
    hash_files=False,
    ),
    outputDirectory=dict(argstr='--outputDirectory %s',
    hash_files=False,
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    smallGradientThreshold=dict(argstr='--smallGradientThreshold %f',
    ),
    terminal_output=dict(nohash=True,
    ),
    useBMatrixGradientDirections=dict(argstr='--useBMatrixGradientDirections ',
    ),
    useIdentityMeaseurementFrame=dict(argstr='--useIdentityMeaseurementFrame ',
    ),
    writeProtocolGradientsFile=dict(argstr='--writeProtocolGradientsFile ',
    ),
    )
    inputs = DWIConvert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DWIConvert_outputs():
    output_map = dict(gradientVectorFile=dict(),
    outputBValues=dict(),
    outputBVectors=dict(),
    outputDirectory=dict(),
    outputVolume=dict(),
    )
    outputs = DWIConvert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
