#read memory location at &v for v.size()

cdef class MyClass:
    cdef _MyClass *thisptr;

    def __cinit__(self):
        self.thisptr = new _MyClass()

    def __dealloc__(self):
        del self.thisptr

    def get_matrix(self):
        return ndarray(self.thisptr.get_matrix())
