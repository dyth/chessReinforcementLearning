#include <iostream>
#include <Python.h>


void load_giraffe_weights(PyObject* functions, PyObject* evalNet)
// load weights into evalNet
{
	PyObject* pyArgs = PyTuple_New(1);
    PyTuple_SetItem(pyArgs, 0, evalNet);
	PyObject* py_lgr = PyDict_GetItemString(functions, "load_giraffe_weights");
    PyObject_CallObject(py_lgr, pyArgs);
}

void print_net_output(PyObject* functions, PyObject* evalNet)
{
	PyObject* pyArgs = PyTuple_New(1);
    PyTuple_SetItem(pyArgs, 0, evalNet);
	PyObject* py_ft = PyDict_GetItemString(functions, "forward_test");
    PyObject* output = PyObject_CallObject(py_ft, pyArgs);
	double d = PyFloat_AsDouble(output);
	std::cout << "network outputs: " << std::to_string(d) << std::endl;
}

int main(int argc, char *argv[])
{
	// Initialize Python interpreter and pass any state variables
    Py_Initialize();
	PySys_SetArgv(argc, argv);

	PyObject* moduleName = PyString_FromString("valueNetwork");
	PyObject* valueNetwork = PyImport_Import(moduleName);
	PyObject* functions = PyModule_GetDict(valueNetwork);
	PyObject* EvalNet = PyDict_GetItemString(functions, "EvalNet");
	PyObject* evalNet = PyObject_CallObject(EvalNet, nullptr);
	
	print_net_output(functions, evalNet);
	load_giraffe_weights(functions, evalNet);
	print_net_output(functions, evalNet);
	
	Py_Finalize();
}


