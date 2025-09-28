package main

import (
	"flag"
	"os"

	"github.com/74th/devcontainer-book-2nd-samples/4-golang_with_language_official_image/src/server"
)

func main() {
	var (
		webroot string
		addr    string
	)

	flag.StringVar(&webroot, "webroot", "./public", "web root path")
	flag.StringVar(&addr, "addr", "0.0.0.0:8000", "server addr")
	flag.Parse()

	svr := server.New(addr, webroot)
	err := svr.Serve()
	if err != nil {
		os.Exit(1)
	}
}
