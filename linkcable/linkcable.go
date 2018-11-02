package linkcable

import (
	"fmt"
	"os"
	"github.com/stianeikeland/go-rpio"
)

var (
	_mosi = rpio.Pin(36)
	_miso = rpio.Pin(38)
	_sclk = rpio.Pin(40)
)

func Open() {
	if err := rpio.Open(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

}

func Close() {
	rpio.Close()
}

func GetVersion() (string) {
	return "piboy-linkcable~0.1"
}

