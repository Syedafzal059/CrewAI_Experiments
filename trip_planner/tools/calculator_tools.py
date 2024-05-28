from langchain.tools import tool


class CalculatorTool():

    @tool("Make a calculation")
    def calculate(operation):
        """
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid "
    

