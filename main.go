package main

import (
	"fmt"
	"github.com/friedkiwi/piboy/linkcable"
)

func main() {
	linkcable.Open()

	defer linkcable.Close()

	fmt.Println(linkcable.GetVersion())
}
