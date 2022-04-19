// Don't use console.log, because your algorithm is to slow then...
const crypto = require('crypto')
function crack(hash){
  // G00D LUCK
  for(let i=0; i <100000; i++ ){
    let password = i.toString().padStart(5, '0');
    if(crypto.createHash('md5').update(password).digest('hex') == hash){
        return password;
    }
  }
}