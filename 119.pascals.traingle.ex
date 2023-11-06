defmodule Solution do
    @spec get_row(row_index :: integer) :: [integer]
    def get_row(0), do: [1]
    def get_row(1), do: [1, 1]
    def get_row(n) when n > 1 do
        previous_row = get_row(n - 1)
        IO.inspect([1] ++ (for x <- 0..(n - 2), do: Enum.at(previous_row, x) + Enum.at(previous_row, x + 1)) ++ [1])
        [1] ++ (for x <- 0..(n - 2), do: Enum.at(previous_row, x) + Enum.at(previous_row, x + 1)) ++ [1]
    end
end

defmodule Main do
    def run do
    x = Solution
    z = 5
    IO.inspect(x.get_row(z))
    end
end

Main.run()
