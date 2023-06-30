import bpy

from placement.factory import AssetFactory


class BaseMolluskFactory(AssetFactory):
    max_expected_radius = .5
    noise_strength = .02
    ratio = 1
    x_scale = 2
    z_scale = 1
    distortion = 1

    def __init__(self, factory_seed, coarse=False):
        super(BaseMolluskFactory, self).__init__(factory_seed, coarse)

    def create_asset(self, **params) -> bpy.types.Object:
        raise NotImplemented
