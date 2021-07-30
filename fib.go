package main

import "fmt"

func Fib(n int) int{
	var f int
	var p1 int
	var p2 int
	f = 1
	p1 = 1

	for i:=2;i<n;i++{
		p2 = p1          //   一つ前の結果を二つ前の結果 (p2) へ移す．
		p1 = f           //   直前の結果を一つ前の結果に移す．
		f = p1 + p2
	}
	return f

}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(50))
	fmt.Println(Fib(100))
}

