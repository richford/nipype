# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..misc import CalculateNormalizedMoments

def test_CalculateNormalizedMoments_inputs():
    input_map = dict(moment=dict(mandatory=True,
    ),
    timeseries_file=dict(mandatory=True,
    ),
    )
    inputs = CalculateNormalizedMoments.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_CalculateNormalizedMoments_outputs():
    output_map = dict(moments=dict(),
    )
    outputs = CalculateNormalizedMoments.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
