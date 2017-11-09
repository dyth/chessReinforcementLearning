#include <iostream>
#include <Python.h>

// Call Python to compute 2+2
// Based on https://www.coveros.com/calling-python-code-from-c/
int main(int argc, char *argv[])
{
	// Initialize Python interpreter and pass any state variables
    Py_Initialize();
	PySys_SetArgv(argc, argv);
	
	PyObject *pyName, *pyModule, *pyDict, *py_add, *pyArgs, *pya;
	
    // import file in python session using python string, get dict of functions 
    pyName = PyString_FromString("Sample");
    pyModule = PyImport_Import(pyName);
    pyDict = PyModule_GetDict(pyModule);
	
    // Create Python argument tuple of python elements 
    pyArgs = PyTuple_New(2);
    pya = PyInt_FromLong(2);
    PyTuple_SetItem(pyArgs, 0, pya);
    PyTuple_SetItem(pyArgs, 1, pya);

	// Call python function, convert result from python object, end
	py_add = PyDict_GetItemString(pyDict, "add");
    PyObject* pyResult = PyObject_CallObject(py_add, pyArgs);
    long result = PyInt_AsLong(pyResult);
    Py_Finalize();
	
    // Print result.
    cout << "The result is %ld\n" << result;
}
