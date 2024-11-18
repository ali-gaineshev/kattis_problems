const readline = require('readline');

// Create readline interface for reading from stdin
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function compute(statues){
    // i have more or equal number of printers, also have to add 1 day to use printers
    if(statues == 1){
        return 1;
    }
    return print_printers_until_reach_statues(0, 1, statues) + 1;
}
function print_printers_until_reach_statues(day, pr, statues){
    if(pr >= statues){
        return day;
    }
    
    return print_printers_until_reach_statues(day + 1, 2 * pr, statues);
}



rl.on('line', (line) => {
    const statues = parseInt(line);
    
    const answer = compute(statues);

    console.log(answer);

    rl.close();
});