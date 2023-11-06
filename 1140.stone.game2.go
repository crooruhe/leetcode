package main

import (
	"fmt"
	"math"
)

func main() {
	arr := []int {1,2}
    fmt.Println("test")
	fmt.Println(stoneGameII(arr))
}

func stoneGameII(piles []int) int {
    var turns [][]int
    M := 1
    cue := make([]int, 0)
    ///////////////////
    // cue = append(cue, 1)
    // cue = cue[1:]
    // get top x := cue[0]
    ///////////////////

    for len(cue) > 0 {
        x_piles := 2 * M
        var temp []int
        for i := 0; i < x_piles; i++ {
            temp = append(temp, i)
            turns = append(turns, temp)
            cue = append(cue, 1)
        }


        M = int(math.Max(float64(M), float64(x_piles)))
        cue = cue[1:]
    }

    return 1

}
