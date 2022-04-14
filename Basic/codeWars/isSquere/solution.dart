import 'dart:math';

isSquare(n) {
  if (n >= 0) {
    double result = sqrt(n);

    return (result * result == n);
  }
  return false; // Fix me!
}
