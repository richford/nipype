# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..dti import DTITracker

def test_DTITracker_inputs():
    input_map = dict(angle_threshold=dict(argstr='-at %f',
    ),
    angle_threshold_weight=dict(argstr='-atw %f',
    ),
    args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    input_data_prefix=dict(argstr='%s',
    position=0,
    usedefault=True,
    ),
    input_type=dict(argstr='-it %s',
    ),
    invert_x=dict(argstr='-ix',
    ),
    invert_y=dict(argstr='-iy',
    ),
    invert_z=dict(argstr='-iz',
    ),
    mask1_file=dict(argstr='-m %s',
    mandatory=True,
    position=2,
    ),
    mask1_threshold=dict(position=3,
    ),
    mask2_file=dict(argstr='-m2 %s',
    position=4,
    ),
    mask2_threshold=dict(position=5,
    ),
    output_file=dict(argstr='%s',
    position=1,
    usedefault=True,
    ),
    output_mask=dict(argstr='-om %s',
    ),
    primary_vector=dict(argstr='-%s',
    ),
    random_seed=dict(argstr='-rseed',
    ),
    step_length=dict(argstr='-l %f',
    ),
    swap_xy=dict(argstr='-sxy',
    ),
    swap_yz=dict(argstr='-syz',
    ),
    swap_zx=dict(argstr='-szx',
    ),
    tensor_file=dict(),
    terminal_output=dict(nohash=True,
    ),
    tracking_method=dict(argstr='-%s',
    ),
    )
    inputs = DTITracker.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DTITracker_outputs():
    output_map = dict(mask_file=dict(),
    track_file=dict(),
    )
    outputs = DTITracker.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
