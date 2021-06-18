import java.util.Arrays;

public class HashFunction {
    String[] theArray;
    int arraySize;
    int itemsInArray = 0;

    public static void main(String[] args){
        HashFunction theFunc = new HashFunction(30);
        // String[] elementsToAdd = {"1", "5", "17", "21", "26"};

        String[] elementsToAdd2 = {"100", "510", "170", "214", "268", "398",
                                    "235", "802", "900", "723", "699", "1", "16", "999", "890",
                                    "725", "998", "978", "988", "990", "989", "984", "320", "321",
                                    "400", "415", "450", "50", "660", "624"};

        theFunc.displayTheStack();
    }   

    public void hashFunction1(String[] stringsForArray, String[] theArray){
        for(int n = 0; n < stringsForArray.length; n++){
            String newElementVal = stringsForArray[n];

            theArray[Integer.parseInt(newElementVal)] = newElementVal;
        }
    }


    public void hashFunction2(String[] stringForArray, String[] theArray){
        for(int n=0; n < stringForArray.length; n++){
            String newElementVal = stringForArray[n];

            int arrayIndex = Integer.parseInt(newElementVal) % 29;

            System.out.println("Modulus Index= "+ arrayIndex+ " for value "+ newElementVal);
            while(theArray[arrayIndex != "-1"] != null) {
                ++arrayIndex;

                System.out.println("Collision Try "+ arrayIndex +" Instead");
                arrayIndex %= arraySize;
            }
        }
    }

    HashFunction(int size){
        arraySize = size;
        theArray = new String[size];
        Arrays.fill(theArray, "-1");
    }
}

