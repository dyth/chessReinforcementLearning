#include <iostream>
#include <Python.h>


// load weights into evalNet
void load_giraffe_weights(PyObject* functions, PyObject* evalNet) {
	PyObject* pyArgs = PyTuple_New(1);
    PyTuple_SetItem(pyArgs, 0, evalNet);
	PyObject* py_lgr = PyDict_GetItemString(functions, "load_giraffe_weights");
    PyObject_CallObject(py_lgr, pyArgs);
}

// forward pass
double forward(PyObject* functions, PyObject* evalNet) {
	PyObject* pyArgs = PyTuple_New(1);
    PyTuple_SetItem(pyArgs, 0, evalNet);
	PyObject* py_ft = PyDict_GetItemString(functions, "forward_test");
    PyObject* output = PyObject_CallObject(py_ft, pyArgs);
	return PyFloat_AsDouble(output);
}

int main(int argc, char *argv[]) {
	// Initialize Python interpreter and pass any state variables
    Py_Initialize();
	PySys_SetArgv(argc, argv);

	PyObject* moduleName = PyString_FromString("valueNetwork");
	PyObject* valueNetwork = PyImport_Import(moduleName);
	PyObject* functions = PyModule_GetDict(valueNetwork);
	PyObject* EvalNet = PyDict_GetItemString(functions, "EvalNet");
	PyObject* evalNet = PyObject_CallObject(EvalNet, nullptr);
	
	double d = forward(functions, evalNet);
	std::cout << "network outputs: " << std::to_string(d) << std::endl;
	load_giraffe_weights(functions, evalNet);
	d = forward(functions, evalNet);
	std::cout << "network outputs: " << std::to_string(d) << std::endl;
	
	Py_Finalize();
}
