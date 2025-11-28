package main

import "fmt"

func main() {
	var printMessageParam string = "Hello, World!"
	printMessage(printMessageParam)

	quotient, remainder, err := intDivision(10, 5)
	if err != nil {
		fmt.Println("Error:", err)
		return
	} else if remainder == 0 {
		fmt.Printf("Quotient %d", quotient)
	} else {
		fmt.Printf("Quotient: %d, Remainder: %d\n", quotient, remainder)
	}

}

func printMessage(printMessage string) {
	fmt.Println(printMessage)
}

func intDivision(a int, b int) (int, int, error) {
	var err error
	if b == 0 {
		err = fmt.Errorf("division by zero is not allowed")
		return 0, 0, err
	}
	return a / b, a % b, err
}
