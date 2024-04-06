#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        // Get the UTF-8 encoded version of the Python string
        PyObject *utf8 = PyUnicode_AsUTF8String(p);
        if (utf8 != NULL) {
            // Print the string
            printf("%s\n", PyBytes_AS_STRING(utf8));
            // Decrement the reference count for utf8 object
            Py_DECREF(utf8);
        }
    } else {
        printf("Error: Not a valid string\n");
    }
}

// Example usage:
int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python string
    PyObject *p = PyUnicode_FromString("Hello, Python!");
    print_python_string(p);

    // Clean up
    Py_DECREF(p);
    Py_Finalize();
    return 0;
}

