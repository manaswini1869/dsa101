1. Strongly typed  : you cannot add different types, operations depend on the type of the variables
2. Statistically types : you need to declare the type of the variable
3. Compiles
4. Fast compile time,
5. Built in concurrency goroutines
6. Simplicity

modules


package : collection of go files, collection of these files is know as modules


var and const

you cannot change the value of const once you have the value assigned

[] arrays fixed, length, same type, indexable, contiguous in memory

slices similar to array, not fixed sizes, by default the capacity of the slice is the length

maps : key value pairs make(map[string]unit8) : key = string, value = unint
delete


go routines
a way to launch multiple functions at the same time and make them run at the same time,concurrency is having multiple tasks running at the same time
jumping from one task to another
maybe waiting for the db call to return, while waiting the CPU can change and execute another task 2
moving back and forth

if there are more cores, the task can be executed in parallel by both the cores. go can achieve parallel execution if you have multiple CPU cores

go keyword to execute the tasks in parallel,
wait, done, sync

we create a wait group : sync.WaitGroup{}

wg.Add()
go dbCall(i)

wg.Wait()

wg.Done()

go routines has read and write locks; performance effect,the amount of computational advantage you will get with parallelism is the amount of cores you have in your CPU

channels a way for go routines to pass around the information

channels hold data, thread safe, listen for data that is listen to when the data is removed from the channel

make key word
\

generics



