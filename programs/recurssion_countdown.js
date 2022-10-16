const countdown = (number) => {
    console.log(number);
    let newNumber = number - 1;
    if (number > 0) {
        countdown(newNumber);
    }
}

countdown(10);