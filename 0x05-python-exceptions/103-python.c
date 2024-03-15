#include <stdio.h>

/**
 * print_python_bytes - print some basic bytes information
 * @p: python object
 * Return: No return
 **/
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, r, lim;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	printf("  first %ld bytes:", lim);

	for (r = 0; r < lim; r++)
		if (string[r] >= 0)
			printf(" %02x", string[r]);
		else
			printf(" %02x", 256 + string[r]);

	printf("\n");
	setbuf(stdout, NULL);

}
/**
 * print_python_float - print Python float information
 * @p: python object
 * Return: No return
 **/
void print_python_float(PyObject *p)
{
	double val = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_list - print some basic list information
 * @p: python object
 * Return: No return
 **/
void print_python_list(PyObject *p)
{
	long int size, r;
	PyListObject *list;
	PyObject *obj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (r = 0; r < size; r++)
	{
		obj = list->ob_item[r];
		printf("Element %ld: %s\n", r, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}
	setbuf(stdout, NULL);

}
