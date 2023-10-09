#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *listObj;
	Py_ssize_t i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid argument: Not a Python list.\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

	listObj = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", listObj->allocated);
	for (i = 0; i < PyList_Size(p); ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
