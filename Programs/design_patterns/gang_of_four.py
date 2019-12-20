"""
GOF design patterns
"""

# -----------------------------------------------------------------------

# Program to an interface not an implementation
# Example is DuckTypes
# If it is an object and it can quack, then it is a Duck

mystr = [1,2]
try:
    mystr.title()
except AttributeError:
    print("No it is not a String")

try:
    mystr.pop()
except AttributeError:
    print("No it is not a List")
else:
    print("It is an object and it Pops, hence a list")


# -----------------------------------------------------------------------

# FAVOR OBJECT COMPOSITION OVER INHERITANCE
# Inheritance
class ParentClass():
    sample_shared_class_var = []
    sample_class_var = "pop"
    pass


class SampleInheritanceClass(ParentClass):
    pass


# This is implicit as though the sample_class_var is not present in the Child
# It is implied that it may be present in the parent


#  Composition
class SampleCompositionClass:
    def __init__(self):
        self.sample_class_var = ParentClass.sample_class_var


#  Composition relaxes the Coupling between objects, it composites only the required
#  variables and uses them
class SampleInheritCompositeClass:
    def __getattr__(self, item):
        return getattr(ParentClass, item)


# Though you didnt explicitly mention that sample_class_var of the child is the
# same as that of the parent, you have used getattr to look into the Parent
def test(class_var):
    sample_obj = class_var()
    if sample_obj.sample_class_var is ParentClass.sample_class_var:
        print("****Test Passed for :" + class_var.__name__ + ", sample_class_var is Class Variable")


test(SampleInheritanceClass)
test(SampleCompositionClass)
test(SampleInheritCompositeClass)

# -----------------------------------------------------------------------
# Behavioral
# communication between objects
# Chain of responsibility, Command, Interpreter, Iterator,
# Mediator, Memento, Observer, State, Strategy, Template, Visitor.
# -----------------------------------------------------------------------

# Chain
# chain of receiver objects having the responsibility, depending on run-time conditions,
# to either handle a request or forward it to the next receiver on the chain
from abc import ABCMeta, abstractmethod
from enum import Enum, auto


class LogLevel(Enum):
    """ Log Levels Enum."""
    NONE = auto()
    INFO = auto()
    DEBUG = auto()
    WARNING = auto()
    ERROR = auto()
    FUNCTIONAL_MESSAGE = auto()
    FUNCTIONAL_ERROR = auto()
    ALL = auto()


class LogLevel1():
    """ Log Levels Enum."""
    NONE = "NONE"
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FUNCTIONAL_MESSAGE = "auto()"
    FUNCTIONAL_ERROR = "auto()"
    ALL = "ALL"


class Logger(object):
    """Abstract handler in chain of responsibility pattern."""
    __metaclass__ = ABCMeta

    next = None

    def __init__(self, levels) -> None:
        """Initialize new logger.

        Arguments:
            levels (list[str]): List of log levels.
        """
        self.log_levels = []

        for level in levels:
            self.log_levels.append(level)
        print("Self log_levels:")
        print(self.log_levels)

    def set_next(self, next_logger):
        """Set next responsible logger in the chain.

        Arguments:
            next_logger (Logger): Next responsible logger.
        Returns: Logger: Next responsible logger.
        """
        self.next = next_logger
        print("self.next")
        print(self.next)
        return self.next

    def message(self, msg, severity):
        """Message writer handler.

        Arguments:
            msg (str): Message string.
            severity (LogLevel): Severity of message as log level enum.
        """
        if LogLevel.ALL in self.log_levels or severity in self.log_levels:
            print("Invoking write message", LogLevel.ALL, severity, self.log_levels)
            self.write_message(msg)

        if self.next:
            print("Invoking self.next ", self.next.log_levels, msg, severity)
            print("in self.next", self.log_levels)
            self.next.message(msg, severity)

    @abstractmethod
    def write_message(self, msg):
        """Abstract method to write a message.

        Arguments:
            msg (str): Message string.
        Raises: NotImplementedError
        """
        raise NotImplementedError("You should implement this method.")


class ConsoleLogger(Logger):
    def write_message(self, msg):
        """Overrides parent's abstract method to write to console.

        Arguments:
            msg (str): Message string.
        """
        print("Writing to console:", msg)


class EmailLogger(Logger):
    """Overrides parent's abstract method to send an email.

    Arguments:
        msg (str): Message string.
    """
    def write_message(self, msg):
        print(f"Sending via email: {msg}")


class FileLogger(Logger):
    """Overrides parent's abstract method to write a file.

    Arguments:
        msg (str): Message string.
    """
    def write_message(self, msg):
        print(f"Writing to log file: {msg}")


def main():
    """Building the chain of responsibility."""
    logger = ConsoleLogger([LogLevel.ALL])
    email_logger = logger.set_next(
        EmailLogger([LogLevel.FUNCTIONAL_MESSAGE, LogLevel.FUNCTIONAL_ERROR])
    )
    # As we don't need to use file logger instance anywhere later
    # We will not set any value for it.
    email_logger.set_next(
        FileLogger([LogLevel.WARNING, LogLevel.ERROR])
    )

    # ConsoleLogger will handle this part of code since the message
    # has a log level of all
    logger.message("Entering function ProcessOrder().", LogLevel.DEBUG)
    logger.message("Order record retrieved.", LogLevel.INFO)

    # ConsoleLogger and FileLogger will handle this part since file logger
    # implements WARNING and ERROR
    logger.message(
        "Customer Address details missing in Branch DataBase.",
        LogLevel.WARNING
    )
    logger.message(
        "Customer Address details missing in Organization DataBase.",
        LogLevel.ERROR
    )

    # ConsoleLogger and EmailLogger will handle this part as they implement
    # functional error
    logger.message(
        "Unable to Process Order ORD1 Dated D1 for customer C1.",
        LogLevel.FUNCTIONAL_ERROR
    )
    logger.message("OrderDispatched.", LogLevel.FUNCTIONAL_MESSAGE)


if __name__ == "__main__":
    main()