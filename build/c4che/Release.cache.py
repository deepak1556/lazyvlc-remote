AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
CCFLAGS = ['-g']
CCFLAGS_MACBUNDLE = ['-fPIC']
CCFLAGS_NODE = ['-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64']
CC_VERSION = ('4', '6', '3')
COMPILER_CXX = 'g++'
CPP = '/usr/bin/cpp'
CPPFLAGS_NODE = ['-D_GNU_SOURCE']
CPPPATH_NODE = '/usr/local/include/node'
CPPPATH_ST = '-I%s'
CXX = ['/usr/lib64/ccache/g++']
CXXDEFINES_ST = '-D%s'
CXXFLAGS = ['-g']
CXXFLAGS_DEBUG = ['-g']
CXXFLAGS_NODE = ['-D_LARGEFILE_SOURCE', '-D_FILE_OFFSET_BITS=64']
CXXFLAGS_RELEASE = ['-O2']
CXXLNK_SRC_F = ''
CXXLNK_TGT_F = ['-o', '']
CXX_NAME = 'gcc'
CXX_SRC_F = ''
CXX_TGT_F = ['-c', '-o', '']
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
FULLSTATIC_MARKER = '-static'
HAVE_LUA = 1
LIBDIR = '/home/robo/.node_libraries'
LIBPATH_NODE = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_LUA = ['lua', 'm', 'dl']
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINK_CXX = ['/usr/lib64/ccache/g++']
NODE_PATH = '/home/robo/.node_libraries'
PREFIX = '/usr/local'
PREFIX_NODE = '/usr/local'
RANLIB = '/usr/bin/ranlib'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STATICLIBPATH_ST = '-L%s'
STATICLIB_MARKER = '-Wl,-Bstatic'
STATICLIB_ST = '-l%s'
defines = {'HAVE_LUA': 1}
macbundle_PATTERN = '%s.bundle'
program_PATTERN = '%s'
shlib_CXXFLAGS = ['-fPIC', '-DPIC']
shlib_LINKFLAGS = ['-shared']
shlib_PATTERN = 'lib%s.so'
staticlib_LINKFLAGS = ['-Wl,-Bstatic']
staticlib_PATTERN = 'lib%s.a'