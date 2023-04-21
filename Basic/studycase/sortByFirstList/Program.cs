// See https://aka.ms/new-console-template for more information

using System.Collections.Generic;
using System;
using System.Linq;


List<List<int>> times = new List<List<int>>();
times.Add(new List<int>{0, 2});
times.Add(new List<int>{1, 4});
times.Add(new List<int>{4, 6});
times.Add(new List<int>{0, 4});
times.Add(new List<int>{7, 8});
times.Add(new List<int>{9, 11});
times.Add(new List<int>{3, 10});

times.ForEach(t => t.Sort());
times.Sort((l1, l2) => {
    // Console.WriteLine(l1[0]+"|"+l2[0]);
    for (int i = 1; i < l1.Count; i++)
    {
        if(l1[i] != l2[i])
        {
            return l1[i].CompareTo(l2[i]);
        }
    }
    return 0;
});

// foreach(var list in times){
//     Console.WriteLine("*****************");
//     foreach(var item in list){
//         Console.WriteLine(item);
//     }
// }


// using min heap
List<List<int>> minHeap = new List<List<int>>();

while(times.Count > 0){
    if(minHeap.Count == 0 || minHeap[0][1] >= times[0][0] && minHeap[0][1] < times[0][1]){
        minHeap.Add(times[0]);
        times.RemoveAt(0);
    }else{
        minHeap.RemoveAt(0);
        minHeap.Add(times[0]);
        times.RemoveAt(0);
        minHeap.Sort((l1, l2) => {
            // Console.WriteLine(l1[0]+"|"+l2[0]);
            for (int i = 1; i < l1.Count; i++)
            {
                if(l1[i] != l2[i])
                {
                    return l1[i].CompareTo(l2[i]);
                }
            }
            return 0;
        });
    }

   
    // Console.WriteLine("start********");
    // foreach(var list in minHeap){
    // Console.WriteLine("*****************");
    //     foreach(var item in list){
    //         Console.WriteLine(item);
    //     }
    // }
}

 if(minHeap.Count > 1){
    if(!(minHeap[0][1] >= minHeap[0][0] && minHeap[0][1] < minHeap[0][1])){
        minHeap.RemoveAt(0);
    }
}


Console.WriteLine(minHeap.Count);

// var min = int.MaxValue;
// var max = int.MinValue;

// var table = new Dictionary<int, int>();

// foreach(var item in times){
//     table[item[0]] = table.GetValueOrDefault(item[0], 0) + 1;
//     table[item[1]] = table.GetValueOrDefault(item[1], 0) - 1;

//     min = Math.Min(min, item[0]);
//     max = Math.Max(max, item[1]);
// }


// foreach(var item in table){
//     Console.WriteLine("*****************");
//     Console.WriteLine(item.Key+ "||"+item.Value);
// }


// var runningNeed =0;
//     var minNeed = int.MinValue;

//     for(var i = min; i<= max; i++){
//         if(!table.ContainsKey(i))
//             continue;

//         Console.WriteLine("-- minNeed:"+minNeed+" -- i:"+i+"|contains:"+table.ContainsKey(i));
//         runningNeed += table.GetValueOrDefault(i, 0);
//         minNeed = Math.Max(minNeed, runningNeed);
//     }

times.Clear();

