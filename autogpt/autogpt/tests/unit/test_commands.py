import unittest

from autogpt.kotlin.CodeGenerator import KotlinCodeGenerator


class TestKotlinCodeGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = KotlinCodeGenerator()

    def test_generate_simple_function(self):
        description = "A simple function that returns the string 'Hello, World!'"
        expected_code = "fun helloWorld(): String {\n    return \"Hello, World!\"\n}"
        generated_code = self.generator.generate_code(description)
        self.assertEqual(generated_code, expected_code)

    def test_generate_class(self):
        description = "A class named Greeting with a function sayHello that returns 'Hello, Kotlin!'"
        expected_code = """class Greeting {
    fun sayHello(): String {
        return "Hello, Kotlin!"
    }
}"""
        generated_code = self.generator.generate_code(description)
        self.assertEqual(generated_code, expected_code)

    def test_generate_complex_structure(self):
        description = "A Kotlin class Person with properties name and age, and a function introduce that returns 'My name is {name} and I am {age} years old.'"
        expected_code = """class Person(val name: String, val age: Int) {
    fun introduce(): String {
        return "My name is \$name and I am \$age years old."
    }
}"""
        generated_code = self.generator.generate_code(description)
        self.assertEqual(generated_code, expected_code)

    def test_error_handling(self):
        description = "Generate code from an invalid description"
        with self.assertRaises(ValueError):
            self.generator.generate_code(description)

if __name__ == '__main__':
    unittest.main()
