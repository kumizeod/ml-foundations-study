"""Geometry and convolution shape checks; no camera calibration is implied."""
import math


def conv_output_size(size, kernel, stride=1, padding=0, dilation=1):
    if any(type(x) is not int for x in (size, kernel, stride, padding, dilation)):
        raise ValueError('shape arguments must be integers')
    if min(size, kernel, stride, dilation) <= 0 or padding < 0:
        raise ValueError('invalid convolution geometry')
    effective = dilation * (kernel-1) + 1
    if size + 2*padding < effective:
        raise ValueError('no valid output position')
    return (size + 2*padding - effective) // stride + 1


def receptive_field(layers):
    """Sequence of (kernel, stride, dilation), one spatial dimension."""
    field, jump = 1, 1
    for k, s, d in layers:
        if any(type(x) is not int or x <= 0 for x in (k, s, d)):
            raise ValueError('positive integer layer geometry required')
        field += (k-1)*d*jump
        jump *= s
    return {'field': field, 'jump': jump}


def unproject(u, v, depth, fx, fy, cx, cy):
    if any(not math.isfinite(x) for x in (u, v, depth, fx, fy, cx, cy)) or min(depth, fx, fy) <= 0:
        raise ValueError('finite coordinates, positive depth/focal length required')
    return [(u-cx)*depth/fx, (v-cy)*depth/fy, depth]


def transform(point, rotation, translation, inverse=False):
    if len(point) != 3 or len(translation) != 3 or len(rotation) != 3 or any(len(row) != 3 for row in rotation):
        raise ValueError('3D point, 3x3 rotation and 3D translation required')
    if any(not math.isfinite(x) for row in [point, translation, *rotation] for x in row):
        raise ValueError('nonfinite rigid transform')
    r = rotation
    if any(abs(sum(r[k][i]*r[k][j] for k in range(3))-int(i == j)) > 1e-6
           for i in range(3) for j in range(3)):
        raise ValueError('rotation must be orthogonal')
    det = (r[0][0]*(r[1][1]*r[2][2]-r[1][2]*r[2][1])
           -r[0][1]*(r[1][0]*r[2][2]-r[1][2]*r[2][0])
           +r[0][2]*(r[1][0]*r[2][1]-r[1][1]*r[2][0]))
    if abs(det-1) > 1e-6:
        raise ValueError('proper rotation requires determinant +1')
    if inverse:
        shifted = [point[i]-translation[i] for i in range(3)]
        return [sum(r[j][i]*shifted[j] for j in range(3)) for i in range(3)]
    return [sum(r[i][j]*point[j] for j in range(3))+translation[i] for i in range(3)]
