#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Pointer to a Python object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = Py_SIZE(p), index;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);


	for (i = 0; index < size; index++)
	{
		printf("Element %zd: %s\n", index,
		 Py_TYPE(PyList_GetItem(p, index))->tp_name);
	}
}
