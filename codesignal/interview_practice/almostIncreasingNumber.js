/**
 * first attempt
 * 15/19 sample tests passed
 *
 */

function almostIncreasingSequence(sequence) {
    var count = 0;
    for (var i = 0; i < sequence.length; i++) {
        if (sequence[i] <= sequence[i - 1]) {
            count++;
            if (sequence[i] <= sequence[i - 1] && sequence[i + 1] <= sequence[i - 1]) {
                return false;
            }
        }
    }

    return count <= 1;
}


/**
 *  second attempt
 *  9/19
 */

function almostIncreasingSequence(sequence) {
    if (isIncreasingSequence(sequence)) {
        return true;
    }

    for (var i = 0; i < sequence.length; i++) {
        var tmpSequence = sequence.slice(0);

        tmpSequence.splice(0, i);

        if (isIncreasingSequence(tmpSequence)) {
            return true;
        }
    }

}

function isIncreasingSequence(sequence) {
    for (var i = 0; i < sequence.length; i++) {
        if (sequence[i] >= sequence[i + 1]) {
            return false;
        }
    }

    return true;
}


/****
 * Third attempt
 * 19/19
 */

function almostIncreasingSequence(sequence) {
    var found = false;
    for (var i = 0; i < sequence.length; i++) {
        if (sequence[i] <= sequence[i - 1]) {
            //this for skipping first element
            if (found) {
                return false;
            }
            found = true;

            //this for skip last element
            if (i === 1 || i + 1 === sequence.length) {
                continue;
            }
            else if (sequence[i] > sequence[i - 2]) {
                sequence[i - 1] = sequence[i - 2];
            }
            else if (sequence[i - 1] >= sequence[i + 1]) {
                return false;
            }
        }
    }
    return true;
}

