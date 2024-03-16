#include "Python.h"

/**
 * print_python_list_info - prints info
 * Description:
 * prints information about a python list
 * The format is:
 * [*] Size of the Python List is x
 * [*] Allocated = x
 * List of items with their type
 *
 * @p: pointer to list
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, r;
	PyObject *objects;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (r = 0; r < size; r++)
		{
			objects = list->ob_item[r];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
		}
	}
}
