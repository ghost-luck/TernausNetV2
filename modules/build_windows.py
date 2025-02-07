import os
import torch

from torch.utils.ffi import create_extension

sources = ['src/lib_cffi.cpp']
headers = ['src/lib_cffi.h']
extra_objects = ['src/bn.cu.obj'] #['src/bn.o']
with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

ffi = create_extension(
    '_ext',
    headers=headers,
    sources=sources,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects,
    extra_compile_args=['/std:c++latest'], #["-std=c++11"]
	extra_link_args=['cudart.lib','caffe2.lib','caffe2_gpu.lib']
)

if __name__ == '__main__':
    ffi.build()
