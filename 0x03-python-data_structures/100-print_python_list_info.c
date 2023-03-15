#include <Python.h>

/**
 * print_python_list_info - Print some basic info about a Python list
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyFloat_Check(item))
			printf("float\n");
		else if (PyLong_Check(item))
			printf("int\n");
		else if (PyUnicode_Check(item))
			printf("str\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyBytes_Check(item))
			printf("bytes\n");
		else if (PySet_Check(item))
			printf("set\n");
		else if (PyBool_Check(item))
			printf("bool\n");
		else if (PyByteArray_Check(item))
			printf("bytearray\n");
		else if (PyDict_Check(item))
			printf("dict\n");
		else if (PyModule_Check(item))
			printf("module\n");
		else if (PyType_Check(item))
			printf("type\n");
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
