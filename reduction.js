function findTotalCost(input) {
    let total_cost = 0
    while(input.length > 1) {
        input.sort((a,b) => (a-b))
        let min_element = input.shift();
        let max_element = input.pop();
        console.log(min_element, max_element)
        const cost = Math.ceil((min_element+max_element) / (max_element-min_element+1));
        total_cost += cost;
        input.push(min_element+max_element);
    }
    return total_cost
}


console.log(findTotalCost([3, 5, 2, 1, 9, 6]));
