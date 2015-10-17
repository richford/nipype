# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..svm import SVMTest

def test_SVMTest_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    classout=dict(argstr='-classout',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-testvol %s',
    mandatory=True,
    ),
    model=dict(argstr='-model %s',
    mandatory=True,
    ),
    multiclass=dict(argstr='-multiclass %s',
    ),
    nodetrend=dict(argstr='-nodetrend',
    ),
    nopredcensord=dict(argstr='-nopredcensord',
    ),
    options=dict(argstr='%s',
    ),
    out_file=dict(argstr='-predictions %s',
    name_template='%s_predictions',
    ),
    outputtype=dict(),
    terminal_output=dict(nohash=True,
    ),
    testlabels=dict(argstr='-testlabels %s',
    ),
    )
    inputs = SVMTest.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_SVMTest_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = SVMTest.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
