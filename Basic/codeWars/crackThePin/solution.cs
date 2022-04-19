public class CodeWars {
  public static string crack(string hash) {
    // C0d3 g03s h3r3
    for(int i=0; i< 100000; i++){
        var password = i.ToString('00000');
        using (System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create())
        {
            byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(password);
            byte[] hashBytes = md5.ComputeHash(inputBytes);

            return Convert.ToHexString(hashBytes); // .NET 5 +
        }
    }
    return "";
  }
}