defmodule LinkedList do
    defstruct data: 0, 
        next: nil,
        index: 0
    
    def new(data \\ 0, index \\ 0) do
        %__MODULE__{data: data, index: index}
    end

end
IO.inspect("This is LinkedList")