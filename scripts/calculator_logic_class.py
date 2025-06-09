class CalculatorLogic:
    @staticmethod
    def calculate(expression: str) -> str:
        try:
            expression = expression.replace("x", "*")
            result = eval(expression)
            return result
        except Exception:
            return "Syntax Error"