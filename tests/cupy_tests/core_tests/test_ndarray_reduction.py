import unittest

import cupy
from cupy import testing


@testing.gpu
class TestArrayReduction(unittest.TestCase):

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_all(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.max()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_all_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.max(keepdims=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_axis_large(self, xp, dtype):
        a = testing.shaped_random((3, 1000), xp, dtype)
        return a.max(axis=0)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_axis0(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.max(axis=0)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_axis1(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.max(axis=1)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_axis2(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.max(axis=2)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_multiple_axes(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.max(axis=(1, 2))

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_multiple_axes_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.max(axis=(1, 2), keepdims=True)

    @testing.for_float_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_nan(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.max()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_nan_real(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.max()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_max_nan_imag(self, xp, dtype):
        a = xp.array([float('nan')*1.j, 1.j, -1.j], dtype)
        return a.max()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_all(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.min()

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_all_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.min(keepdims=True)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_axis_large(self, xp, dtype):
        a = testing.shaped_random((3, 1000), xp, dtype)
        return a.min(axis=0)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_axis0(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.min(axis=0)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_axis1(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.min(axis=1)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_axis2(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.min(axis=2)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_multiple_axes(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.min(axis=(1, 2))

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_multiple_axes_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.min(axis=(1, 2), keepdims=True)

    @testing.for_float_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_nan(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.min()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_nan_real(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.min()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_min_nan_imag(self, xp, dtype):
        a = xp.array([float('nan')*1.j, 1.j, -1.j], dtype)
        return a.min()

    # skip bool: numpy's ptp raises a TypeError on bool inputs
    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_all(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.ptp()

    @testing.with_requires('numpy>=1.15')
    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_all_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3), xp, dtype)
        return a.ptp(keepdims=True)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_axis_large(self, xp, dtype):
        a = testing.shaped_random((3, 1000), xp, dtype)
        return a.ptp(axis=0)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_axis0(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.ptp(axis=0)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_axis1(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.ptp(axis=1)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_axis2(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.ptp(axis=2)

    @testing.with_requires('numpy>=1.15')
    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_multiple_axes(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.ptp(axis=(1, 2))

    @testing.with_requires('numpy>=1.15')
    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose()
    def test_ptp_multiple_axes_keepdims(self, xp, dtype):
        a = testing.shaped_random((2, 3, 4), xp, dtype)
        return a.ptp(axis=(1, 2), keepdims=True)

    @testing.for_float_dtypes()
    @testing.numpy_cupy_allclose()
    def test_ptp_nan(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.ptp()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_ptp_nan_real(self, xp, dtype):
        a = xp.array([float('nan'), 1, -1], dtype)
        return a.ptp()

    @testing.for_complex_dtypes()
    @testing.numpy_cupy_allclose()
    def test_ptp_nan_imag(self, xp, dtype):
        a = xp.array([float('nan')*1.j, 1.j, -1.j], dtype)
        return a.ptp()


# This class compares CUB results against NumPy's
@testing.parameterize(*testing.product({
    'shape': [(10,), (10, 20), (10, 20, 30), (10, 20, 30, 40)],
    'order': ('C', 'F'),
}))
@testing.gpu
@unittest.skipUnless(cupy.cuda.cub_enabled, 'The CUB routine is not enabled')
class TestCubReduction(unittest.TestCase):

    def setUp(self):
        self.old_backends = cupy.core._backend.get_reduction_backends()
        cupy.core._backend.set_reduction_backends(['cub'])

    def tearDown(self):
        cupy.core._backend.set_reduction_backends(self.old_backends)

    @testing.for_contiguous_axes()
    @testing.for_all_dtypes(no_bool=True, no_float16=True)
    @testing.numpy_cupy_allclose(rtol=1E-5)
    def test_cub_min(self, xp, dtype, axis):
        a = testing.shaped_random(self.shape, xp, dtype)
        if self.order in ('c', 'C'):
            a = xp.ascontiguousarray(a)
        elif self.order in ('f', 'F'):
            a = xp.asfortranarray(a)
        return a.min(axis=axis)

    @testing.for_contiguous_axes()
    @testing.for_all_dtypes(no_bool=True, no_float16=True)
    @testing.numpy_cupy_allclose(rtol=1E-5)
    def test_cub_max(self, xp, dtype, axis):
        a = testing.shaped_random(self.shape, xp, dtype)
        if self.order in ('c', 'C'):
            a = xp.ascontiguousarray(a)
        elif self.order in ('f', 'F'):
            a = xp.asfortranarray(a)
        return a.max(axis=axis)
