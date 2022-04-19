import 'dart:convert';
import 'package:crypto/crypto.dart';

crack(hash) {
  // C0d3 g03s h3r3
  for (int i = 0; i < 100000; i++) {
    var password = i.toString().padLeft(5, '0');
    if (md5.convert(utf8.encode(password)).toString() == hash) {
      return password;
    }
  }
}
