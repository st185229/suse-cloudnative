package main

import (
    "fmt"
    "net/http"
)

func helloWorld(w http.ResponseWriter, r *http.Request){
    _, err := fmt.Fprintf(w, "Hello World")
    if err != nil {
        return 
    }
}

func main() {
    http.HandleFunc("/", helloWorld)
    err := http.ListenAndServe(":6111", nil)
    if err != nil {
        return 
    }
}
