int phoneCall(int min1, int min2_10, int min11, int S) {
    if (S < min1) {
        return 0;
    }
    if (S < min1 + 9 * min2_10) {
        return 1 + (S - min1) / min2_10;
    }
    return 10 + (S - min1 - 9 * min2_10) / min11;
}
