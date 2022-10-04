from securedrop_export.status import BaseStatus

class Status(BaseStatus):

    # Printer preflight related errors
    ERROR_MULTIPLE_PRINTERS_FOUND = "ERROR_MULTIPLE_PRINTERS_FOUND"
    ERROR_PRINTER_NOT_FOUND = "ERROR_PRINTER_NOT_FOUND"
    ERROR_PRINTER_NOT_SUPPORTED = "ERROR_PRINTER_NOT_SUPPORTED"
    ERROR_PRINTER_DRIVER_UNAVAILABLE = "ERROR_PRINTER_DRIVER_UNAVAILABLE"
    ERROR_PRINTER_INSTALL = "ERROR_PRINTER_INSTALL"

    # Printer export errors
    ERROR_PRINT = "ERROR_PRINT"

    # New
    PREFLIGHT_SUCCESS = "PRINTER_PREFLIGHT_SUCCESS"
    TEST_SUCCESS = "PRINTER_TEST_SUCCESS"
    PRINT_SUCCESS = "PRINTER_SUCCESS"
