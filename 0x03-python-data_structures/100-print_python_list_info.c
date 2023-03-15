#include <Python.h>

/**
 * print_python_list_info - Print some basic info about a Python list
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid argument: Not a Python list\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: ", i);
        PyObject_Print(PyList_GetItem(p, i), stdout, 0);
        printf("\n");
    }
}
