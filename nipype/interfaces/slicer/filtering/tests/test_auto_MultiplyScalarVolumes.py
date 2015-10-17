# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..arithmetic import MultiplyScalarVolumes

def test_MultiplyScalarVolumes_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume1=dict(argstr='%s',
    position=-3,
    ),
    inputVolume2=dict(argstr='%s',
    position=-2,
    ),
    order=dict(argstr='--order %s',
    ),
    outputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = MultiplyScalarVolumes.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MultiplyScalarVolumes_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = MultiplyScalarVolumes.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
