#include <iostream>
#include <Python.h>

// Call Python to compute 2+2
// Based on https://www.coveros.com/calling-python-code-from-c/
int main(int argc, char *argv[])
{
	// Initialize Python interpreter and Python placeholder objects
    Py_Initialize();
    PyObject *pName, *pModule, *pDict, *pFunc, *pArgs, *pValue;
	
    // Filename -> Python string, then import file as a module
	PySys_SetArgv(argc, argv);
    pName = PyString_FromString("Sample");
    pModule = PyImport_Import(pName);
	
    // Create a dictionary of module contents and get add method
    pDict = PyModule_GetDict(pModule);
    pFunc = PyDict_GetItemString(pDict, "add");
	
    // Create a Python argument tuple, set argument values to python methods
    pArgs = PyTuple_New(2);
    pValue = PyInt_FromLong(2);
    PyTuple_SetItem(pArgs, 0, pValue);
    PyTuple_SetItem(pArgs, 1, pValue);

	// Call the function with the arguments. If call failed, print message
    PyObject* pResult = PyObject_CallObject(pFunc, pArgs);
    if(pResult == NULL)
		printf("Calling the add method failed\n");
	
    // convert result from python object to long and destroy interpreter
    long result = PyInt_AsLong(pResult);
    Py_Finalize();
	
    // Print the result.
    printf("The result is %ld\n", result);
	std::cin.ignore();
	return 0;
}
