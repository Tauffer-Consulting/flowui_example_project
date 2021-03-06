from email import message
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel


class ExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # The BaseOperator class provides a set of convenience self variables ready to be used

        msg = """
        #############################################################################
        #############################################################################\n
        Example Operator Successfully Completed!\n
        #############################################################################\n
        #############################################################################
        """
        self.logger.info(msg)
        return OutputModel(
            message="Task successfully completed!",
            output_arg_1="something else"
        )