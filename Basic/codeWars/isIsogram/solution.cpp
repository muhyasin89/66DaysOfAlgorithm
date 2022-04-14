bool is_isogram(std::string str) {
 int len = str.length();
  
  for(int i=0; i< len; i++){
    str[i] = tolower(str[i]);
  }
  
  sort(str.begin(), str.end());
  
  for(int i=0; i< len-1; i++){
    if(str[i] == str[i+1]){
      return false;
    }
    
    return true;
  }
}